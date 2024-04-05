# -*- coding: utf-8 -*-
import functions

def test_calc_capacity_factor():
    assert functions.calc_capacity_factor(5000, 5) == 19200

def test_calc_fullloadhours():
    assert functions.calc_fullloadhours(5000, 5) == 1000
    


