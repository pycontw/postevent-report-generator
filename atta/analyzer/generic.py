from atta.cleaner.title import cat_title

def apply_others(x):
    if x == '':
        return 'Others'


def add_cat_title(df):
    df['Title_Categories'] = df['Title'].apply(cat_title)
    others = df[df['Title_Categories'] == '']['Title_Categories'].apply(apply_others)
    df['Title_Categories'].update(others)
    return df