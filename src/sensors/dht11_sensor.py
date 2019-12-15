
import RPi.GPIO as GPIO
import DHT11_Python.dht11 as dht11
from sensors.sensor import Sensor
from sensors.sensor import SensorError

class DHT11_Sensor(Sensor):
    """
    Class for direct work with sensor and get raw data from DHT11 sensor
    """

    def __init__(self, pin=4, key_name="missing"):
        # initialize GPIO
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.cleanup()

        self.pin = pin
        self.key_name = key_name
        self.retries = 3

    def _dht11_reader(self):
        self.reader = dht11.DHT11(pin=self.pin)
        self.raw_data = self.reader.read()
 
    def __str__(self):
        """ Print the results for local testing """
        if not self.sensor_data: # Data collected only after run() fucntion called
            return ""

        return str(self.sensor_data)

    def get_data(self):
        """ Get results in dictionary """
        while not self._validate_data():
            continue

        if self.key_name == "humidity":
            self.sensor_data = {self.key_name:self.raw_data.humidity}
        elif self.key_name == "temperature":
            self.sensor_data = {self.key_name:self.raw_data.temperature}

        return self.sensor_data

    def run(self):
        """ Main run file to run this module """
        self._dht11_reader()
        return self.get_data()

    def _validate_data(self):
        if self.raw_data.is_valid():
            return True
        elif self.retries > 0:
            self.raw_data = self.reader.read()
            self.retries-= 1
            return False  # This we still need to validate
        else:
            raise SensorError("Data from DHT11 is not valid")
