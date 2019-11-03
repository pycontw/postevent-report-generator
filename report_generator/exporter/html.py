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

        img_data = open(img_path, "rb").read()
        data_uri = base64.b64encode(img_data).decode("utf-8").replace("\n", "")
        tag_template = '<img src="data:image/jpg;base64,{0}">'
        img_tag = tag_template.format(data_uri)
        all_tags.update({tag: img_tag})

        for entry in yaml:
            tag_yaml = entry.get(tag)
            if tag_yaml:
                p_tag_template = "<p>{0}</p>"
                p_tag = ""
                for meta in tag_yaml:
                    tag_description = meta.get("description")
                    if tag_description:
                        p_tag = p_tag_template.format(tag_description)

                all_tags.update({tag + "_Description": p_tag})

    # general info - more info
    tag_yaml_gi = yaml[0]["General_Info"]
    p_tag_template = "<p>{0}</p>"
    for meta in tag_yaml_gi:
        tag_gi_description = meta.get("description")
        p_tag = p_tag_template.format(tag_gi_description)
    all_tags.update({"General_Info_Description": p_tag})

    # general info - attendee number
    total_attendee_number = str(attendee_obj.total_attendee_number)
    total_attendee_number_tag = "<td>" + total_attendee_number + "</td>"
    all_tags.update({"general_total_attendee_number": total_attendee_number_tag})

    # apply information specific to each sponsor
    for sponsor in sponsors:
        # sponsor description
        all_tags.update({"sponsor_description": sponsor.description})

        # sponsor summary tables
        table_sponsor_package_template = "<td>{0}</td><td>{1}</td>"
        data = [sponsor.name, sponsor.package_name]
        tsp = table_sponsor_package_template.format(*data)

        all_tags.update({"table_sponsor_package": tsp})

        # promotion data
        # promotion - web
        table_promotion_web = "<td>{0}</td><td>{1}</td><td>{2}</td>"
        data_tpw = [sponsor.web_click, sponsor.web_click_portion, sponsor.web_click_rank]
        tpw = table_promotion_web.format(*data_tpw)

        all_tags.update({"table_promotion_web": tpw})

        # promotion - facebook
        # table_promotion_facebook: tpf summary
        tpf_row_template = "<tr><td>{0}</td><td>{1}</td><td>{2}</td></tr>"
        data = [
            sponsor.facebook_total_reached_people,
            sponsor.facebook_total_reach_portion,
            sponsor.facebook_total_reach_rank,
        ]
        tpf_row = tpf_row_template.format(*data)
        all_tags.update({"table_promotion_facebook_summary": tpf_row})

        # table_promotion_facebook: tpf
        tpf_rows = ""
        for url in sponsor.facebook_url.keys():
            tpf_row_template = "<tr><td><a href={0}>{0}</a></td>" "<td>{1}</td><td>{2}</td></tr>"
            data = [url, sponsor.facebook_url[url]["reach"], sponsor.facebook_url[url]["engagement"]]
            tpf_row = tpf_row_template.format(*data)
            tpf_rows += tpf_row
        all_tags.update({"table_promotion_facebook": tpf_rows})

        # booth
        all_tags.update({"booth_flag": sponsor.if_one_true_booth})
        if sponsor.if_one_true_booth:
            table_booth_template = "<td>{0}</td><td>{1}</td>"
            data = [sponsor.booth_participant, sponsor.booth_participant_rank]
            table_booth = table_booth_template.format(*data)
            all_tags.update({"table_booth": table_booth})

        # workshop
        workshop_url_tag_template = "<a href={0}>{0}</a>"
        data = sponsor.workshop_event_url
        workshop_url_tag = "Event Link - " + workshop_url_tag_template.format(data)
        all_tags.update({"workshop_flag": sponsor.if_one_true_workshop})
        all_tags.update({"workshop_event_url": workshop_url_tag})
        all_tags.update({"workshop_description": sponsor.workshop_description})

        filename_template = "post-event-report-sponsor-{}.html"
        filename = filename_template.format(sponsor.name)
        full_output_path = Path(output_path).absolute() / Path(filename)
        with open(full_output_path, "w") as fhandler:
            r = template.render(**all_tags)
            fhandler.write(r)
