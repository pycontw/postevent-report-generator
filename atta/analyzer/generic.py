from atta.cleaner.title import cat_title


def add_cat_title(df):
    df['Title_Categories'] = df['Title'].apply(cat_title)
    return df

