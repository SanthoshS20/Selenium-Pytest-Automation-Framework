import yaml
import os


class ConfigReader:

    CONFIG_PATH = os.path.join(
        os.path.dirname(__file__),
        "qa.yaml"
    )

    @staticmethod
    def get_config():

        with open(ConfigReader.CONFIG_PATH, "r") as file:
            return yaml.safe_load(file)