import numpy as np
import pandas as pd
from pandas import DataFrame as df
import textwrap

# to prevent SettingWithCopyWarning;
pd.options.mode.chained_assignment = None  # default='warn'


class DataSet:
    """
    DataSet stores pandas data.
    """

    # initiate
    def __init__(self):
        self.data = df
        pass

    # read_csv
    def get_data(self, path):
        """
        reads data from path
        :param path
        :path (or url)
        :return:
        """
        self.data = pd.read_csv(path)

    def get_info(self):

        """
        gets shape and columns
        :return:
        """
        # shape
        print('{} rows and {} columns.'.format(self.data.shape[0],
              self.data.shape[1]))
        # components
        strs = ', '.join(list(self.data.columns.values))
        print('Components are: ')
        print(textwrap.fill(strs, 70))

    def clean(self):
        """
        static method that get rid of unnamed columns
        :return:
        """
        # get rid of 'Unnamed' columns and empty rows
        for col in self.data.columns:
            if 'Unnamed' in col:
                del self.data[col]

        self.data = self.data.dropna(axis=0, how='all')

    def drop(self, components):
        """
        drop a list of components
        :param components: list[component1, component2...]
        :return:
        """
        self.data = self.data.drop(components, axis=1)

    def extrapolate_400K(self, components):
        """
        input a list! For instance: ['preparative route']
        For every row that has 400K properties, create a new row with
        properties and add to the data
        :input: list of components of interest
        :return: static method
        """

        # components including TE properties at 400K
        component_list = ['Resist. (400K)', 'Seebeck (400K)', 'Formula']\
            + components

        # make a new DataFrame from the list
        new_df = self.data[component_list]
        new_df['T'] = 400
        # drop all the NaN rows
        new_df = new_df[np.isfinite(new_df['Resist. (400K)'])]
        component_list = ['Resist', 'Seebeck', 'Formula']\
            + components + ['T (K)']
        new_df.columns = component_list

        # now make a df from the current self.data
        old_component_list = ['T (K)', 'Resist. (Ohm.cm)', 'Seebeck (uV/K)',
                              'Formula'] + components
        old_df = self.data[old_component_list]
        old_component_list = ['T (K)', 'Resist', 'Seebeck', 'Formula']\
            + components
        old_df.columns = old_component_list  # change column names

        final_df = pd.concat([old_df, new_df], ignore_index=True)

        # delete duplicates
        final_df.drop_duplicates(keep=False)

        return final_df

    def export_to(self, name):
        self.df.to_csv(name + '.csv', index=False)

    def split(self, percentage):
        """
        this function splits the DataSet into two dataframes:
        test set and training set
        :param percentage: the percentage data for testing
        :return: tuple (test_set, training set)
        """
        msk = np.random.rand(len(self.df))
        train = self.df[msk]
        test = self.df[~msk]
        return (test, train)

    @property
    def df(self):
        """
        returns the internal DataFrame
        :return: DataFrame
        """
        return self.data


# create a new DataSet object
# ds = DataSet()
# ds.get_data('../data/TE_survey_csv_repaired.csv')
# ds.clean()
# ds.get_info()
#

# ds.drop(['Authors', 'DOI', 'Comments', 'Comments.1',
#          'Author of Unit Cell','Unit Cell DOI'])

# # use extrapolate_400K to extrapolate more row data
# new_ds = DataSet()
# new_ds.data = ds.extrapolate_400K(['preparative route'])
# print(new_ds.df)
# new_ds.getInfo()
# # test write to csv, you can find the new_ds.csv under data directory.
# new_ds.export_to('../data/new_ds')
