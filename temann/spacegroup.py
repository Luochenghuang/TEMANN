# build database of spacegroups
# draw key information from spacegroup information
import pandas as pd
import numpy as np
import spglib
import ase.spacegroup
from ase.spacegroup import Spacegroup

# number of spacegroups
num = 230
sg = list(range(1, num+1))
# build empy dataframe
df = pd.DataFrame(data=np.zeros((len(sg), 5)),
                  columns=['spacegroup', 'crystal system', 'lattice type',
                           'centrosymmetric', 'symmetry operations'])

# make column of spacegroup numbers
df['spacegroup'] = sg
# parse crystal system of spacegroups
df['crystal system'] = 'cubic'
df.loc[range(0, 2), 'crystal system'] = 'triclinic'
df.loc[range(2, 15), 'crystal system'] = 'monoclinic'
df.loc[range(15, 74), 'crystal system'] = 'orthorhombic'
df.loc[range(74, 142), 'crystal system'] = 'tetragonal'
df.loc[range(142, 167), 'crystal system'] = 'hexagonal'

# use Spacegroup class to iterate through and populate columns
for i in range(len(df)):
    # populate lattice type from looping through Spacegroup class
    lattice = Spacegroup(i+1).symbol[0]
    df.iloc[i, 2] = lattice
    # whether centrosymmetric for each spacegroup
    centro = Spacegroup(i+1).centrosymmetric
    df.iloc[i, 3] = centro
    # make spacegroup info into list of strings
    strings = str(Spacegroup(i+1))
    # find index for string marking number we want
    idx = strings.find(' symmetry')
    num1 = strings[idx-2]
    num2 = strings[idx-1]
    symmetry = int(num1+num2)
    df.iloc[i, 4] = symmetry
    # DO NOT ADD REST OF HERMANN-MAUGUIN INFORMATION AT THIS TIME
    # NO GOOD WAY TO USE IT


def expand_spacegroup(sg):
    """Input a spacegroup number and this function returns various
    symmetry related descriptors for the material"""
    sg_info = df.loc[sg-1, :]
    return sg_info
