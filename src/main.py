# main file
from sensors.humidity_temperature import humidity_sensor as HUMIDITY
from sensors.humidity_temperature import temperature_sensor as TEMPERATURE
from sender import JsonSender
from config import ConfigReader

config_content = ConfigReader()

data = []
sensors = sensor_modularize(config_content)

for sensor in sensors:
    data.append(sensor.run())

print (data)
sender = JsonSender("https://localhost/test")
sender.push()

def sensor_modularize(config):
    """ Create a list of modules based on config file enabled sensors """
   
    tmp_sensors = []

    if "humidity" in config.sensors:
        tmp_sensors.append(HUMIDITY())

    if "temperature" in config.sensors:
        tmp_sensors.append(TEMPERATURE())

    return tmp_sensors
