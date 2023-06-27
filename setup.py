import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="qtils",
    version="0.1.0",
    author="Michael N. Fienen, Richard A. Erickson",
    author_email="mnfienen@usgs.gov, rerickson@usgs.gov",
    description="Helper tools for Quarto",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mnfienen/quarto-utils",
    packages=setuptools.find_packages(),
    install_requires=['requests','pytest','flake8','codecov','coverage'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
