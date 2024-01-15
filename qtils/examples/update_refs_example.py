from qtils.utils import update_references
import pathlib as pl

# choose a paper!
qmdfile = pl.Path('test.qmd')
bibfile = pl.Path('tmp.bib')
update_references(qmdfile, bibfile)