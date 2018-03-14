from os.path import abspath, dirname, join

import pandas as pd


def file_path(filename):
    """
    Returns the absolute path of a file in the stored data set.
    """
    return abspath(join(dirname(__file__), "data",  "_data", filename))


def encode_columns(df, target_column):
    """Change unique column values to integers.  target_column will
    have values reassigned to integers inline. target_column needs to
    exsist within the feed df.

    Input: data frame to be modified and column to be modified
        e.g. 'preparative_route'
    No output, dataframe modified in function """
    assert isinstance(df, pd.DataFrame), "Function not provided a DataFrame."
    assert isinstance(df, pd.DataFrame), "Function not provided a DataFrame."
    targets = df[target_column].unique()
    map_to_int = {name: n for n, name in enumerate(targets)}
    df[target_column] = df[target_column].replace(map_to_int)

    return
