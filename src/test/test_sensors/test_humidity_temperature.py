
from src.test.test_sensors.test_dht11_sensor import DHT11_Fake_Sensor as DHT11_Sensor

class TestHumiditySensor(DHT11_Sensor):
    """
    Class for direct work with sensor and get raw data from DHT11 sensor,
    we target in this class for humidity
    """

    def __init__(self, pin=4, key_name="humidity", sensor_data=30):
        super().__init__(pin=pin, key_name=key_name)

class TestTemperatureSensor(DHT11_Sensor):
    """
    Class for direct work with sensor and get raw data from DHT11 sensor,
    we target in this class for temperature
    """

    def __init__(self, pin=4, key_name="temperature", sensor_data=20):
        super().__init__(pin=pin, key_name=key_name)


def test_humidity():
    """ Function to test humidity based on Fake humidity class """

    expected_data = {"humidity":20}
    expected_string = "{'humidity': 20}"

    tmp_sensor = TestHumiditySensor()
    tmp_sensor.raw_data.humidity = 20

    tmp_sensor_value = tmp_sensor.get_data()

    assert tmp_sensor_value == expected_data
    assert str(tmp_sensor_value) == expected_string
    assert str(tmp_sensor) == expected_string

def test_temperature():
    """ Function to test humidity based on Fake humidity class """

    expected_data = {"temperature":30}
    expected_string = "{'temperature': 30}"

    tmp_sensor = TestTemperatureSensor()
    tmp_sensor.raw_data.temperature = 30

    tmp_sensor_value = tmp_sensor.get_data()

    assert tmp_sensor_value == expected_data
    assert str(tmp_sensor_value) == expected_string
    assert str(tmp_sensor) == expected_string

