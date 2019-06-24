import yaml

class ConfigReader:
    """Config file reader
    Reads the content in config yaml file and based on that provides info
    """

    def __init__(self, config_file="./config.yaml"):
        """ Config file initiator """
        self._config_file = config_file

        self._read_config_file()

    def _read_config_file(self):
        """ Read the config file content and save to variables """

        with open(self._config_file, "r") as CONF_FILE:
            try:
                self._yaml_content = yaml.safe_load(CONF_FILE)
            except yaml.YAMLError as exc:
                print("Change me to log: ERROR: %s" % (exc,))

        self.url = self._yaml_content["url"]
        self.sensors = self._yaml_content["sensors"]
