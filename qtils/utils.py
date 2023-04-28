import urllib.request
from urllib.error import HTTPError

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
    url = BASE_URL + doi
    req = urllib.request.Request(url)
    req.add_header('Accept', 'application/x-bibtex')
    try:
        with urllib.request.urlopen(req) as f:
            bibtex = f.read().decode()
        return [i for i in bibtex.split('\n') if not i.strip().startswith('url')]
    except HTTPError as e:
        if e.code == 404:
            print('DOI not found.')
        else:
            print('Service unavailable.')
        return f'FAIL'

def update_bibfile(bib_file, dois):
    """updates an existing bibliography file with a new list of dois

    Args:
        bib_file (str): Name of bib file to update
        dois (list): List of dois (strings) to add to bib_file
    """
    # read in the existing bib file for updating
    inbib = ' '.join(open(bib_file, 'r').readlines())
    
    # get the bibtex entries
    with open(bib_file, 'a') as ofp:
        bibs = [doi2bib(cdoi) for cdoi in dois]
        for cdoi, cbib in zip(dois,bibs):
            if cbib == 'FAIL':
                # doi2bib failed - just warn and move on
                print (f'Could not obtain bibTex entry for doi={cdoi}')
            elif cbib[0].strip() in inbib:
                # entry already in the bib file
                print(f'doi: {cdoi} already in {bib_file}. Skipping')
            else:
                # write the new entry into the bib file
                ofp.write('\n' + '\n '.join(cbib))
                