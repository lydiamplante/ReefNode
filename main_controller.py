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


def main():
    print("Starting Aquarium Controller — Base Script")
    print("------------------------------------------")

    while True:

        # -----------------------------------------
        # Clear Terminal
        # -----------------------------------------

        os.system('cls' if os.name == 'nt' else 'clear')


        # -----------------------------------------
        # Read Sensors
        # -----------------------------------------

        air_temp, humidity = read_air_sensor()
        water_temp = read_water_temp()
        water_level_ok = read_ATO_sensor()


        # -----------------------------------------
        # Temperature Control
        # -----------------------------------------

        if water_temp < 77.5:
            heater_on()
            fan_off()

        elif water_temp > 78.5:
            heater_off()
            fan_on()

        else:
            heater_off()
            fan_off()


        # -----------------------------------------
        # Water Level Control
        # -----------------------------------------

        if not water_level_ok:
            ato_on()

        else:
            ato_off()


        # -----------------------------------------
        # Get Actuator States
        # -----------------------------------------

        heater_state = get_heater_state()
        fan_state = get_fan_state()
        ato_state = get_ato_state()


        # -----------------------------------------
        # Print Sensor Readings
        # -----------------------------------------

        print_sensor_table(
            air_temp,
            humidity,
            water_temp,
            water_level_ok
        )


        # -----------------------------------------
        # Print Actuator States
        # -----------------------------------------

        print("\nActuators:\n")

        print(
            f"Heater       {'ON' if heater_state else 'OFF'}"
        )

        print(
            f"Cooling Fan  {'ON' if fan_state else 'OFF'}"
        )

        print(
            f"ATO Pump     {'ON' if ato_state else 'OFF'}"
        )


        # -----------------------------------------
        # Check Alerts
        # -----------------------------------------

        alerts = check_alerts(
            air_temp,
            humidity,
            water_temp,
            water_level_ok
        )

        if alerts:
            print("\nAlerts:\n")

            for alert in alerts:
                print(alert)

        else:
            print("\nAll systems normal ✔️")


        # -----------------------------------------
        # Wait Before Next Reading
        # -----------------------------------------

        time.sleep(5)


if __name__ == "__main__":
    main()