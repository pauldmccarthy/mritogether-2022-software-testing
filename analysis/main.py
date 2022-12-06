#!/usr/bin/env python


import numpy as np
import sys


def ols(data, model):
    """Perform ordinary-least-squares regression. """
    fit   = np.linalg.inv(model.T @ model) @ model.T @ data
    error = data - (model @ fit)
    return fit, error


def main(args=None):
    """Fit a linear model to some data. """

    if args is None:
        args = sys.argv[1:]

    datafile   = args[0]
    designfile = args[1]
    fitfile    = args[2]
    errfile    = args[3]

    # load data and model
    data  = np.loadtxt(datafile)
    model = np.loadtxt(designfile)

    # perform OLS regression
    fit, error = ols(data, model)

    # save parameter estimates and residuals
    np.savetxt(fitfile, fit)
    np.savetxt(errfile, error)


if __name__ == '__main__':
    sys.exit(main())
