import DataSet as ds
import numpy as np
import pandas as pd
from interpret import interpret
from querry import *
from sklearn.model_selection import train_test_split
import matplotlib.pylab as plt

# create a new DataSet object
dataset = ds.DataSet()
dataset.get_data('../data/TE_survey_csv_repaired.csv')

dataset.clean()
dataset.drop(['Authors', 'DOI', 'Comments', 'Comments.1', 'Author of Unit Cell','Unit Cell DOI'])

# use extrapolate_400K to extrapolate more row data
dataset_2 = ds.DataSet()
dataset_2.data = dataset.extrapolate_400K([])
dataset_2.get_info()

# make an array containing the atomic descriptors
array = [compound_short_descriptors(x) for x in dataset_2.df['Formula'].values]
ndf = pd.DataFrame.from_records(array)
ndf = ndf.fillna(0)
print(ndf) # looks good!

