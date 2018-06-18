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
    sns.countplot(x = str(col), data = df)
    # directory = Tk.tk() # Something about
    plt.savefig(str(col) + str(year) + '.jpg')
