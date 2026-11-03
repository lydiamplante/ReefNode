import random

# ============================================================
# WATER TEMP SENSOR PLACEHOLDER (DS18B20, etc.)
# ============================================================
# When you get the real sensor:
#   - enable 1-Wire on the Pi
#   - read from /sys/bus/w1/devices/28-xxxx/w1_slave
#   - parse the temperature value

def read_water_temp():
    water_temp = random.uniform(76, 80)   # °F
    return water_temp
