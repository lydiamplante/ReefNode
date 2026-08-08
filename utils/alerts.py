def check_alerts(air_temp, humidity, water_temp, water_level_ok):
    alerts = []

    # Air temperature range
    if air_temp < 73 or air_temp > 78:
        alerts.append(f"⚠️ \tAir temperature out of range: {air_temp:.1f} °F")

    # Humidity range
    if humidity < 40 or humidity > 50:
        alerts.append(f"⚠️ \tHumidity out of range: {humidity:.1f} %")

    # Water temperature range
    if water_temp < 77 or water_temp > 78:
        alerts.append(f"⚠️ \tWater temperature out of range: {water_temp:.1f} °F")

    # ATO float switch
    if not water_level_ok:
        alerts.append("⚠️ \tWater level LOW — ATO needed")

    return alerts
