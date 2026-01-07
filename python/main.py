import time
import math
from arduino.app_utils import App, Bridge

def run_raw_latency_test():
    """
    Measures the raw round-trip latency of a call to the Arduino.
    """
    print("--- Running RAW Latency Test ---")
    time.sleep(2)
    
    num_executions = 10
    latencies = []

    print(f"  Performing {num_executions} test calls...")

    for i in range(num_executions):
        try:
            start_time = time.perf_counter()
            Bridge.call("ping")
            end_time = time.perf_counter()
            
            duration_ms = (end_time - start_time) * 1000
            latencies.append(duration_ms)
            time.sleep(0.1)
        except Exception as e:
            print(f"  Error during ping execution {i+1}: {e}")
            continue

    if not latencies:
        print("  Raw Latency test failed: No successful pings.")
        print("----------------------------")
        return

    min_latency = min(latencies)
    max_latency = max(latencies)
    avg_latency = sum(latencies) / len(latencies)

    print("\n  --- Raw Latency Results ---")
    print(f"  Min Latency: {min_latency:.2f} ms")
    print(f"  Max Latency: {max_latency:.2f} ms")
    print(f"  Avg Latency: {avg_latency:.2f} ms")
    print("----------------------------")
    time.sleep(1)

def run_temp_latency_test():
    """
    Measures the latency of calling get_temp1 and prints individual results.
    """
    print("--- Running Temperature Latency Test ---")
    time.sleep(1)

    num_executions = 10
    latencies = []

    print(f"  Performing {num_executions} test calls to get_temp1...")

    for i in range(num_executions):
        try:
            start_time = time.perf_counter()
            temp = Bridge.call("get_temp1")
            end_time = time.perf_counter()

            duration_ms = (end_time - start_time) * 1000
            latencies.append(duration_ms)

            if temp is not None and not math.isnan(temp):
                print(f"  Execution {i+1:2d}: Latency: {duration_ms:6.2f} ms, Temp: {temp:.2f} °C")
            else:
                print(f"  Execution {i+1:2d}: Latency: {duration_ms:6.2f} ms, Temp: Invalid Reading")

            time.sleep(1)
        except Exception as e:
            print(f"  Error during get_temp1 execution {i+1}: {e}")
            continue

    if not latencies:
        print("  Temperature Latency test failed: No successful calls.")
        print("------------------------------------")
        return

    min_latency = min(latencies)
    max_latency = max(latencies)
    avg_latency = sum(latencies) / len(latencies)

    print("\n  --- Temp Latency Results ---")
    print(f"  Min Latency: {min_latency:.2f} ms")
    print(f"  Max Latency: {max_latency:.2f} ms")
    print(f"  Avg Latency: {avg_latency:.2f} ms")
    print("----------------------------")
    time.sleep(1)

def loop():
    """
    This function is called repeatedly by the App framework.
    """
    print("Requesting temperatures...")
    try:
        temp1 = Bridge.call("get_temp1")
        if temp1 is not None and not math.isnan(temp1):
            print(f"  THERMO1: {temp1:.2f} °C")
        else:
            print("  THERMO1: Invalid reading")
    except Exception as e:
        print(f"  Error reading THERMO1: {e}")

    time.sleep(0.2)

    try:
        temp2 = Bridge.call("get_temp2")
        if temp2 is not None and not math.isnan(temp2):
            print(f"  THERMO2: {temp2:.2f} °C")
        else:
            print("  THERMO2: Invalid reading")
    except Exception as e:
        print(f"  Error reading THERMO2: {e}")

    time.sleep(0.2)

    try:
        temp3 = Bridge.call("get_temp3")
        if temp3 is not None and not math.isnan(temp3):
            print(f"  THERMO3: {temp3:.2f} °C")
        else:
            print("  THERMO3: Invalid reading")
    except Exception as e:
        print(f"  Error reading THERMO3: {e}")

    print("-" * 20)
    time.sleep(5)


# Run the latency tests first.
run_raw_latency_test()
run_temp_latency_test()

# Then, start the main application loop.
App.run(user_loop=loop)
