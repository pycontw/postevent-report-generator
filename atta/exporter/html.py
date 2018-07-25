import base64
import atta.partner.sponsor as asponsor
from jinja2 import Environment, PackageLoader
from jinja2 import Markup


loader=PackageLoader('atta.exporter', 'data')
env = Environment(loader=loader)


def generate(data=None, yaml=None):
    def include_file(name):
        # This helper function insert static files literally into Jinja
        # templates without parsing them.
        return Markup(loader.get_source(env, name)[0])

    env.globals['include_file'] = include_file

    template = env.get_template('sponsor.html')

    all_tags = {}
    for tag in data:
        img_path = data[tag]

        img_data = open(img_path, 'rb').read()
        data_uri = base64.b64encode(img_data).decode('utf-8').replace('\n','')
        tag_template = '<img src="data:image/jpg;base64,{0}">'
        img_tag = tag_template.format(data_uri)
        all_tags.update({tag: img_tag})

        for entry in yaml:
            tag_yaml = entry.get(tag)
            if tag_yaml:
                p_tag_template = '<p>{0}</p>'
                p_tag = ''
                for meta in tag_yaml:
                    tag_description = meta.get('description')
                    if tag_description:
                        p_tag = p_tag_template.format(tag_description)

                all_tags.update({tag + '_Description': p_tag})


    sponsors = asponsor.get_all_sponsors()

    for sponsor in sponsors:
        table_sponsor_package_template = '<td>{0}</td><td>{1}</td>'
        data = [sponsor.name, sponsor.package_name]
        tsp = table_sponsor_package_template.format(*data)

        all_tags.update({'table_sponsor_package': tsp})

        with open('/tmp/atta.html', 'w') as fhandler:
            r = template.render(**all_tags)
            fhandler.write(r)
