import pandas as pd


def melt_cols(df, col_names):
    """
    :param df: DataFrame to meld
    :param col_names: names of columns to meld
    :return: DataFrame with columns: (a) index values of original df w. index name
    (b) col_names, categorial, vals values from cols
    """
    id_val = 'index' if df.index.name is None else df.index.name
    return df[col_names].reset_index().melt(id_vars=id_val, var_name='col_names', value_name='vals')
