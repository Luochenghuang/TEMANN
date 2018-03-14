# Unit test for plotting.py
from ..plotting import three_elements_to_formula
from ..plotting import generate_heatmap_data
from ..plotting import plot_ternary


def test_three_elements_to_formula():
    el1 = 'Ca'
    el2 = 'Mn'
    el3 = 'Sr'
    st1 = 2
    st2 = 3
    st3 = 1
    non_elem = 3
    non_st = 'Mn'
    # Try case of integer for element input
    try:
        three_elements_to_formula(non_elem, el2, el3, st1, st2, st3)
    except Exception:
        pass
    else:
        raise Exception('Did not catch case of non-string input for element')
    # Try case of string input for stoichiometry
    try:
        three_elements_to_formula(el1, el2, el3, non_st, st2, st3)
    except Exception:
        pass
    else:
        raise Exception('Did not catch case of string input for stoichiometry')

    # Make sure output is correct value
    results = three_elements_to_formula(el1, el2, el3, st1, st2, st3)
    assert results == 'Ca2Mn3Sr1'

    return True


def test_generate_heatmap_data():
    el1 = 'Ca'
    el2 = 'Mn'
    el3 = 'Sr'
    sg = 35
    non_sg = 231
    T = 40
    scale = 10
    non_T = -49
    non_scale = -4
    # invalid space group
    try:
        generate_heatmap_data(el1, el2, el3, non_sg, T, scale)
    except Exception:
        pass
    else:
        raise Exception('Did not catch case of invalid spacegroup')
    # Try case of invalid temperature input
    try:
        generate_heatmap_data(el1, el2, el3, sg, non_T, scale)
    except Exception:
        pass
    else:
        raise Exception('Did not catch case of invalid temperature')
    # Try case of invalid scale input
    try:
        generate_heatmap_data(el1, el2, el3, sg, T, non_scale)
    except Exception:
        pass
    else:
        raise Exception('Did not catch case of invalid scale')

    return True


def test_plot_ternary():

    noncap_elements = 'Gaasc'
    toomany_elements = 'GasAsCB'
    sg = 49
    # Try invalid elements input
    try:
        plot_ternary(noncap_elements, sg)
    except Exception:
        pass
    else:
        raise Exception('Did not catch case of non-capitalized elements')
    # Try case of invalid temperature input
    try:
        plot_ternary(toomany_elements, sg)
    except Exception:
        pass
    else:
        raise Exception('Did not catch case of too many capital letters')

    return True
