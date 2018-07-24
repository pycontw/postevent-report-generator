import logging
import pkg_resources
import atta.io.yaml as attayaml

logger = logging.getLogger('atta')

resource_package = __name__
resource_path_packages = '/'.join(('../data', 'packages.yaml'))
resource_path_sponsors = '/'.join(('../data', 'sponsors.yaml'))

template_packages = pkg_resources.resource_stream(resource_package,
                                                  resource_path_packages)

template_sponsors = pkg_resources.resource_stream(resource_package,
                                                  resource_path_sponsors)

yaml_packages = attayaml.read_yaml(template_packages.name)
yaml_sponsors = attayaml.read_yaml(template_sponsors.name)


class Sponsor:

    def __init__(self, sponsor_name):
        self.name = sponsor_name
        self.package_name = yaml_sponsors[sponsor_name]['package']

        self.content = yaml_sponsors[self.name]
        self.package_content_flag = yaml_packages[self.package_name]
        self.package_content_generic_flag = yaml_packages['generic']

    @property
    def flag_description(self):
        return self.package_content_flag['description']

    @property
    def description(self):
        if self.flag_description:
            return self.content['description']
        else:
            self.flag_description

    @property
    def flag_web_click(self):
        return self.package_content_flag['promotion']['web']['click']

    @property
    def web_click(self):
        if self.flag_web_click:
            return self.content['promotion']['web']['click']
        else:
            return self.flag_web_click

def get_all_sponsors():
    sponsors = []
    for entry in yaml_sponsors:
        sponsor = Sponsor(entry)
        description = sponsor.description
        web_click = sponsor.web_click
        pass

    sponsors.append(sponsor)

    return sponsors
