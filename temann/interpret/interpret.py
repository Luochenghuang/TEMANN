import re


def get_empirical_formula(formula):
    """
    Parses a chemical formula into elements and proportions.

    Converts chemical formula to a dictionary containing elements
    and respective coefficients for doping and proportions.

    Args:
        formula (string): Chemical formula of a compound.

    Output:
        dictionary: Each key is a unique element in `formula` with the
            values being the element's associated proportion.

    Example:
        >>> from temann.interpret import get_empirical_formula
        >>> get_empirical_formula("Ca0.98La0.02MnO3")
        {'Ca': 0.98, 'La': 0.02, 'Mn': 1, 'O': 3}
    """
    assert not isinstance(formula, list), \
        "Cannot pass a list. Input must be a string"

    assert isinstance(formula, str), "Must pass a string."

    # Split formula into individual elements and their proportions
    proportions = re.findall("[A-Z][^A-Z]*", formula)

    elements = {}

    # Split each group into element and coefficient
    for pair in proportions:
        if bool(re.search(r"\d", pair)):
            split = re.match(r"([A-Z][a-z]*)([0-9]\.*[0-9]*)", pair)
            if bool(re.search(r"\.", split.group(2))):
                elements[split.group(1)] = float(split.group(2))
            else:
                elements[split.group(1)] = int(split.group(2))
        else:
            elements[pair] = 1

    return elements
