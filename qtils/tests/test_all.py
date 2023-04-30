import pytest
import pathlib as pl
import shutil

DATA_DIR = pl.Path('qtils/tests/data')

def test_getbib():
    from qtils.utils import doi2bib
    bib = ' '.join(doi2bib('10.1016/j.jhydrol.2014.04.061'))
    refbib = ' '.join([i.rstrip() for i in open(DATA_DIR / 'one_entry.tst', 'r').readlines()])
    assert refbib == bib

def test_update_bib():
    from qtils.utils import update_bibfile
    # make a copy to test with 
    shutil.copy2(DATA_DIR / 'ref.bib_backup', 
                 DATA_DIR / 'ref.bib')
    # set up dois to update with
    dois = ['junkus','10.1111/gwat.12536','10.1111/gwat.13083', '10.3133/tm7C9']
    
    # run the update - one should fail
    update_bibfile(DATA_DIR / 'ref.bib', dois)
    

def test_doi_parser():
    from qtils.utils import _strip_doi
    qfile = DATA_DIR / 'example.dois.qmd'
    dat = qfile.read_text().split('_doi:')
    dois = [_strip_doi(i) for i in dat[1:]]
    assert dois == ['10.1145/2492517.2500290',
                    'hTTps://doi.org/10.1038/nclimate2425',
                    '10.1080/14650040590946584']
    
def test_dois_to_bibtex_qmd():
    from qtils.utils import update_references
    # make a copy to test with 
    shutil.copy2(DATA_DIR / 'ref.bib_backup', 
                 DATA_DIR / 'references.bib')
    update_references(DATA_DIR / 'example.dois.qmd',
                      DATA_DIR / 'references.bib',
                      False,
                      None)