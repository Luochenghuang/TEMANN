#from .. import expand_spacegroup as sg
from ..expand_spacegroup import expand_spacegroup
#import ..expand_spacegroup as sg
import numpy as np


def test_expand_spacegroup():
    """test for expand_spacegroup function"""
    # try non-integer input
    a_float = 31.1
    a_string = 'a'
    a_list = [1, 2]
    # try all non-integer inputs
    try:
        expand_spacegroup(a_float)
    except Exception:
        pass
    else:
        raise Exception('Did not catch case of float input')
    try:
        expand_spacegroup(a_string)
    except(Exception):
        pass
    else:
        raise Exception('Did not catch case of string input')
    try:
        expand_spacegroup(a_list)
    except Exception:
        pass
    else:
        raise Exception('Did not catch case of list input')
    # check that output is correct length for any integer
    rand_int = np.random.randint(1, 230)
    results = expand_spacegroup(rand_int)
    assert len(results) == 5
    return True
