import logging

import pandas as pd


def csv_to_dataframe(csv_single):
    # read csv as pandas dataframe
    df_single = pd.read_csv(csv_single)
    # Print the keys as bug messages
    logging.debug(df_single.keys())

    return df_single
