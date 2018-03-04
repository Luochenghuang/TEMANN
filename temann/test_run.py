import DataSet as ds
import numpy as np
import pandas as pd
from interpret import interpret
from sklearn.model_selection import train_test_split
import matplotlib.pylab as plt

# create a new DataSet object
dataset = ds.DataSet()
dataset.getData('../data/TE_survey_csv_repaired.csv')

dataset.clean()
dataset.drop(['Authors', 'DOI', 'Comments', 'Comments.1', 'Author of Unit Cell','Unit Cell DOI'])

# use extrapolate_400K to extrapolate more row data
dataset_2 = ds.DataSet()
dataset_2.data = dataset.extrapolate_400K([])


# # test write to csv, you can find the new_ds.csv under data directory.
# dataset_2.export_to('../data/new_ds')

#make a little graph
# plt.scatter(dataset_2.df['Resist'], dataset_2.df['Seebeck'])
# plt.show()

dataset_2.df['Pretty'] = None
dataset_3 = pd.Series()

for index, row in dataset_2.df.iterrows():
    dataset_2.df['Pretty'][index] = interpret.get_empirical_formula(dataset_2.df['Formula'][index])

print(dataset_2.df)

train, test = train_test_split(dataset_2.df, test_size=0.2)
print(test)
print(train)