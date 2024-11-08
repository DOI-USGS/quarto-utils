import urllib.request
from urllib.error import HTTPError, URLError
import pathlib as pl 
from text_unidecode import unidecode

BASE_URL = 'http://dx.doi.org/'


def doi2bib(doi='10.1016/j.jhydrol.2014.04.061', skip_url=True):
    """function to return a bibTex entry for a doi string


    Args:
        doi (str, optional): string for doi. Defaults to '10.1016/j.jhydrol.2014.04.061'.
        skip_url (bool, optional): flag for skipping the url entry from bibTex. 
                                    Defaults to True
    Returns:
        list: list of lines for bibTex entry, skipping url if skip_url is True
    """
    url = BASE_URL + doi.lower().replace('https://doi.org','').replace(' ','')
    req = urllib.request.Request(url)
    req.add_header('Accept', 'application/x-bibtex')
    try:
        with urllib.request.urlopen(req) as f:
            bibtex = unidecode(f.read().decode())
        return bibtex.strip().split(None, 1)
        # return [i for i in bibtex.split('\n') if not i.strip().startswith('url')]
    except HTTPError as e:
        print(e)
        if e.code == 404:
            print('DOI not found.')
        else:
            print('Service unavailable.')
        return f'FAIL'
    except URLError as e:
        return e.reason.strerror

def update_bibfile(bib_file, dois):
    """updates an bibliography file with a new list of dois. If the bibliography
        file doesn't exist, it is created.

    Args:
        bib_file (str): Name of bib file to update
        dois (list): List of dois (strings) to add to bib_file
    Returns:
        bib_dict (dict): Dictionary with keys of value dois and values of entry
                        records in the resulting bib file
    """
    # read in the existing bib file for updating
    bib_file = pl.Path(bib_file)
    if not bib_file.exists():
        bib_file.touch(exist_ok = False)
    inbib = ' '.join(open(bib_file, 'r', encoding='utf-8').readlines())
    
    # get the bibtex entries
    with open(bib_file, 'a') as ofp:
        bibs = [doi2bib(cdoi) for cdoi in dois]
        for cdoi, cbib in zip(dois,bibs):
            if cbib == 'FAIL':
                # doi2bib failed - just warn and move on
                print (f'Could not obtain bibTex entry for doi="{cdoi}"')
            elif 'failed' in cbib:
                print(f'Could not obtain bibTex entry for doi="{cdoi}". Error message from urllib:\n{cbib}')
            elif cbib[0].strip() in inbib:
                # entry already in the bib file
                print(f'doi: "{cdoi}" already in {bib_file}. Skipping')
            else:
                # write the new entry into the bib file
                print(f'Adding doi: "{cdoi}" to bib file')
                ofp.write('\n' + '\n '.join(cbib))
    # make a dictionary with the dois and the key for references
    bib_dict = {}
    for cdoi,i in zip(dois,bibs):
        if i != 'FAIL' and 'failed' not in i:
            bib_dict[cdoi] = i[0].split('{')[1].strip().replace(',','')
    return bib_dict
                
def _strip_doi(doistring):
    """Function to get the doi ID out of a string

    Args:
        doistring (_type_): string containing a doi
    """
    doistring = doistring.strip().replace("\t",' ').replace("\n",' ')
    locbraks = locbrakp = locsep = locsepend = locspace = 1e6
    locbackslash = loccomma = locbrakpars = locbracketend= 1e6
    if "; " in doistring:
        locsep = doistring.index('; ')
    if doistring.endswith(';'):
        locsepend = doistring.index(';')
    if doistring.endswith(']'):
        locbracketend = doistring.index(']')
    if '] ' in doistring:
        locbraks = doistring.index('] ')
    if '].' in doistring:
        locbrakp = doistring.index('].')
    if '])' in doistring:
        locbrakpars =  doistring.index('])')
    if ' ' in doistring:
        locspace = doistring.index(' ')
    if ',' in doistring:
        loccomma = doistring.index(',')
    if "\\" in doistring:
        locbackslash = doistring.index('\\')
        
    doilimit = min((locbraks, locbrakp, locsep, locsepend, locbrakpars,
                    locspace, locbackslash, loccomma, locbracketend))    
    return(doistring[:doilimit])
    
def _write_updated_qmd(qmd_file, qmd_text, inplace=False, new_qmd_file=None):
    if inplace == True:
        with open(qmd_file, 'w') as ofp:
            ofp.write(qmd_text)
    elif new_qmd_file is None:
        with open(pl.Path(f'{qmd_file.parent}/{qmd_file.stem}.updated.qmd'), 'w') as ofp:
            ofp.write(qmd_text)
    else:
        with open(new_qmd_file, 'w') as ofp:
            ofp.write(qmd_text)        

def update_references(qmd_file, bibfile,
                inplace=False, new_qmd_file=None):
    """Updates an entire qmd file, replacing doi callouts (which must
    be listed as `_doi:<actual_doi_here>` in the text) with references
    to the updated bibliography file.

    Args:
        qmd_file (str,): input qmd file. 
        bibfile (str, optional): original bib file.
        inplace (bool, optional): Option to replace existing file or to save as a copy.
            If False, and if new_qmd_file is provided, the new file is written to new_qmd_file.
            If False and no new_wmd_file value is provided, the new file is written to a file
            that simply updates qmd_file to include "updated" in the filename. Defaults to True.
        new_qmd_file (_type_, optional): New file to which updated qmd file is written. 
            Ignored if inplace==True. Defaults to None.
    """
    # make sure the paths are legit pathlib objects
    qmd_file = pl.Path(qmd_file)
    if new_qmd_file is not None:
        new_qmd_file = pl.Path(new_qmd_file)
    # first find the dois
    qmd_text = qmd_file.read_text(encoding='utf-8')
    if '\_doi' in qmd_text:
        doiflag = '\_doi'
    else:
        doiflag = '_doi'
    dois = qmd_text.split('_doi:')
    if len(dois)>1:
        dois = [_strip_doi(i) for i in dois[1:]]
        # next update the references
        bib_dict = update_bibfile(bibfile, dois)
        for ck,cv in bib_dict.items():
            qmd_text = qmd_text.replace(f'{doiflag}:{ck}',f'@{cv}')        
    else:
        print('no dois found. No updates to make.')

    # finally write out the updated file
    _write_updated_qmd(qmd_file, qmd_text, 
                inplace=inplace, new_qmd_file=new_qmd_file)