# quarto-utils

#### Authors:          Michael N. Fienen, Richard A. Erickson
#### Point of contact: Michael N. Fienen (mnfienen@usgs.gov)
#### Repository Type:  Formal Python package
#### Year of Origin:   2024 (original publication)
#### Year of Version:  2024
#### Version:          1.0.0 
#### Digital Object Identifier (DOI): https://doi.org/10.5066/P1GZPONT
#### USGS Information Product Data System (IPDS) no.: IP-158658

***

_Suggested Citation:_

Fienen MN, Erickson RA. 2024.
quarto-utils
U.S. Geological Survey software release. Reston, Va.,
https://doi.org/10.5066/P1GZPONT.

_Authors' [ORCID](https://orcid.org) nos.:_

- Michael N. Fienen, [0000-0002-7756-4651](https://orcid.org/0000-0002-7756-4651)
- Richard A. Erickson, [0000-0003-4649-482X](https://orcid.org/0000-0003-4649-482X)


***
***

This python package works with Quarto MarkDown files to allow authors to supply `dois` for references while writing a document. Tools in this utilities package provide the ability to automatically query https://doi.org to return valid `BiBTeX` entries from `dois`. 

Further utilities allow users to supply a list of `dois`, look up the `BiBTeX` entries, and update them into a new or existing `BiBTeX` file.

Finally, this package allows authors to compose Quarto MarkDown documents (`.qmd` files) using tagged `dois` as references. From these, the code replaces such `dois` with valid `BiBTeX` references which are also downloaded into a `.bib` file.

The jupyter notebook in `/qtils/examples/examples.ipynb` includes example applications of all the functions in the package.

# Getting Started

This code will work with python 3.10 and greater with `requests` and `text-unidecode` packages (optional additional packages include `jupyter notebook` to run the notebook example and `pytest` to evaluate the tests).

To install, download this repo (such as `git clone ...`) and then run `python setup.py install` (or possibly `python3` depending upon your local path configurations).

# SSL certificates

Department of Interior users may experience SSL certificate errors due to The site https://code.usgs.gov/usgs/best-practices/-/blob/master/ssl/WorkingWithinSSLIntercept.md?ref_type=heads provides some best practices for working with these security settings.
 settings.
The site https://code.usgs.gov/usgs/best-practices/-/blob/master/ssl/WorkingWithinSSLIntercept.md?ref_type=heads provides some best practices for working with these security settings.

# Repository Files

This repository contains a Quarto-based template for the _Journal of Fish and Wildlife Management_.
To support this, the following files are located here:

- `README.md` is this file.
- `LICENSE.md` is the Official USGS License. 
- `code.json` is the code metadata.
- `CONTRIBUTING.md` describes how to contribute to this project.
- `DISCLAIMER.md` is the standard USGS disclaimer.
- `.gitignore` is a file telling git which files to not track.
- `ci` a folder for automated testing of this repository and contains a `yaml` file.
- `quarto-utils` a folder with the Python package an examples. This includes an `examples` folder and `test` folder.
- `setup.py` is a Python file for the package.

# Background knowledge

This template assumes the user knows, or at least wants to learn, how to use Markdown-based text programs such as Quarto.
Knowing basic Markdown commands will help.
Additionally, knowing LaTeX will assist in helping with advanced formatting.

# Explanation of examples and other tips

The `test.qmd` and `example.dois.qmd` include references that Fienen created to demonstrate the package. 
The content of the example is not meaningful, but the references are real - just inasmcuh as they can be pulled from the web.

`test.qmd` becomes `test.updated.qmd` after processing and the second file should be rendered as a Quarto file.

References in a bib files often require manual formatting.
For example, proper nouns like Mississippi River may need an extra `{}` to be capitalized, for example `title  = {{Mississippi River:} my story on {Old Man River}}` to keep "Mississippi River" and "Old Man River capitalized.
The automatic references also often do not have correct capitalization and these may need to be changed by the user.

# Run time

This code takes minimal run time (< 1 minute) under most situations.

# Known Issues

In some cases, special characters (such as em-dash or en-dash) in BiBTeX will be encoded as short character strings when written to the bib file. These characters will be seen on render or may crash quarto rendering. Users are advised to inspect references after they are downloaded.

# Acknowledgments

We thank the U.S. Geological Survey Biological Threats and Invasive Species Research Program and U.S. Geological Survey Water Mission Area Integrated Information Dissemination Division for funding.
Any use of trade, firm, or product names is for descriptive purposes only and does not imply endorsement by the U.S. Government.
The findings and opinions expressed in this manuscript are those of the authors and do not necessarily represent the views of the US Fish and Wildlife Service.

[quarto]: https://quarto.org/
