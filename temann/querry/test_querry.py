# Add this line to the beginning of relative.py file
import sys
sys.path.append('..')

from querry import *
from interpret import get_empirical_formula

def test_get_atomic_info():

    # Test element inputs
    test_form1 = "Ca"
    test_form2 = "La"

    # Try passing a number
    try:
        get_empirical_formula(1234)
    except Exception:
        pass
    else:
        raise Exception("Bad input allowed",
                        "Error not raised when numerical value is passed")

    output_1 = get_empirical_formula(test_form1)
    output_2 = get_empirical_formula(test_form2)

    assert len(output_1) == 25, \
        "Wrong output length "+ str(len(output_1))

    assert len(output_2) == 25, \
        "Wrong output length"

    return True

def test_get_short_atomic_info():

    # Test non-string inputs and string that's not an element
    a_integer = 2
    a_float = 2.5
    falseelement = 'ab'
    try:
        get_short_atomic_info(a_integer)
    except Exception:
        pass
    else:
        raise Exception("Input must be a string and the name of an element")
    try:
        get_short_atomic_info(a_float)
    except Exception:
        pass
    else:
        raise Exception("Input must be a string and the name of an element")
    try:
        get_short_atomic_info(falseelement)
    except Exception:
        pass
    else:
        raise Exception("Input must be element on the periodic table")
    return True
