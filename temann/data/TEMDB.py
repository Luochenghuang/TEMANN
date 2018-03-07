import pandas as pd

from ..util.load_data import file_path


TEMDB = pd.read_csv(file_path('TEMDB.csv'))
