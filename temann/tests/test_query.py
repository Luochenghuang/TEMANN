from ..query import *


def test_get_atomic_info():

    # Test element inputs
    test_form1 = "Ca"
    test_form2 = "La"
    test_form3 = "ga"
    not_element = "Az"
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
        "Wrong output length " + str(len(output_1))

    assert len(output_2) == 25, \
        "Wrong output length"
    # Try non-capitalized element name
    try:
        get_atomic_info(test_form3)
    except Exception:
        pass
    else:
        raise Exception("Did not catch case of non-capitalized element")
    try:
        get_short_atomic_info(not_element)
    except Exception:
        pass
    else:
        raise Exception("Did not catch case of non-element input")
    return True


def test_get_short_atomic_info():

    # Test non-string inputs and string that's not an element
    test1 = "H"
    a_integer = 2
    a_float = 2.5
    not_element = "Az"
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
    # output should be 25 descriptors * number of
    #     elements + number of elements
    assert len(test1) == 78,\
        "Wrong output length"
    # ensure descriptors for each element is obtained

    return True


def test_compound_short_descriptors():

    # make sure output is list
    test1 = compound_short_descriptors("Mn0.5B0.3C1.2")
    assert isinstance(test1, list),\
        "Output is not a list"
    # output should be 15 descriptors * number of
    #     elements + number of elements
    assert len(test1) == 48,\
        "Wrong output length"
    # ensure descriptors for each element is obtained

    return True


def test_get_empirical_formula():

    # Test formula inputs
    test_form1 = "Ca0.98La0.02MnO3"
    test_form2 = "LiO"

    # Try passing a number
    try:
        get_empirical_formula(1234)
    except(Exception):
        pass
    else:
        raise Exception("Bad input allowed",
                        "Error not raised when numerical value is passed")

    # Check output of valid run
    elements1 = get_empirical_formula(test_form1)

    assert set(['Ca', 'La', 'Mn', 'O']).issubset(elements1.keys()), \
        "Incorrect list of elements in formula"

    assert set([0.98, 0.02, 1, 3]).issubset(elements1.values()), \
        "Incorrect list of coefficients in formula"

    assert type(elements1['Ca']) is float, "Proportion value not a float"
    assert type(elements1['Mn']) is int, "Proportion value not an int"
    assert type(elements1['O']) is int, "Proportion value not an int"

    # Check output of valid run with no doping percentages
    elements2 = get_empirical_formula(test_form2)

    assert set(['Li', 'O']).issubset(elements2.keys()), \
        "Incorrect list of elements in formula"

    assert set([1, 1]).issubset(elements2.values()), \
        "Incorrect list of coefficients in formula"

    return
