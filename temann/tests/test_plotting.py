# Unit test for plotting.py
from ..plotting import three_elements_to_formula

def test_three_elements_to_formula():
    el1 = 1
    el2 = 'Mn'
    el3 = 'Sr'
    st1 = 2
    st2 = 3
    st3 = 1
    try:
        three_elements_to_formula(el1, el2, el3, st1, st2, st3)
    except Exception:
        pass
    else:
        raise Exception('Did not catch case of non-string input for element')

    el1 = 'Ca'
    results = three_elements_to_formula(el1, el2, el3, st1, st2, st3)
    assert results == 'Ca2Mn3Sr1'
    return True
