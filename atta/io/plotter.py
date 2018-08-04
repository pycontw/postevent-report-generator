import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl


new_fonts = ['AR PL UKai TW'] + mpl.rcParams['font.sans-serif']
mpl.rcParams['font.sans-serif'] = new_fonts
#mpl.rcParams.update({'font.size': 24})


def plot_counts(df, year):
    cols = df.keys().tolist()
    figs = {}
    for col in cols:
        figs.update(plot_count(df, col, year))

    return figs


def plot_count(df, col, year):
    """
    Core function to plot counts.

    If you want to change the count plots in the report, you would probably
    need to change this function.

    :param df: dataframe
    :param col: column
    :param year: year string
    :return: saved figure object
    """
    #sns.set(font=new_fonts)
    #sns.set_style({"font.sans-serif": new_fonts})
    # chnage seaborn font configuration will override matplotlib font conf
    # so the CJK fonts could not show correctly. Do not use sns until
    # I found a solution for it.
    #
    # ref: https://www.one-tab.com/page/DHKTSk5CQ1eRobxOZxWnjQ
    #
    #sns.set(font_scale=2)

    col_title = str(col)
    if col_title == 'Title_Categories':
        plot_x_description = 'Job Titles'
    else:
        plot_x_description = col_title

    # plot seaborn countplot on this fig
    fig, ax = plt.subplots(figsize=(12, 8))

    order = get_order(df, col)

    # let seaborn controls ax
    ax = sns.countplot(x=col_title, data=df, order=order)

    ax.set_title(plot_x_description + ' of the Attendees in ' + str(year))
    ax.set_xlabel(plot_x_description)
    ax.set_ylabel('Attendee Number')
    ax.set_xticklabels(order,
                      rotation=45,
                      fontdict={"fontsize": '16'})

    # Tweak spacing to prevent clipping of ylabel or xlabel
    fig.tight_layout()

    return save_fig(col_title)


def save_fig(identifier):
    fig_name = identifier + '.jpg'
    fig_path = '/tmp/' + fig_name
    plt.savefig(fig_path)

    return {identifier: fig_path}


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
