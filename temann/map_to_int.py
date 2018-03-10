def encode_columns(df, target_column):
    """Change unique column values to integers.  df_mod2 needs to be """
    targets = df[target_column].unique()
    map_to_int = {name: n for n, name in enumerate(targets)}
    df[target_column] = df[target_column].replace(map_to_int)
    
    return
