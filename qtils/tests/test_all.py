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
    
