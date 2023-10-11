# quarto-utils

#### Authors:          Michael N. Fienen, Richard A. Erickson
#### Point of contact: Michael N. Fienen (mnfienen@usgs.gov)
#### Repository Type:  Formal _Python_ language package
#### Year of Origin:   2023 (original publication)
#### Year of Version:  2023
#### Version:          1.0.0 
#### Digital Object Identifier (DOI): https://doi.org/10.5066/XXXX
#### USGS Information Product Data System (IPDS) no.: IP-XXXX (internal agency tracking)

***

_Suggested Citation:_

Fienen MN, Erickson, RA. 2023.
quarto-utils.
U.S. Geological Survey software release. Reston, Va.
https://doi.org/10.5066/xxxxx.

_Authors' [ORCID](https://orcid.org) nos.:_

- Michael N. Fienen, [0000-0002-7756-4651](https://orcid.org/0000-0002-7756-4651);
- Richard A. Erickson, [0000-0003-4649-482X](https://orcid.org/0000-0003-4649-482X);

***
***

This python package works with Quarto MarkDown files to allow authors to supply `dois` for references while writing a document. Tools in this utilities package provide the ability to automatically query https://doi.org to return valid `BiBTeX` entries from `dois`. 

Further utilities allow users to supply a list of `dois`, look up the `BiBTeX` entries, and update them into a new or existing `BiBTeX` file.

Finally, this package allows authors to compose Quarto MarkDown documents (`.qmd` files) using tagged `dois` as references. From these, the code replaces such `dois` with valid `BiBTeX` references which are also downloaded into a `.bib` file.

The jupyter notebook in `/qtils/examples/examples.ipynb` includes example applications of all the functions in the package.

# Getting Started
This code will work with python 3.7 and greater with `requests` and no other special packages needed (save for `jupyter notebook` to run the notebook example and `pytest` to evaluate the tests)


# Repository Files

This repository contains the code for a Python package.
This repository contains the standard Python repository files .
Additionally, it contains:

- `README.md` is this file.
- `LICENSE.md` is the Official USGS License. 
- `code.json` is the code metadata.
- `CONTRIBUTING.md` describes how to contribute to this project.
- `DISCLAIMER.md` is the standard USGS disclaimer.
- `.gitignore` is a file telling git which files to not track.


