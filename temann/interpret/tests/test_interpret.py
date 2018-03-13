from ..interpret import *


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
