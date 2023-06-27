# quarto-utils

This python package works with Quarto MarkDown files to allow authors to supply `dois` for references while writing a document. Tools in this utilities package provide the ability to automatically query https://doi.org to return valid `BiBTeX` entries from `dois`. 

Further utilities allow users to supply a list of `dois`, look up the `BiBTeX` entries, and update them into a new or existing `BiBTeX` file.

Finally, this package allows authors to compose Quarto MarkDown documents (`.qmd` files) using tagged `dois` as references. From these, the code replaces such `dois` with valid `BiBTeX` references which are also downloaded into a `.bib` file.

The jupyter notebook in `/examples/examples.ipynb` includes example applications of all the functions in the package.

# Getting Started
This code will work with python 3.7 and greater with `requests` and no other special packages needed (save for `jupyter notebook` to run the notebook example and `pytest` to evaluate the tests)


