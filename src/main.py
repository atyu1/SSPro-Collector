# TODO
# main file
from sensors.humidity_temperature import humidity_sensor as HUMIDITY
from sensors.humidity_temperature import temperature_sensor as TEMPERATURE
from sender import JsonSender

data = []

sensors = [ HUMIDITY(), 
            TEMPERATURE(),
          ]

for sensor in sensors:
    data.append(sensor.run())

sender = JsonSender("https://localhost/test")
sender.push()
