import pandas as pd


def excel_to_dataframe(excel_file):
    # read  all excel sheets as pandas dataframe
    df_excel = pd.read_excel(excel_file, sheet_name=None)
    return df_excel
