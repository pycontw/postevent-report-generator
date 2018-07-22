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


class Package:

    def __init__(self):
        pass

class Sponsor(Package):

    def get_sponsors(self):
        pass