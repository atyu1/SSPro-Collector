#import RPi.GPIO as GPIO
#from DHT11_Python import dht11
import json

class SensorError(Exception):
    """ Sensor Issues are reported through custom error """
    pass

class Sensor(SensorError):
    """ General class for common sensor attributes """
    pass

