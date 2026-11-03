def print_sensor_table(air_temp, humidity, water_temp, water_level_ok):
    print("\nSensor Readings:\n")
    print(f" Air Temp              {air_temp:6.1f} °F")
    print(f" Humidity              {humidity:6.1f} % ")
    print(f" Water Temp            {water_temp:6.1f} °F")
    print(f" ATO Status            {'OK' if water_level_ok else 'LOW':>6}\n")

    
