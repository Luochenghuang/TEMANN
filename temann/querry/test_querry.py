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
    except(Exception):
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

    return


test_get_atomic_info()