from os.path import abspath, dirname, join


def file_path(filename):
    """
    Returns the absolute path of a file in the stored data set.
    """
    return abspath(join(dirname(__file__), "..", "data",  "_data", filename))
