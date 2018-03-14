def test_encode_columns_1():
    df = pd.DataFrame({'A': [1,2,3], 'B': ['a','b','c'], 'C': [4,5,6]})
    encode_columns(df, 'B')
    resultA = df["B"].iloc[0]
    resultB = df["B"].iloc[-1]
    assert isinstance(np.asscalar(resultA), int), "Target column not populated with integers."
    assert isinstance(np.asscalar(resultA), int), "Target column not populated with integers."
    return

def test_encode_columns_2():
    df = pd.DataFrame({'A': [1,2,3], 'B': ['a','b','c'], 'C': [4,5,6]})
    target_column = 'B'
    try:
        encode_columns(df, target_column)
    except(Exception):
        raise Exception ("Bad input allowed",
                        "Error not raised when input is not a list")
    else:
        pass
    return

