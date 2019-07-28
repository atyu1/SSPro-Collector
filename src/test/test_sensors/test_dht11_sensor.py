import pytest

from src.test.test_sensors.test_sensor import TestSensor as Sensor
from src.sensors.dht11_sensor import DHT11_Sensor

class DHT11_Fake_Sensor(DHT11_Sensor):
     """ This is class to use as data class for DHT11 tests """
     def __init__(self, pin=1, humidity=30, temperature=20, key_name="test", sensor_data=10):
         self.pin = pin
         self.raw_data = self.RawData()
         self.raw_data.humidity = humidity
         self.raw_data.temperature = temperature
         self.raw_data.valid = True
         self.key_name = key_name
         self.sensor_data = sensor_data 

     class RawData:
         def __init__(self):
             pass

         def is_valid(self):
             return self.valid

class TestDHT11_Sensor:
    """ General tests for DHT11_sensor functions """
    def __init__(self):
        self._dht11_reader()

    def _dht11_reader(self):
        self.reader = DHT11_Fake_Sensor()  #Leave default values

    def test_init(self):
        assert self.reader.pin == 1
        assert self.reader.raw_data.humidity == 30
        assert self.reader.raw_data.temperature == 20
        assert self.reader.key_name == "test"
        assert self.reader.sensor_data == 10

    def test_get_data(self):
        """ Function to test __str__() """
        key1 = "humidity"
        key2 = "temperature"
   
        expected_data1 = {key1:self.reader.sensor_data}
        expected_data2 = {key2:self.reader.sensor_data}

        self.reader.key_name = key1
        data1 = self.get_data()

        assert data1 == expected_data1
 
        
