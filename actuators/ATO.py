# ATO.py

ato_state = False


def ato_on():
    """Turn the ATO pump on."""
    global ato_state
    ato_state = True


def ato_off():
    """Turn the ATO pump off."""
    global ato_state
    ato_state = False


def get_ato_state():
    """Return the current ATO pump state."""
    return ato_state