# SSPro-Collector

## Overview


## Install


## Quick Guide


## System Admin Part


### Testing

Manual Testing:

```
[test@localhost src]$ pwd
/home/test/code/SSPro-Collector/src
[test@localhost src]$ pytest
================================================================================== test session starts ==================================================================================
platform linux -- Python 3.6.8, pytest-5.0.0, py-1.8.0, pluggy-0.12.0
rootdir: /home/test/code/SSPro-Collector/src
collected 3 items                                                                                                                                                                       

test/test_config.py .                                                                                                                                                             [ 33%]
test/test_sensors/test_dht11_sensor.py ..                                                                                                                                         [100%]

=============================================================================== 3 passed in 0.07 seconds ================================================================================
[test@localhost src]$ 
```

Testing via Docker:

```
[test@localhost SSPro-Collector]$ docker build -f Dockerfile.test -t asovak/sspro-collector:test .
<Progress ommited>

[test@localhost SSPro-Collector]$ docker run -it --rm --name test-ssprocollector asovak/sspro-collector:test
================================================================================== test session starts ==================================================================================
platform linux -- Python 3.7.3, pytest-5.0.0, py-1.8.0, pluggy-0.12.0
rootdir: /var/app/src
collected 5 items                                                                                                                                                                       

test/test_config.py .                                                                                                                                                             [ 20%]
test/test_sensors/test_dht11_sensor.py ..                                                                                                                                         [ 60%]
test/test_sensors/test_humidity_temperature.py ..                                                                                                                                 [100%]

=================================================================================== warnings summary ====================================================================================
test/test_sensors/test_humidity_temperature.py:4
  /var/app/src/test/test_sensors/test_humidity_temperature.py:4: PytestCollectionWarning: cannot collect test class 'TestHumiditySensor' because it has a __init__ constructor (from: test/test_sensors/test_humidity_temperature.py)
    class TestHumiditySensor(DHT11_Sensor):

test/test_sensors/test_humidity_temperature.py:13
  /var/app/src/test/test_sensors/test_humidity_temperature.py:13: PytestCollectionWarning: cannot collect test class 'TestTemperatureSensor' because it has a __init__ constructor (from: test/test_sensors/test_humidity_temperature.py)
    class TestTemperatureSensor(DHT11_Sensor):

-- Docs: https://docs.pytest.org/en/latest/warnings.html
========================================================================= 5 passed, 2 warnings in 0.13 seconds ==========================================================================
[test@localhost SSPro-Collector]$ 
```
