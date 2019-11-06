import base64
from pathlib import Path

from jinja2 import Environment, PackageLoader
from jinja2 import Markup


loader = PackageLoader("report_generator.exporter", "data")
env = Environment(loader=loader)


def generate(data=None, yaml=None, attendee_obj=None, sponsors=None, output_path="/tmp"):
    def include_file(name):
        # This helper function insert static files literally into Jinja
        # templates without parsing them.
        return Markup(loader.get_source(env, name)[0])

    env.globals["include_file"] = include_file

    template = env.get_template("sponsor.html")

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
    for meta in tag_yaml_gi:
        tag_gi_description = meta.get("description")
        p_tag = f"<p>{tag_gi_description}</p>"
    all_tags.update({"General_Info_Description": p_tag})

    # general info - attendee number
    total_attendee_number_tag = f"<td>{attendee_obj.total_attendee_number}</td>"
    all_tags.update({"general_total_attendee_number": total_attendee_number_tag})

    # apply information specific to each sponsor
    for sponsor in sponsors:
        # sponsor description
        all_tags.update({"sponsor_description": sponsor.description})

        # sponsor summary tables
        table_sponsor_package = f"<td>{sponsor.name}</td><td>{sponsor.package_name}</d>"
        all_tags.update({"table_sponsor_package": table_sponsor_package})

        # promotion data
        # promotion - web
        table_promotion_web = (
            f"<td>{sponsor.web_click}</td>"
            f"<td>{sponsor.web_click_portion}</td>"
            f"<td>{sponsor.web_click_rank}</td>"
        )
        all_tags.update({"table_promotion_web": table_promotion_web})

        # promotion - facebook
        # table_promotion_facebook: tpf summary
        tpf_row = (
            "<tr>"
            f"<td>{sponsor.facebook_total_reached_people}</td>"
            f"<td>{sponsor.facebook_total_reach_portion}</td>"
            f"<td>{sponsor.facebook_total_reach_rank}</td>"
            "</tr>"
        )
        all_tags.update({"table_promotion_facebook_summary": tpf_row})

        # table_promotion_facebook: tpf
        tpf_rows = ""
        for url in sponsor.facebook_url.keys():
            reach = sponsor.facebook_url[url]["reach"]
            engagement = sponsor.facebook_url[url]["engagement"]
            tpf_row = f"<tr><td><a href={url}>{url}</a></td><td>{reach}</td><td>{engagement}</td></tr>"
            tpf_rows += tpf_row
        all_tags.update({"table_promotion_facebook": tpf_rows})

        # booth
        all_tags.update({"booth_flag": sponsor.if_one_true_booth})
        if sponsor.if_one_true_booth:
            table_booth = f"<td>{sponsor.booth_participant}</td><td>{sponsor.booth_participant_rank}</td>"
            all_tags.update({"table_booth": table_booth})

        # workshop
        workshop_url_tag = f"Event Link - <a href={sponsor.workshop_event_url}>{sponsor.workshop_event_url}</a>"
        all_tags.update({"workshop_flag": sponsor.if_one_true_workshop})
        all_tags.update({"workshop_event_url": workshop_url_tag})
        all_tags.update({"workshop_description": sponsor.workshop_description})

        # export report
        filename = f"post-event-report-sponsor-{sponsor.name}.html"
        full_output_path = Path(output_path).absolute() / Path(filename)
        with open(full_output_path, "w") as fhandler:
            r = template.render(**all_tags)
            fhandler.write(r)
