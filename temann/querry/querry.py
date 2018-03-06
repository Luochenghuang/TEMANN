import pandas as pd
import numpy as np
import pymatgen as mg
from pymatgen import MPRester

a = MPRester('9Mh5d6mP4sgSBzeE')

def get_atomic_info(element):
    '''
    inputes an element (Str), returns the properties
    :return: list
    '''

    e = mg.Element(element)
    properties = [e.atomic_mass]

    return properties

