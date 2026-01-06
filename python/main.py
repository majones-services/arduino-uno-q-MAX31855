import time
import math
from arduino.app_utils import *

def loop():
    """
    This function is called repeatedly by the App framework.
    It requests and prints the temperature from three thermocouples.
    """
    print("Requesting temperatures...")
    try:
        # Use the generic 'call' method to invoke remote functions
        temp1 = Bridge.call("get_temp1")
        if temp1 is not None and not math.isnan(temp1):
            print(f"  THERMO1: {temp1:.2f} C")
        else:
            print("  THERMO1: Invalid reading")
    except Exception as e:
        print(f"  Error reading THERMO1: {e}")

    time.sleep(0.2)  # Small delay for robustness

    try:
        temp2 = Bridge.call("get_temp2")
        if temp2 is not None and not math.isnan(temp2):
            print(f"  THERMO2: {temp2:.2f} C")
        else:
            print("  THERMO2: Invalid reading")
    except Exception as e:
        print(f"  Error reading THERMO2: {e}")

    time.sleep(0.2)  # Small delay for robustness

    try:
        temp3 = Bridge.call("get_temp3")
        if temp3 is not None and not math.isnan(temp3):
            print(f"  THERMO3: {temp3:.2f} C")
        else:
            print("  THERMO3: Invalid reading")
    except Exception as e:
        print(f"  Error reading THERMO3: {e}")

    print("-" * 20)
    # Wait for 5 seconds before the next loop
    time.sleep(5)


# See: https://docs.arduino.cc/software/app-lab/tutorials/getting-started/#app-run
App.run(user_loop=loop)
