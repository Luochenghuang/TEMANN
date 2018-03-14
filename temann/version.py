from __future__ import absolute_import, division, print_function
from os.path import join as pjoin

# Format expected by setup.py and doc/source/conf.py: string of form "X.Y.Z"
_version_major = 0
_version_minor = 1
_version_micro = ''  # use '' for first of series, number for 1 and above
_version_extra = 'dev'
# _version_extra = ''  # Uncomment this for full releases

# Construct full version string from these.
_ver = [_version_major, _version_minor]
if _version_micro:
    _ver.append(_version_micro)
if _version_extra:
    _ver.append(_version_extra)

__version__ = '.'.join(map(str, _ver))

CLASSIFIERS = ["Development Status :: 3 - Alpha",
               "Environment :: Console",
               "Intended Audience :: Science/Research",
               "License :: OSI Approved :: MIT License",
               "Operating System :: OS Independent",
               "Programming Language :: Python",
               "Topic :: Scientific/Engineering"]

# Description should be a one-liner:
description = "temann: package for predicting Seebeck coefficients"
# Long description will go up on the pypi page
long_description = """

TEMANN
======
TEMANN is a python module that allows users to predict Seebeck
coefficients for novel materials. Inside TEMANN there is an artificial
neural network that was trained on a data set of thermoelectric
materials. In addition to material descriptors, TEMANN also interfaces
with the Materials Project via the pymatgen python package.

All a user needs to do is provide the chemical formula of the material
of interest, it's space group number, and the temperature (K) of
interest. The output will be a predicted Seebeck coefficient for that
material in the units of uV/K.

License
=======
``temann`` is licensed under the terms of the MIT license. See the file
"LICENSE" for information on the history of this software, terms & conditions
for usage, and a DISCLAIMER OF ALL WARRANTIES.

All trademarks referenced herein are property of their respective holders.

Copyright (c) 2018--, Luke Gibson, Luocheng Huang, Nathan Laurie, &
Ellen Murphy, The University of Washington.
"""

NAME = "temann"
MAINTAINER = "Luke Gibson"
MAINTAINER_EMAIL = "ldgibson@uw.edu"
DESCRIPTION = description
LONG_DESCRIPTION = long_description
URL = "https://github.com/Luochenghuang/TEMANN"
DOWNLOAD_URL = ""
LICENSE = "MIT"
AUTHOR = "Luke Gibson <ldgibson@uw.edu>, " +\
         "Luocheng Huang <luochenghuang@gmail.com>, " +\
         "Nathan Laurie <natelaur@uw.edu>, " + \
         "Ellen Murphy <murphy89@uw.edu>"
AUTHOR_EMAIL = ""
PLATFORMS = "OS Independent"
MAJOR = _version_major
MINOR = _version_minor
MICRO = _version_micro
VERSION = __version__
PACKAGE_DATA = {'temann': [pjoin('data', '_data', '*')],
                '': ['*.csv']}
REQUIRES = ["numpy", "pandas", "ase", "pymatgen"]
