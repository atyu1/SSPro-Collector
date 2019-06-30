import RPi.GPIO as GPIO
from DHT11_Python import dht11
import json

class SensorError(Excpetion):
    """ Sensor Issues are reported through custom error """
    pass


class Sensor(SensorError):
    """ General class for common sensor attributes """
    pass


class DHT11_Sensor(Sensor):
    """
    Class for direct work with sensor and get raw data from DHT11 sensor
    """

    def __init__(self, pin=4, key_name="missing"):
        # initialize GPIO
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.cleanup()

        self.reader = dht11.DHT11(pin=pin)
        self.raw_data = self.reader.read()
        self.key_name = key_name

    def __str__(self):
        """ Print the results for local testing """
        data = "%v: %d\n" % (self.key_name, self.raw_data.data)

        print (data) 

    def get_data(self):
        """ Get results in dictionary """
        if self.key_name == "humidity":
            data = {keyname:self.raw_data.humidity}
        elif self.key_name == "temperature":
            data = {keyname:self.raw_data.temperature}

        return data

    def run(self):
        """ Main run file to run this module """
        return self.get_data()
