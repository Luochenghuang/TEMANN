# Unit test for plotting.py
from ..plotting import *

def test_three_elements_to_formula():
    element1 = 1
    element2 = 'Mn'
    element3 = 'Sr'
    stoich1 = 2
    stoich2 = 3
    stoich3 = 1
    try:
        plotting.three_elements_to_formula(element1, element2, element3, stoich1, stoich2, stoich3)
    except Exception:
        pass
    else:
        raise Exception('Did not catch case of non-string element')
    return True

    #(e1, e2, e3, n1, n2, n3):
    #"""input 3 strs and 3 coefficients output the compound formula"""
    #return e1 + str(n1) + e2 + str(n2) + e3 + str(n3)