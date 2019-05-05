import RPi.GPIO as GPIO
from DHT11_Python import dht11
import json

class TempHumSensorReader:
    """
    Class for direct work with sensor and get raw data from DHT11 sensor
    """

    def __init__(self, pin=4):
        # initialize GPIO
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.cleanup()

        self._reader = dht11.DHT11(pin=pin)
        self._raw_data = self._read_raw()

    def _read_raw(self):
        "Read the digits from sensor directly"""
        result = self._reader.read()

        return result

    def get_data(self):
        """ Get results in dictionary """
        data = {"temperature":self._raw_data.temperature, 
                "humidity":self._raw_data.humidity}

    def print_text(self):
        """ Print the results for local testing """
        data = "Temperature: %d\nHumidity: %d\n" % (self._raw_data.temperature,
                self._raw_data.humidity)

        print (data) 

if __name__ == "__main__":
    reader = TempHumSensorReader()
    reader.print_text()
