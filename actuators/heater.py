# heater.py

heater_state = False


def heater_on():
    """Turn the heater on."""
    global heater_state
    heater_state = True


def heater_off():
    """Turn the heater off."""
    global heater_state
    heater_state = False


def get_heater_state():
    """Return the current heater state."""
    return heater_state