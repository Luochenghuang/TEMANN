import DataSet as ds
import numpy as np
import pandas as pd


# create a new DataSet object
dataset = ds.DataSet()
dataset.getData('../data/TE_survey_csv_repaired.csv')

dataset.clean()
dataset.drop(['Authors', 'DOI', 'Comments', 'Comments.1', 'Author of Unit Cell','Unit Cell DOI'])

# use extrapolate_400K to extrapolate more row data
dataset_2 = ds.DataSet()
dataset_2.data = dataset.extrapolate_400K(['preparative route','average atomic volume'])
print(dataset_2.df)
dataset_2.getInfo()
# test write to csv, you can find the new_ds.csv under data directory.
dataset_2.export_to('../data/new_ds')