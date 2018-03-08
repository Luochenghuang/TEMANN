import sys
from os.path import abspath, dirname, join
from io import StringIO

from ..DataSet import *

test_path = abspath(join(dirname(__file__), 'test_data.csv'))

testclass = DataSet()
testclass.get_data(test_path)


def test_get_info():
    output = StringIO()
    # capture all stdout in `output` via redirection
    sys.stdout = output

    # call the class method
    testclass.get_info()
    # reset redirection
    sys.stdout = sys.__stdout__

    # split the output into lines
    lines = output.getvalue().splitlines()

    # make sure there are 3 rows and 3 columns
    assert lines[0] == '3 rows and 3 columns.',\
        'Incorrect number of rows and columns.'
    # check the column headers
    assert lines[2] == 'x,  y,  z',\
        'Incorrect column headers.'
    return
