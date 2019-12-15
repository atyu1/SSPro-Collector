from sensors.dht11_sensor import DHT11_Sensor

class HumiditySensor(DHT11_Sensor):
    """
    Class for direct work with sensor and get raw data from DHT11 sensor,
    we target in this class for humidity
    """

    def __init__(self, pin=4, key_name="humidity"):
        super().__init__(pin=pin, key_name=key_name)
       
class TemperatureSensor(DHT11_Sensor):
    """
    Class for direct work with sensor and get raw data from DHT11 sensor,
    we target in this class for temperature
    """

    def __init__(self, pin=4, key_name="temperature"):
        super().__init__(pin=pin, key_name=key_name)
