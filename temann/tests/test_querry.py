
from ..querry import *
from ..interpret import get_empirical_formula

def test_get_atomic_info():

    # Test element inputs
    test_form1 = "Ca"
    test_form2 = "La"
    test_form3 = "ga"
    # Try passing a number
    try:
        get_atomic_info(1234)
    except Exception:
        pass
    else:
        raise Exception("Bad input allowed",
                        "Error not raised when numerical value is passed")

    output_1 = get_atomic_info(test_form1)
    output_2 = get_atomic_info(test_form2)

    assert len(output_1) == 25, \
        "Wrong output length "+ str(len(output_1))

    assert len(output_2) == 25, \
        "Wrong output length"
    # Try non-capitalized element name
    try:
        get_atomic_info(test_form3)
    except Exception:
        pass
    else:
        raise Exception("Did not catch case of non-capitalized element")
    return True


def test_get_short_atomic_info():

    # Test non-string inputs and string that's not an element
    test1 = "H"
    a_integer = 2
    a_float = 2.5
    not_element = "ab"
    not_capitalize = "ga"
    # Ensure output is correct length
    results = get_short_atomic_info(test1)
    assert len(results) == 15, \
        "Wrong output length"
    # Try integer input
    try:
        get_short_atomic_info(a_integer)
    except Exception:
        pass
    else:
        raise Exception("Input must be a string and the name of an element")
    # Try float input
    try:
        get_short_atomic_info(a_float)
    except Exception:
        pass
    else:
        raise Exception("Input must be a string and the name of an element")
    # Try a non-element
    try:
        get_short_atomic_info(not_element)
    except Exception:
        pass
    else:
        raise Exception("Did not catch case of non-element input")
    # Try non-capitalized element
    try:
        get_short_atomic_info(not_capitalize)
    except Exception:
        pass
    else:
        raise Exception("Did not catch case of non-capitalized element")
    return True

def test_compound_to_descriptors():

    # make sure output is list
    test1 = compound_to_descriptors("Mn0.5B0.3C1.2")
    assert isinstance(test1, list),\
        "Output is not a list"

    # ensure descriptors for each element is obtained

    return True

def test_compound_short_descriptors():


    return True