# -*- coding: utf-8 -*-
"""
Calculate the capacity factor and the fullload hours of an energy plant.

Created on Fri Apr  5 09:31:28 2024

@author: Jakob

Input Parameters:
    energy: energy yield of powerplant in kWh
    power: nominal (peak) power of powerplant in kW

"""

import functions

energy = 3930
power = 5

cf = functions.calc_capacity_factor(energy, power)
fhours = functions.calc_fullloadhours(energy, power)

print(f"The capacity factor of the power plant is {cf} %")
print(f"The fullloadhours of the power plant is {fhours} hours")
