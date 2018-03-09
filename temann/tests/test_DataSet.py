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

def test_clean_1():
#test to make sure all Unnamed columns are removed
    ds = DataSet()
    ds.data = pd.DataFrame({'A' : [1, 2, 3], 'Unnamed' : [4, 5, 6]})
    ds.clean()
    for col in ds.data.columns:
        if 'Unnamed' in col:
            raise Exception('Not clean',
                            'Unnamed column not cleaned out of DataFrame!')     

def test_clean_2():
#Check that all of the rows with NA or NaN values have been removed from the
#dataset. 
    ds = DataSet()
    ds.data = pd.DataFrame({'A' : [1, 2, 3], 'Unnamed' : ['NA', 5, 6]})
    ds.clean()
    for i in range(len(ds.data)):
        row = list(ds.data.iloc[i])
        if ('NaN' in row) or ('NA' in row):
            raise Exception('Not clean',
                            'Rows with NaN/NA values not cleaned out of DataFrame!')

def test_extrapolate_400K_1():
#Ensure that extrapolated dataset is longer than the original dataset.
    ds = DataSet()
    ds.data = pd.DataFrame({'Resist. (400K)' : [1, 2], 'Seebeck (400K)' : [1, 2], 
                            'Formula' : [1, 2], 'preparative route' : [1, 2],
                           'T (K)': [1, 2], 'Resist. (Ohm.cm)': [1, 2], 
                            'Seebeck (uV/K)': [1, 2]})
    result = ds.extrapolate_400K(['preparative route'])
    assert len(ds.data) < len(result), 'Rows not added, check df input!'
