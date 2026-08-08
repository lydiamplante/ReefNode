import random

# ============================================================
# ATO FLOAT SWITCH PLACEHOLDER
# ============================================================
# When you get the real sensor:
#   - read GPIO pin HIGH/LOW
#   - optical sensors may return True/False

def read_ATO_sensor():
    water_level_ok = random.choice([True, True, True, True, True, False])
    return water_level_ok
