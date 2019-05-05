# TODO
# main file
from sensors.humidity_temperature import humidity_sensor as HUMIDITY
from sensors.humidity_temperature import temperature_sensor as TEMPERATURE

HUM_SEN = HUMIDITY()
TEMP_SEN = TEMPERATURE()

print (HUM_SEN.run())
print (TEMP_SEN.run())
