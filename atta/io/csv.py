import logging
import pandas as pd


def csv_to_dataframe(csv):
    # read csv as pandas dataframe
    df = pd.read_csv(csv)
    # Print the keys as bug messages
    logging.debug(df.keys())

    return df
