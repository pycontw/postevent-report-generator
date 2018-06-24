import click
import pkg_resources
import logging
import pandas as pd
import atta.config as attaconfig
import atta.analyzer.generic as ag
import atta.viewer.text as vtext
import atta.io.plotter as plotter
import atta.io.csv as attacsv


logger = logging.getLogger('atta')

resource_package = __name__
resource_path = '/'.join(('../data', 'default.ini'))

template = pkg_resources.resource_stream(resource_package, resource_path)


@click.command()
@click.option('--csv', default="data.csv",
              help='Read csv format data')
@click.option('--interactive/--no-interactive', default=False,
              help='Quiet mode. Useful for automation. True for no prompt.')
@click.option('--conf', help='Configuration file of how to analyze')
def main(csv, interactive, conf):
    conf_singlet = attaconfig.Configuration.get_instance()
    conf_singlet.read_configuration(template)
    if conf:
        logger.debug('User customized conf is specified: %s' % conf_singlet)
        conf_singlet.read_configuration(conf)

    df = attacsv.csv_to_dataframe(csv)

    # welcome user, ask year of data
    year = vtext.welcome_ask_year(interactive)
    # select necessary columns from df
    df = vtext.select_column(df, interactive)

    # everything is ready. let's call analyzer to do something
    df = ag.add_cat_title(df)

    # analyzed data frame is ready. let's plot
    plotter.plot_counts(df, year)

    print('Analysis process finished completely.')


if __name__ == '__main__':
    main()
