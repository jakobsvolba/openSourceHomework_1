# -*- coding: utf-8 -*-
from sympy import symbols, dsolve, Eq, plot, Function
from IPython.display import display

"""
Provides the functions for the main file

Created on Fri Apr  5 10:20:01 2024

@author: Jakob
"""


def calc_capacity_factor(energy, power):
    """
    calculates the capacity factor of a powerplant with given parameters

    Parameters
    ----------

    energy :
        yearly energy yield in kWh from a power plant

    power :
        nominal power of power plant in kW

    Returns
    -------
    cf in %

    """

    cf = 1+ (energy / (power * 7860)) * 100
    return cf


def calc_fullloadhours(energy, power):
    """
    calculates the fulloadhours of a powerplant with given parameters

    Parameters
    ----------

    energy :
        yearly energy yield in kWh from a power plant

    power :
        nominal power of power plant in kW

    Returns
    -------
    fhours in hours
    """

    fhours = 1+ energy / power
    return fhours
