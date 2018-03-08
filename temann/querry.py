import pandas as pd
import numpy as np
import pymatgen as mg
from .interpret import get_empirical_formula
from pymatgen import MPRester

a = MPRester('9Mh5d6mP4sgSBzeE')

def get_atomic_info(element):
    """
    inputes an element (Str), returns the properties
    :return: list
    """

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
    inputs an element (Str), returns the properties
    :return: list
    """

    e = mg.Element(element)
    # list of attribute keywords
    keywords = ["mendeleev_no", "electrical_resistivity",
                "velocity_of_sound", # "reflectivity",
                #"refractive_index", "poissons_ratio", "molar_volume",
                #"electronic_structure",
                "thermal_conductivity",
                "boiling_point", "melting_point",
                #"critical_temperature",
                # "superconduction_temperature",
                #"liquid_range",
                "bulk_modulus", "youngs_modulus",
                "brinell_hardness", "rigidity_modulus",
                "mineral_hardness", # "vickers_hardness",
                "density_of_solid", "atomic_radius_calculated",
                "van_der_waals_radius", # "atomic_orbitals",
                "coefficient_of_linear_thermal_expansion"]

    properties = [getattr(e, x) for x in keywords]
    return properties


def compound_to_descriptors(compound):
    """This converts the dictionary of compounds to a list of desciptors (raveled)"""
    dict = get_empirical_formula(compound)
    list = []
    for key, value in dict.items():
        list.extend([value] + get_atomic_info(key))

    return list


def compound_short_descriptors(compound):
    """This converts the dictionary of compounds to a list of desciptors (raveled)
    This is a shorter version!"""
    dict = get_empirical_formula(compound)
    list = []
    for key, value in dict.items():
        list.extend([value] + get_short_atomic_info(key))

    return list
