import pytest

from src.test.test_sensors.test_sensor import TestSensor as Sensor
from src.sensors.dht11_sensor import DHT11_Sensor

class DHT11_Raw_Data(DHT11_Sensor):
     """ This is class to use as data class for DHT11 tests """
     def __init__(self, humidity=30, temperature=20):
         self.humidity = humidity
         self.temperature = temperature

class TestDHT11_Sensor:
    """ General tests for DHT11_sensor functions """
    def init_data(self, key_name):
        self.raw_data = DHT11_Raw_Data(humidity=40,temperature=25)

    def test_init(self):
        pass

    def test_str(self):
        """ Function to test __str__() """
        key1 = "humidity"
        key2 = "temperature"

        # Test before and after run() method
