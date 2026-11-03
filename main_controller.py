import time
import os

# Import sensor modules
from sensors.air_sensor import read_air_sensor
from sensors.water_temp_sensor import read_water_temp
from sensors.ATO_sensor import read_ATO_sensor

# Import utilities
from utils.formatting import print_sensor_table
from utils.alerts import check_alerts

# Import actuators
from actuators.heater import heater_on, heater_off, get_heater_state
from actuators.fan import fan_on, fan_off, get_fan_state
from actuators.ATO import ato_on, ato_off, get_ato_state


def read_controller_state():
    """Read sensors once, apply automatic control, and return a snapshot."""
    air_temp, humidity = read_air_sensor()
    water_temp = read_water_temp()
    water_level_ok = read_ATO_sensor()
    if water_temp < 77.5:
        heater_on(); fan_off()
    elif water_temp > 78.5:
        heater_off(); fan_on()
    else:
        heater_off(); fan_off()
    if water_level_ok:
        ato_off()
    else:
        ato_on()
    return {"air_temp": air_temp, "humidity": humidity, "water_temp": water_temp,
            "water_level_ok": water_level_ok, "heater": get_heater_state(),
            "fan": get_fan_state(), "ato": get_ato_state(),
            "alerts": check_alerts(air_temp, humidity, water_temp, water_level_ok)}


def main():
    while True:
        state = read_controller_state()
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Aquarium Controller — Simulation")
        print_sensor_table(state["air_temp"], state["humidity"], state["water_temp"], state["water_level_ok"])
        print("\nActuators:\n")
        for label, key in (("Heater", "heater"), ("Cooling Fan", "fan"), ("ATO Pump", "ato")):
            print(f"{label:12} {'ON' if state[key] else 'OFF'}")
        print("\nAlerts:\n" + "\n".join(state["alerts"]) if state["alerts"] else "\nAll systems normal ✔️")
        time.sleep(5)


if __name__ == "__main__":
    main()
