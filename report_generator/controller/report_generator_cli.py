import logging

import click
import pandas as pd
import pkg_resources

import report_generator.analyzer.generic as ag
import report_generator.analyzer.plotter as plotter
import report_generator.config as report_generatorconfig
import report_generator.exporter.html as exporter_html
import report_generator.io.csv as report_generatorcsv
import report_generator.io.yaml as report_generatoryaml
import report_generator.ticket.attendee as attendee
import report_generator.viewer.text as vtext
from report_generator.partner import sponsor as apsponsor

logger = logging.getLogger("report_generator")

resource_package = __name__
resource_path = "/".join(("../data", "default.ini"))

template = pkg_resources.resource_stream(resource_package, resource_path)


@click.command()
@click.option(
    "--csv",
    required=True,
    default="data.csv",
    multiple=True,
    help="Read csv format data",
)
@click.option(
    "--talks-csv", required=True, default="talks.csv", help="CSV file for talks"
)
@click.option(
    "--proposed-talks-csv",
    required=True,
    default="talks.csv",
    help="CSV file for proposed talks",
)
@click.option(
    "--booth-csv",
    required=True,
    default="booth.csv",
    help="CSV file for booth checking",
)
@click.option(
    "--interactive/--no-interactive",
    default=False,
    show_default=True,
    help="Quiet mode. Useful for automation. True for no prompt.",
)
@click.option(
    "--cjk-support/--no-cjk-support",
    default=False,
    show_default=True,
    help="Enable CJK support in the plot or not.",
)
@click.option("--conf", help="Configuration file of how to analyze")
@click.option(
    "--yaml", required=True, help="Report yaml file to describe how a report would be"
)
@click.option(
    "--package-yaml",
    required=True,
    help="Package yaml file to describe how a package is defined",
)
@click.option(
    "--sponsor-yaml",
    required=True,
    help="Sponsor yaml file to describe how a sponsor is defined",
)
@click.option(
    "--output-path",
    help="Where the reports exported",
    default="/tmp",
    show_default=True,
)
def main(
    csv,
    talks_csv,
    proposed_talks_csv,
    booth_csv,
    interactive,
    cjk_support,
    conf,
    yaml,
    package_yaml,
    sponsor_yaml,
    output_path,
):
    conf_singlet = report_generatorconfig.Configuration.get_instance()
    conf_singlet.read_configuration(template)
    if conf:
        logger.debug("User customized conf is specified: %s" % conf_singlet)
        conf_singlet.read_configuration(conf)

    # welcome user, ask year of data
    year = vtext.welcome_ask_year(interactive)

    frames = []
    for csv_single in csv:
        csv_index = csv.index(csv_single)

        df = report_generatorcsv.csv_to_dataframe(csv_single)

        # select necessary columns from df
        df = vtext.select_column(df, interactive, csv_index)

        frames.append(df)

    df_all = pd.concat(frames, join="outer", axis=0, ignore_index=True)

    # all raw data is imported. let's call analyzer to do something
    df_all = ag.add_cat_title(df_all)
    df_all = df_all.fillna(value="No Record")
    df_all = ag.get_sanity_data(df_all, cjk_support)

    # all datafram general data object
    df_all_g_data_obj = attendee.Attendee(df_all)

    # analyzed data frame is ready. let's plot attendee data
    figs = plotter.plot_attendee_counts(df_all, year, cjk_support)

    # prepared the selected topic pie chart
    talks_df = report_generatorcsv.csv_to_dataframe(talks_csv)
    talks_fig = plotter.plot_talk_categories(talks_df)
    figs.update(talks_fig)

    # prepared the proposed topic pie chart
    p_talks_df = report_generatorcsv.csv_to_dataframe(proposed_talks_csv)
    p_talks_fig = plotter.plot_talk_categories(p_talks_df, fig_title="Proposed_Topics")
    figs.update(p_talks_fig)

    booth_df = report_generatorcsv.csv_to_dataframe(booth_csv)
    # TODO: if we want to enhance the issue #11 in the future like #23, we may start here by using the returned value
    plotter.plot_booth(booth_df, "booth")

    # read the other report data
    report_yaml = report_generatoryaml.read_yaml(yaml)

    sponsors = apsponsor.get_all_sponsors(package_yaml, sponsor_yaml)

    accepted_talk_number = talks_df["category"].value_counts().sum()
    all_talk_number = p_talks_df["category"].value_counts().sum()
    talk_info_ratio = accepted_talk_number / all_talk_number
    talk_info = "{:.1%}".format(talk_info_ratio)
    # generate the report
    # general info (everyone could see it):
    #   figs: plots from attendee dataframe and talks
    #   df_all_g_data_obj: numbers from attendee dataframe
    #   report_yaml: plot description of figs
    # sponsors:
    #   sponsor specific information based on yaml descriptor
    print(
        f"{accepted_talk_number} accepted proposals out of {all_talk_number}. Accepted rate: {talk_info}"
    )
    exporter_html.generate(
        figs,
        report_yaml,
        df_all_g_data_obj,
        sponsors,
        talk_info,
        "sponsor.html",
        output_path=output_path,
    )

    # summary for internal review
    exporter_html.generate_summary(
        figs,
        report_yaml,
        df_all_g_data_obj,
        sponsors,
        talk_info,
        "internal.html",
        "internal-post-event",
        output_path,
    )

    print("Analysis process finished completely.")


if __name__ == "__main__":
    main()
