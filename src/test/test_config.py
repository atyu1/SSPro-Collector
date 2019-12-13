import pytest

from src.config import ConfigReader

CONF_FILE="config_sample.yaml"

class TestConfigReader():
    def _init_config(self):
        self.config = ConfigReader(config_file=CONF_FILE)

    def test_read_config_file(self):
        self._init_config()

        url = "https://localhost/test"
        tokenuser = "test"
        tokenpass = "test"
        sensors = ["humidity","temperature"]

        assert url == self.config.url, "URL was changed and nont like in example"
        assert tokenuser == self.config.tokenuser, "Tokenuser is not test as expected in sample"
        assert tokenpass == self.config.tokenpass, "Tokenpass is not changeme as expected in sample"
        assert sensors == self.config.sensors, "List of loaded sensors is not the same"
