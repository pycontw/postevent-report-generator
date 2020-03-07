import base64
from collections.abc import Iterable
from pathlib import Path

from jinja2 import Environment, Markup, PackageLoader

loader = PackageLoader("report_generator.exporter", "data")
env = Environment(loader=loader)


def _generate_html_rows(*data, with_tr=False):
    if not isinstance(data, Iterable):
        data = (data,)
    html_rows = "".join([f"<td>{datum}</td>" for datum in data])
    if not with_tr:
        return html_rows
    return f"<tr>{html_rows}</tr>"


def _generate_html_link(url: str):
    return f"<a href={url}>{url}</a>"


def generate(
    data=None,
    yaml=None,
    attendee_obj=None,
    sponsors=None,
    talk_info=None,
    html_template="sponsor.html",
    output_prefix="post-event",
    output_path="/tmp",
):
    def include_file(name):
        # This helper function insert static files literally into Jinja
        # templates without parsing them.
        return Markup(loader.get_source(env, name)[0])

    env.globals["include_file"] = include_file

    print("Exporting a html report based on the template: {}".format(html_template))
    template = env.get_template(html_template)

    # hosting all tags that will be applied to the jinja2 target string
    all_tags = {}

    # apply general information which everyone could see it
    # general info - description for plots
    #    Add plot description if it could be found in the yaml
    for tag in data:
        img_path = data[tag]

        with open(img_path, "rb") as img_file:
            img_data = img_file.read()
            data_uri = base64.b64encode(img_data).decode("utf-8").replace("\n", "")

        img_tag = f'<img src="data:image/jpg;base64,{data_uri}">'
        all_tags.update({tag: img_tag})

        for entry in yaml:
            tag_yaml = entry.get(tag)
            if tag_yaml:
                p_tag = ""
                for meta in tag_yaml:
                    tag_description = meta.get("description")
                    if tag_description:
                        p_tag = f"<p>{tag_description}</p>"

                all_tags.update({tag + "_Description": p_tag})

    # general info - more info
    tag_yaml_gi = yaml[0]["General_Info"]
    p_tag = ""
    for meta in tag_yaml_gi:
        tag_gi_description = meta.get("description")
        p_tag = f"<p>{tag_gi_description}</p>"
    all_tags.update({"General_Info_Description": p_tag})

    # general info - attendee number
    total_attendee_number_tag = _generate_html_rows(attendee_obj.total_attendee_number)
    all_tags.update({"general_total_attendee_number": total_attendee_number_tag})

    # apply information specific to each sponsor
    for sponsor in sponsors:
        # sponsor description
        all_tags.update({"sponsor_description": sponsor.description})

        # sponsor summary tables
        table_sponsor_package = _generate_html_rows(sponsor.name, sponsor.package_name)
        all_tags.update({"table_sponsor_package": table_sponsor_package})

        # promotion data
        # promotion - web
        table_promotion_web = _generate_html_rows(
            sponsor.web_click, sponsor.web_click_portion
        )
        all_tags.update({"table_promotion_web": table_promotion_web})

        # promotion - facebook
        # table_promotion_facebook: tpf summary
        tpf_row = _generate_html_rows(
            sponsor.facebook_total_reached_people,
            sponsor.facebook_total_reach_portion,
            with_tr=True,
        )
        all_tags.update({"table_promotion_facebook_summary": tpf_row})

        # table_promotion_facebook: tpf
        tpf_rows = ""
        for url in sponsor.facebook_url.keys():
            html_url = _generate_html_link(url)
            reach = sponsor.facebook_url[url]["reach"]
            engagement = sponsor.facebook_url[url]["engagement"]
            tpf_row = _generate_html_rows(html_url, reach, engagement, with_tr=True)
            tpf_rows += tpf_row
        all_tags.update({"table_promotion_facebook": tpf_rows})

        # booth
        all_tags.update({"booth_flag": sponsor.if_one_true_booth})
        if sponsor.if_one_true_booth:
            table_booth = _generate_html_rows(
                sponsor.booth_participant, sponsor.booth_participant_portion
            )
            all_tags.update({"table_booth": table_booth})

        # workshop
        workshop_url_tag = (
            f"Event Link - {_generate_html_link(sponsor.workshop_event_url)}"
        )
        all_tags.update({"workshop_flag": sponsor.if_one_true_workshop})
        all_tags.update({"workshop_event_url": workshop_url_tag})
        all_tags.update({"workshop_description": sponsor.workshop_description})

        # export report
        filename = f"{output_prefix}-report-sponsor-{sponsor.name}.html"
        full_output_path = Path(output_path).absolute() / Path(filename)
        with open(full_output_path, "w") as fhandler:
            r = template.render(**all_tags)
            fhandler.write(r)

    print("Dumping post event reports for each sponsor to {}".format(output_path))


def generate_summary(
    data=None,
    yaml=None,
    attendee_obj=None,
    sponsors=None,
    talk_info=None,
    html_template="sponsor.html",
    output_prefix="internal-summary-post-event",
    output_path="/tmp",
):
    def include_file(name):
        # This helper function insert static files literally into Jinja
        # templates without parsing them.
        return Markup(loader.get_source(env, name)[0])

    env.globals["include_file"] = include_file

    print("Exporting a html report based on the template: {}".format(html_template))
    template = env.get_template(html_template)

    # hosting all tags that will be applied to the jinja2 target string
    all_tags = {}

    # apply general information which everyone could see it
    # general info - description for plots
    #    Add plot description if it could be found in the yaml
    for tag in data:
        img_path = data[tag]

        with open(img_path, "rb") as img_file:
            img_data = img_file.read()
            data_uri = base64.b64encode(img_data).decode("utf-8").replace("\n", "")

        img_tag = f'<img src="data:image/jpg;base64,{data_uri}">'
        all_tags.update({tag: img_tag})

        for entry in yaml:
            tag_yaml = entry.get(tag)
            if tag_yaml:
                p_tag = ""
                for meta in tag_yaml:
                    tag_description = meta.get("description")
                    if tag_description:
                        p_tag = f"<p>{tag_description}</p>"

                all_tags.update({tag + "_Description": p_tag})

    # # general info - more info
    # tag_yaml_gi = yaml[0]["General_Info"]
    # p_tag = ""
    # for meta in tag_yaml_gi:
    #     tag_gi_description = meta.get("description")
    #     p_tag = f"<p>{tag_gi_description}</p>"
    # all_tags.update({"General_Info_Description": p_tag})

    # general info - attendee number
    total_attendee_number_tag = _generate_html_rows(attendee_obj.total_attendee_number)
    all_tags.update({"general_total_attendee_number": total_attendee_number_tag})

    # general info - accepted rate
    accepted_rate_tag = _generate_html_rows(talk_info)
    all_tags.update({"table_proposal_info": accepted_rate_tag})

    # apply information specific to each sponsor
    table_promotion_web_all = ""
    tpfs_row_all = ""
    tpf_rows_all = ""
    table_booth_all = ""
    for sponsor in sponsors:
        # promotion data
        # promotion - web
        table_promotion_web = _generate_html_rows(
            sponsor.name,
            sponsor.package_name,
            sponsor.web_click,
            sponsor.web_click_portion,
            sponsor.web_click_rank,
            with_tr=True,
        )
        table_promotion_web_all = table_promotion_web_all + table_promotion_web

        # promotion - facebook
        # table_promotion_facebook_summary: tpf summary
        tpfs_row = _generate_html_rows(
            sponsor.name,
            sponsor.package_name,
            sponsor.facebook_total_reached_people,
            sponsor.facebook_total_reach_portion,
            sponsor.facebook_total_reach_rank,
            with_tr=True,
        )
        tpfs_row_all = tpfs_row_all + tpfs_row

        # table_promotion_facebook: tpf
        tpf_rows = ""
        for url in sponsor.facebook_url.keys():
            html_url = _generate_html_link(url)
            reach = sponsor.facebook_url[url]["reach"]
            engagement = sponsor.facebook_url[url]["engagement"]
            tpf_row = _generate_html_rows(
                sponsor.name,
                sponsor.package_name,
                reach,
                engagement,
                html_url,
                with_tr=True,
            )
            tpf_rows += tpf_row
        tpf_rows_all = tpf_rows_all + tpf_rows

        # booth
        table_booth = _generate_html_rows(
            sponsor.name,
            sponsor.package_name,
            sponsor.booth_participant,
            sponsor.booth_participant_portion,
            sponsor.booth_participant_rank,
            with_tr=True,
        )
        table_booth_all = table_booth_all + table_booth

    all_tags.update({"table_promotion_web_all": table_promotion_web_all})
    all_tags.update({"table_promotion_facebook_summary_all": tpfs_row_all})
    all_tags.update({"table_promotion_facebook_all": tpf_rows_all})
    all_tags.update({"table_booth": table_booth_all})

    # export report
    filename = f"{output_prefix}-report.html"
    full_output_path = Path(output_path).absolute() / Path(filename)
    print("Dumping summary to {}".format(full_output_path))
    with open(full_output_path, "w") as fhandler:
        r = template.render(**all_tags)
        fhandler.write(r)
