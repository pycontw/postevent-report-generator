import re

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


def get_sanity_data(df, cjk_support=False):
    if not cjk_support:
        # so matplotlib won't show warnings
        # issue #2
        # https://github.com/pycontw/pycontw-postevent-report-generator/
        # issues/2
        for df_col in df:
            for idx in range(len(df[df_col])):
                text = df[df_col][idx]

                # replace the specific cells
                # TODO: this stage should be completed at data sanity stage
                replace_dic = {
                    "1 年以內": "within 1 year",
                    "1 到 5 年": "1 - 5 years",
                    "5 到 10 年": "5 - 10 years",
                    "10 到 20 年": "10 - 20 years",
                    "China or HongKong or Macau 中國/香港/澳門": "China or HongKong or Macau",
                    "Singapore or Malaysia 新加坡/馬來西亞": "Singapore or Malaysia",
                }
                for key in replace_dic:
                    if key in text:
                        text = replace_dic[key]

                # strip non-ascii
                strip_cjk = re.sub(r"[^\x00-\x7f]", r"", text)

                df[df_col][idx] = strip_cjk

    return df
