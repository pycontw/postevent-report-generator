import logging
import pkg_resources

import click
import pandas as pd

import atta.config as attaconfig
import atta.analyzer.generic as ag
import atta.viewer.text as vtext
import atta.io.plotter as plotter
import atta.io.csv as attacsv
import atta.io.yaml as attayaml
import atta.ticket.attendee as attendee
import atta.exporter.html as exporter_html
from atta.partner import sponsor as apsponsor


logger = logging.getLogger("atta")

resource_package = __name__
resource_path = "/".join(("../data", "default.ini"))

template = pkg_resources.resource_stream(resource_package, resource_path)


@click.command()
@click.option("--csv", required=True, default="data.csv", multiple=True, help="Read csv format data")
@click.option(
    "--interactive/--no-interactive", default=False, help="Quiet mode. Useful for automation. True for no prompt."
)
@click.option("--conf", help="Configuration file of how to analyze")
@click.option("--yaml", required=True, help="Report yaml file to describe how a report would be")
@click.option("--package-yaml", required=True, help="Package yaml file to describe how a package is defined")
@click.option("--sponsor-yaml", required=True, help="Sponsor yaml file to describe how a sponsor is defined")
def main(csv, interactive, conf, yaml, package_yaml, sponsor_yaml):
    conf_singlet = attaconfig.Configuration.get_instance()
    conf_singlet.read_configuration(template)
    if conf:
        logger.debug("User customized conf is specified: %s" % conf_singlet)
        conf_singlet.read_configuration(conf)

    # welcome user, ask year of data
    year = vtext.welcome_ask_year(interactive)

    frames = []
    for csv_single in csv:
        csv_index = csv.index(csv_single)

        df = attacsv.csv_to_dataframe(csv_single)

        # select necessary columns from df
        df = vtext.select_column(df, interactive, csv_index)

        frames.append(df)

    df_all = pd.concat(frames, join="outer", axis=0)

    # everything is ready. let's call analyzer to do something
    df_all = ag.add_cat_title(df_all)
    df_all = df_all.fillna(value="No Record")

    # all datafram general data object
    df_all_g_data_obj = attendee.Attendee(df_all)

    # analyzed data frame is ready. let's plot
    figs = plotter.plot_counts(df_all, year)

    # read the other report data
    report_yaml = attayaml.read_yaml(yaml)

    sponsors = apsponsor.get_all_sponsors(package_yaml, sponsor_yaml)

    # generate the report
    # general info (everyone could see it):
    #   figs: plots from attendee dataframe
    #   df_all_g_data_obj: numbers from attendee dataframe
    #   report_yaml: plot description of figs
    # sponsors:
    #   sponsor specific information based on yaml descriptor
    exporter_html.generate(figs, report_yaml, df_all_g_data_obj, sponsors)

    print("Analysis process finished completely.")


if __name__ == "__main__":
    main()
