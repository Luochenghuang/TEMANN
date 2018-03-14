import re

import pandas as pd
import numpy as np
import pymatgen as mg
from pymatgen import MPRester

a = MPRester('9Mh5d6mP4sgSBzeE')


def get_atomic_info(element):
    """
    inputs an element (Str), returns a number of properties
    :return: list
    """

    assert element[0].isupper(),\
        "First letter must be capitalized, follow the periodic table"

    e = mg.Element(element)
    # list of attribute keywords
    keywords = ["mendeleev_no", "electrical_resistivity",
                "velocity_of_sound", "reflectivity",
                "refractive_index", "poissons_ratio", "molar_volume",
                "electronic_structure", "thermal_conductivity",
                "boiling_point", "melting_point",
                "critical_temperature", "superconduction_temperature",
                "liquid_range", "bulk_modulus", "youngs_modulus",
                "brinell_hardness", "rigidity_modulus",
                "mineral_hardness", "vickers_hardness",
                "density_of_solid", "atomic_radius_calculated",
                "van_der_waals_radius", "atomic_orbitals",
                "coefficient_of_linear_thermal_expansion"]

    properties = [getattr(e, x) for x in keywords]

    return properties


def get_short_atomic_info(element):
    """
    inputs an element (Str), returns a shorter number of
        properties than get_atomic_info
    :return: list
    """

    assert element[0].isupper(), \
        "First letter must be capitalized, follow the periodic table"

    e = mg.Element(element)
    # list of attribute keywords
    keywords = ["mendeleev_no", "electrical_resistivity",
                "velocity_of_sound",  # "reflectivity",
                # "refractive_index", "poissons_ratio", "molar_volume",
                # "electronic_structure",
                "thermal_conductivity",
                "boiling_point", "melting_point",
                # "critical_temperature",
                # "superconduction_temperature",
                # "liquid_range",
                "bulk_modulus", "youngs_modulus",
                "brinell_hardness", "rigidity_modulus",
                "mineral_hardness",  # "vickers_hardness",
                "density_of_solid", "atomic_radius_calculated",
                "van_der_waals_radius",  # "atomic_orbitals",
                "coefficient_of_linear_thermal_expansion"]

    properties = [getattr(e, x) for x in keywords]
    return properties


def compound_to_descriptors(compound):
    """This converts the dictionary of compounds to a list of all
    descriptors available (raveled)"""
    dict = get_empirical_formula(compound)
    list = []
    # populate list with stoichiometry
    for key, value in dict.items():
        list.extend([value] + get_atomic_info(key))
    # Ensure output length is right size, use dummy variable "H" to get length
    assert len(list) == len(get_atomic_info("H"))*len(dict)+len(dict),\
        "Output is wrong length"
    return list


def compound_short_descriptors(compound):
    """This converts the dictionary of compounds to a list of
    descriptors that are relevant for our ANN(raveled)
    This is a shorter version!"""

    # get_empirical_formula returns a dictionary with elements
    #     and corresponding stoichiometry
    dict = get_empirical_formula(compound)
    list = []
    # populate list with stoichiometry
    for key, value in dict.items():
        list.extend([value] + get_short_atomic_info(key))
    # Ensure output length is right size
    # use dummy variable, "H" to get length
    assert len(list) == len(get_short_atomic_info("H"))*len(dict)+len(dict),\
        "Output is wrong length"
    return list


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
        >>> from temann.utils import get_empirical_formula
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
