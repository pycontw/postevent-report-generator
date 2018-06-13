import click
import logging
import pandas as pd
import atta.analyzer.generic as ag
import atta.viewer.text as vtext
import atta.io.plotter as plotter


@click.command()
@click.option('--csv', default="data.csv", help='read csv format data')
def main(csv):
    # read csv as pandas dataframe
    df = pd.read_csv(csv)
    # Print the keys as bug messages
    logging.debug(df.keys())

    # welcome user, ask year of data
    year = vtext.welcome_ask_year()
    # select necessary columns from df
    df = vtext.select_column(df)
    df = ag.add_cat_title(df)

    # everything is ready. let's call analyzer to do something
    df = ag.add_cat_title(df)

    # analyzed data frame is ready. let's plot
    plotter.plot_counts(df, year)

    print('Analysis process finished completely.')


if __name__ == '__main__':
    main()
