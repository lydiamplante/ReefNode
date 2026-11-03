fan_state = False


def fan_on():
    """Turn the cooling fan on."""
    global fan_state
    fan_state = True


def fan_off():
    """Turn the cooling fan off."""
    global fan_state
    fan_state = False


def get_fan_state():
    """Return the current fan state."""
    return fan_state