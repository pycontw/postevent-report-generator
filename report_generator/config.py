"""
Global config singlet.
"""
import logging
from configparser import ConfigParser

import pkg_resources

logger = logging.getLogger("report_generator")

resource_package = __name__
resource_path = "/".join(("data", "default.ini"))

template = pkg_resources.resource_stream(resource_package, resource_path)


class Configuration(object):
    __instance = None

    def __init__(self):
        self.config = None

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = Configuration()
        return cls.__instance

    def read_configuration(self, conf_file=None):
        """
        Read the initialization configuration file.

        The function will try to read the user specified configuration file
        first, and fall back expected values to default.ini if they are not
        found.

        All the read values will be then overridden by the special
        environmental variables if this function is invoked by report_generator_cli:main.

        :param conf_file: user specified configuration file.
        :return: configuration object
        """
        config = ConfigParser()
        # fill in default values to avoid too many KeyError
        config.read(template.name)
        # always provides default value
        config_default = ConfigParser()
        config_default.read(template.name)

        if conf_file:
            logger.debug("Reading conf...")
            logger.debug("Found %s", conf_file)
            config.read(conf_file)

        try:
            if conf_file and config["ATTENDEE"]["year"]:
                logger.debug("Override year by the given conf file.")
                logger.debug("It is %s ", config["ATTENDEE"]["year"])
        except KeyError:
            # fallback value
            config["ATTENDEE"]["year"] = config_default["ATTENDEE"]["year"]
            logger.debug("No given year. Use default.ini ")

        try:
            if conf_file and config["ATTENDEE"]["paid_date"]:
                logger.debug("Override year by the given conf file.")
                logger.debug("It is %s ", config["ATTENDEE"]["paid_date"])
        except KeyError:
            # fallback value
            config["ATTENDEE"]["paid_date"] = config_default["ATTENDEE"]["paid_date"]
            logger.debug("No given paid_date. Use default.ini ")

        try:
            if conf_file and config["ATTENDEE"]["nationality"]:
                logger.debug("Override nationality by the given conf file.")
                logger.debug("It is %s ", config["ATTENDEE"]["nationality"])
        except KeyError:
            # fallback value
            config["ATTENDEE"]["nationality"] = config_default["ATTENDEE"][
                "nationality"
            ]
            logger.debug("No given nationality. Use default.ini ")

        try:
            if conf_file and config["ATTENDEE"]["gender"]:
                logger.debug("Override gender by the given conf file.")
                logger.debug("It is %s ", config["ATTENDEE"]["gender"])
        except KeyError:
            # fallback value
            config["ATTENDEE"]["gender"] = config_default["ATTENDEE"]["gender"]
            logger.debug("No given gender. Use default.ini ")

        try:
            if conf_file and config["ATTENDEE"]["job_title"]:
                logger.debug("Override job_title by the given conf file.")
                logger.debug("It is %s ", config["ATTENDEE"]["job_title"])
        except KeyError:
            # fallback value
            config["ATTENDEE"]["job_title"] = config_default["ATTENDEE"]["job_title"]
            logger.debug("No given job_title. Use default.ini ")

        self.config = config
