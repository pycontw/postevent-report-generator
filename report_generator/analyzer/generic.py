import pandas as pd

from report_generator.cleaner.title import cat_title


def apply_others(x):
    if x == "":
        return "Others"


def add_cat_title(df):
    df["Title_Categories"] = df["Title"].apply(cat_title)
    others = df[df["Title_Categories"] == ""]["Title_Categories"].apply(apply_others)
    df["Title_Categories"].update(others)
    return df


def extract_interesting_field(df):
    col_data = df["Interested_Field"]
    fields = []
    for col in col_data:
        if isinstance(col, str):
            fields = fields + col.split(",")

    fields_strip = []
    for ele in fields:
        fields_strip.append(ele.strip())

    new_df = pd.DataFrame.from_dict({"Interested_Field": fields_strip})

    return new_df
