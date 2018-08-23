import pandas as pd


def give_numbers_to_categories(dataframe: pd.DataFrame, headers=[]):
    if not headers:
        headers = list(dataframe)
    for head in headers:
        unique_values = dataframe[head].unique()
        dict_values = {k: v for v, k in enumerate(unique_values)}
        dataframe[head] = dataframe[head].map(dict_values)

    return dataframe