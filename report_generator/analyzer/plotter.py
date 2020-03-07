import logging
import re

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

import report_generator.analyzer.generic as ag

format_str = "[ %(funcName)s() ] %(message)s"
logging.basicConfig(level=logging.INFO, format=format_str)


def plot_attendee_counts(df, year, cjk_support=False):
    cols = df.keys().tolist()
    figs = {}
    for col in cols:
        figs.update(plot_attendee_count(df, col, year, cjk_support))

    return figs


def plot_attendee_count(df, col, year, cjk_support=False):
    """
    Core function to plot counts.

    If you want to change the count plots in the report, you would probably
    need to change this function.

    :param df: dataframe
    :param col: column
    :param year: year string
    :param cjk_support: if enable CJK font support in the report
    :return: saved figure object
    """
    if cjk_support:
        logging.debug("CJK support is enabled.")
        # ref: https://www.one-tab.com/page/DHKTSk5CQ1eRobxOZxWnjQ
        # to support CJK fonts
        sns.set(font_scale=2)
        new_fonts = ["AR PL UKai TW"] + mpl.rcParams["font.sans-serif"]
        mpl.rcParams["font.sans-serif"] = new_fonts
    else:
        logging.debug("CJK support is disabled")

    logging.debug("Mapping column and description")
    col_title = col
    if col_title == "Title_Categories":
        plot_x_description = "Job Titles"
    elif col_title == "Interested_Field":
        df = ag.extract_interesting_field(df)
        plot_x_description = "Interested Fields"
    else:
        plot_x_description = col_title

    # plot seaborn countplot on this fig
    fig, ax = plt.subplots(figsize=(12, 8))

    order = get_order(df, col)

    logging.debug("Plotting...")
    # let seaborn controls ax
    ax = sns.countplot(x=col_title, data=df, order=order)

    ax.set_title(plot_x_description + " of the Attendees in " + str(year))
    ax.set_xlabel(plot_x_description)
    ax.set_ylabel("Attendee Number")
    ax.set_xticklabels(order, rotation=90, fontdict={"fontsize": "16"})

    logging.debug("Fine tune for too small fields")
    if col_title != "Interesting_Field":
        # Add count value for fileds which counts are too small
        col_value_counts = df[col_title].value_counts()
        for idx, _ in enumerate(order):
            count_on_y = col_value_counts[order[idx]]
            ax.text(idx, count_on_y, count_on_y)

    logging.debug("Tweak spacing")
    # Tweak spacing to prevent clipping of ylabel or xlabel
    fig.tight_layout()

    logging.debug("Saving figures...")
    return save_fig(col_title)


def plot_talk_categories(df, fig_title="Topics"):

    # Change category column to readables
    df["category"] = df["category"].map(
        {
            "PRAC": "Best Practices & Patterns",
            "COM": "Community",
            "DB": "Databases",
            "DATA": "Data Analysis",
            "EDU": "Education",
            "EMBED": "Embedded Systems",
            "FIN": "FinTech",
            "GAME": "Gaming",
            "GRAPH": "Graphics",
            "OTHER": "Other",
            "CORE": "Python Core (language, stdlib, etc.)",
            "INTNL": "Python Internals",
            "IOT": "Internet Of Things",
            "LIBS": "Python Libraries",
            "SCI": "Science",
            "SEC": "Security",
            "ADMIN": "Systems Administration",
            "TEST": "Testing",
            "WEB": "Web Frameworks",
        }
    )

    fig, ax = plt.subplots(figsize=(12, 8))

    logging.debug("Plotting...")

    counts_by_category = df["category"].value_counts()

    wedges, _, autotexts = plt.pie(
        counts_by_category,
        # Calculate the percentage back to actual number of talks
        autopct=lambda x: int(round((x / 100) * counts_by_category.sum())),
        pctdistance=0.8,
        # There's too much categories, joining two color palettes to avoid repeating
        colors=sns.color_palette("muted") + sns.color_palette(),
    )

    # Following snippet copied from
    # https://matplotlib.org/3.1.0/gallery/pie_and_polar_charts/pie_and_donut_labels.html
    bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
    kw = dict(arrowprops=dict(arrowstyle="-"), bbox=bbox_props, zorder=0, va="center")

    for i, p in enumerate(wedges):
        ang = (p.theta2 - p.theta1) / 2.0 + p.theta1
        y = np.sin(np.deg2rad(ang))
        x = np.cos(np.deg2rad(ang))
        horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
        connectionstyle = "angle,angleA=0,angleB={}".format(ang)
        kw["arrowprops"].update({"connectionstyle": connectionstyle})
        ax.annotate(
            counts_by_category.index[i],
            xy=(x, y),
            xytext=(np.sign(x) + 0.4 * x, 1.4 * y),
            horizontalalignment=horizontalalignment,
            **kw
        )

    # Setting font styles for talk counts
    for text in autotexts:
        text.set_color("white")
        text.set_fontsize(14)

    ax.set_title("Count of Talks by Topics")
    return save_fig(fig_title)


def plot_booth(df, col):
    print(df[col].value_counts())


def save_fig(identifier):
    fig_name = identifier + ".jpg"
    fig_path = "/tmp/" + fig_name
    plt.savefig(fig_path)

    return {identifier: fig_path}


def reorder(order, tag, reverse=False):
    """
    Relocate the tag column to be the last bin of the order.

    :param order: iterable order.
    :param tag: string
    :param reverse: True to put it at the beginning, false to be the last
    :return: ordered order
    """
    order = list(order)
    others_index = order.index(tag)
    order.pop(others_index)
    if reverse:
        order = [tag] + order
    else:
        order.append(tag)

    return order


def get_reorder_by(df, col, pattern, order=None, reverse=False):
    col_counts = df[col].value_counts()

    if order is None:
        order = col_counts.index

    for col_title in col_counts.keys():
        if re.search(pattern, col_title) is not None:
            order = reorder(order, col_title, reverse)

    return order


def get_order(df, col):
    """
    Get order of x tick labels

    If there are others-like and no-record-like in the meantime, no-record-like
    will be the last one.

    If there is seniority within 1 year, it will be the 1st.

    :param df: dataframe
    :param col: col
    :return: iterable
    """
    col_counts = df[col].value_counts()
    order = col_counts.index

    pattern = "年以內"
    order = get_reorder_by(df, col, pattern, order, reverse=True)

    pattern = "Other|other"
    order = get_reorder_by(df, col, pattern, order)

    pattern = "No Record"
    order = get_reorder_by(df, col, pattern, order)

    return order
