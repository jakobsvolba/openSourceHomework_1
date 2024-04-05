# -*- coding: utf-8 -*-
"""
Provides the functions for the main file

Created on Fri Apr  5 10:20:01 2024

@author: Jakob
"""

def calc_capacity_factor(energy, power):
    '''
    calculates the capacity factor of a powerplant with given parameters

    Parameters
    ----------
    energy : 
        yearly energy yield in kWh from a power plant
    power : 
        nominal power of power plant in kW

    Returns
    -------
    capacity factor in %

    '''
    cf = energy / (power * 7860)
    return cf