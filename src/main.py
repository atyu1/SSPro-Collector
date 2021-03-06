# main file
from sensors.humidity_temperature import HumiditySensor as HUMIDITY
from sensors.humidity_temperature import TemperatureSensor as TEMPERATURE
from sender import JsonSender
from config import ConfigReader

def sensor_modularize(config):
    """ Create a list of modules based on config file enabled sensors """
   
    tmp_sensors = []

    if "humidity" in config.sensors:
        tmp_sensors.append(HUMIDITY())

    if "temperature" in config.sensors:
        tmp_sensors.append(TEMPERATURE())

    return tmp_sensors

def main():
    config_content = ConfigReader()

    data = []
    sensors = sensor_modularize(config_content)

    for sensor in sensors:
        data.append(sensor.run())


    print (data)
    sender = JsonSender("https://localhost", data)
    sender.login(config_content.tokenuser, config_content.tokenpass)
    sender.push(data)

if __name__ == "__main__":
	main()
