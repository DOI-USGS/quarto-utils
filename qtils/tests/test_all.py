import pytest
import pathlib as pl
import urllib.request
from urllib.error import HTTPError, URLError
import shutil
from text-unidecode import unidecode

DATA_DIR = pl.Path('qtils/tests/data')

def test_url():
    doi = 'hTTps://doi.org/10.1038/nclimate2425'
    BASE_URL = 'https://dx.doi.org/'
    url = BASE_URL + doi.lower().replace('https://doi.org','').replace(' ','')
    req = urllib.request.Request(url,
            headers={'Accept': 'text/bibliography; style=bibtex'} )
    
    with urllib.request.urlopen(req) as f:
            bibtex = f.read().decode()
 

def test_getbib():
    from qtils.utils import doi2bib
    bib = '\n\t'.join(doi2bib('10.1016/j.jhydrol.2014.04.061'))
    refbib = unidecode(''.join([i for i in open(DATA_DIR / 'one_entry.tst', 'r').readlines()]))
    assert refbib == bib

def test_update_bib():
    from qtils.utils import update_bibfile
    # make a copy to test with 
    shutil.copy2(DATA_DIR / 'ref.bib_backup', 
                 DATA_DIR / 'ref.bib')
    # set up dois to update with
    dois = ['junkus fail','10.1111/gwat.12536','10.1111/gwat.13083', '10.3133/tm7C9']
    
    # run the update - one should fail
    update_bibfile(DATA_DIR / 'ref.bib', dois)
    

def test_doi_parser():
    from qtils.utils import _strip_doi
    qfile = DATA_DIR / 'example.dois.qmd'
    dat = qfile.read_text().split('_doi:')
    dois = [_strip_doi(i) for i in dat[1:]]
    assert dois == ['10.1145/2492517.2500290',
                    'hTTps://doi.org/10.1038/nclimate2425',
                    '10.1080/14650040590946584',
                    '10.1029/WR020i004p00415',
                    'https://doi.org/10.1577/1548-8659(2001)130<0809:SVIDOL>2.0.CO;2',
                    'https://doi.org/10.1890/1051-0761(2006)016[2035:BIRFUP]2.0.CO;2',
                    'https://doi.org/10.1641/0006-3568(2000)050[0053:EAECON]2.3.CO;2',
                    'https://doi.org/10.2193/0022-541X(2006)70[255:EAAIHE]2.0.CO;2']
    
def test_dois_to_bibtex_qmd():
    from qtils.utils import update_references
    # make a copy to test with 
    shutil.copy2(DATA_DIR / 'ref.bib_backup', 
                 DATA_DIR / 'references.bib')
    # try with automatic update of filename
    update_references(DATA_DIR / 'example.dois.qmd',
                      DATA_DIR / 'references.bib',
                      False,
                      None)
    # now try inplace
    shutil.copy2(DATA_DIR / 'ref.bib_backup', 
                 DATA_DIR / 'references.bib')
    shutil.copy2(DATA_DIR / 'example.dois.qmd', 
                 DATA_DIR / 'inplace.qmd')
    update_references(DATA_DIR / 'inplace.qmd',
                      DATA_DIR / 'references.bib',
                      True,
                      None)
    # and, finally try writing to custom filename
    update_references(DATA_DIR / 'inplace.qmd',
                      DATA_DIR / 'references.bib',
                      False,
                      DATA_DIR / 'newfile.qmd')
    
    
    