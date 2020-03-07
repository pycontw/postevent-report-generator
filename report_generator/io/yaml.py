import logging

import yaml

logger = logging.getLogger("poolctl")


def read_yaml(input_yaml):
    with open(input_yaml, "r") as stream:
        try:
            yaml_load = yaml.load(stream)
            return yaml_load
        except yaml.YAMLError as e:
            logger.critical(e)
            logger.critical("No yaml was found at %s", input_yaml)
