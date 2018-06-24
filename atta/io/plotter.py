import seaborn as sns
import matplotlib.pyplot as plt


def plot_counts(df, year):
    cols = df.keys().tolist()
    # change here to include more columns for count plots
    bar_cols = [cols[0], cols[1], cols[4]]
    for col in bar_cols:
        plot_count(df, col, year)


def plot_count(df, col, year):
    fig, ax = plt.subplots(figsize=(12, 8))
    plt.title(str(col)+' of the Attendees at PyCon Taiwan in ' + str(year))
    ax.set_xticklabels(str(col), rotation=0, fontdict={"fontsize": '8'})
    ax.set_xlabel(xlabel=str(col))
    ax.set_ylabel(ylabel="Counts")
    sns.set(font_scale=2)
    order = get_order(df, col)

    sns.countplot(x=str(col), data=df, order=order)
    plt.savefig(str(col) + str(year) + '.jpg')


def reorder(order, tag, col, chart_type='Title_Categories'):
    """
    Relocate the tag column to be the last bin of the order.

    :param order: iterable order.
    :param tag: string
    :param col: input column title
    :param chart_type: which chart you want to reorder
    :return: ordered order
    """
    if col == chart_type:
        order = list(order)
        others_index = order.index(tag)
        order.pop(others_index)
        order.append(tag)

    return order


def get_order(df, col):
    col_counts = df[col].value_counts()

    if col_counts.get('Others'):
        order = reorder(col_counts.index, 'Others', col)
    else:
        order = col_counts.index

    return order
