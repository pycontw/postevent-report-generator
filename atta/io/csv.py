import logging
import pandas as pd


def csv_to_dataframe(csv):
    frames = []
    for csv_single in csv:
        # read csv as pandas dataframe
        df = pd.read_csv(csv_single)
        # Print the keys as bug messages
        logging.debug(df.keys())
        frames.append(df)

    return pd.concat(frames, join='outer', axis=0)
