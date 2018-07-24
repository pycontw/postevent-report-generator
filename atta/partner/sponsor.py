import logging
import pkg_resources
import atta.io.yaml as attayaml
from abc import ABCMeta, abstractmethod

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


class Package(metaclass=ABCMeta):

    def __init__(self, package_name, sponsor_name):
        self.package_name = package_name
        self.package_content_flag = yaml_packages[package_name]
        self.package_content_generic_flag = yaml_packages['generic']
        self.sections = []
        self.create_profile(package_name, sponsor_name)

    @abstractmethod
    def create_profile(self, name):
        pass

    def get_sections(self):
        return self.sections

    def add_section(self, section):
        self.sections.append(section)

    @property
    def description(self):
        pass


class Sponsor(Package):

    def create_profile(self, package_name, sponsor_name):
        pass
