import random

# ============================================================
# AIR TEMP + HUMIDITY SENSOR PLACEHOLDER
# ============================================================
# When you get the real sensor:
#   - import the sensor library (Adafruit_DHT, SHT31, etc.)
#   - initialize the sensor object
#   - read values using sensor.temperature, sensor.humidity

def read_air_sensor():
    air_temp = random.uniform(72.0, 80.0)        # °F
    humidity = random.uniform(35.0, 55.0)        # %
    return air_temp, humidity
