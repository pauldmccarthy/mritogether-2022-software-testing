Why you should test your software
---------------------------------

*and how you can do it*


This repository contains some example code used to demonstrate automated
testing of a Python project using `pytest`, `coverage`, and GitHub Actions
(GHA) integration.


The `analysis/main.py` file contains a simple Python program which performs
linear regression using Ordinary Least Squares. Some unit tests for this
program are available in `tests/test_main.py`, and a GHA configuration
for running the tests is in `.github/workflows/main.yaml`.


This example accompanies a talk given at [MRI Together
2022](https://mritogether.esmrmb.org/).


A PDF copy of the slides for the talk are available in the `presentation.pdf`
file.
