# uno-q-max31855

A sample project that demonstrates how to interface with three MAX31855 thermocouple amplifiers using an Arduino and a Python host application. This project showcases the communication bridge between the Arduino sketch and the Python script, and includes latency tests to measure the performance of this communication.

## Project Structure

- **sketch/**: Contains the Arduino code.
  - `sketch.ino`: The main Arduino sketch that reads data from the MAX31855 sensors.
  - `sketch.yaml`: Configuration file for the Arduino sketch, specifying libraries and platforms.
- **python/**: Contains the host-side Python application.
  - `main.py`: The Python script that communicates with the Arduino, requests temperature data, and runs latency tests.
- **app.yaml**: The main configuration file for the application.

## Functionality

The `uno-q-max31855` application performs the following functions:

1.  **Temperature Reading**: The Arduino sketch reads temperature data from three separate MAX31855 thermocouple amplifiers.
2.  **Host Communication**: The Python script communicates with the Arduino via a software bridge to request and receive temperature data.
3.  **Latency Testing**: The Python script includes two latency tests to measure the performance of the communication bridge:
    - **Raw Latency Test**: Measures the round-trip time of a simple `ping` call to the Arduino.
    - **Temperature Latency Test**: Measures the round-trip time of a `get_temp1` call to the Arduino, which includes the time taken to read the sensor data.

## Latency Functions

The `python/main.py` script includes the following latency test functions:

### `run_raw_latency_test()`

This function measures the raw round-trip latency of a call to the Arduino. It sends a `ping` command and measures the time until a response is received. This test is useful for understanding the baseline overhead of the communication bridge.

### `run_temp_latency_test()`

This function measures the latency of calling `get_temp1` on the Arduino. This test includes the time taken for the Arduino to read the temperature from the MAX31855 sensor and send it back to the Python script. This provides a more realistic measure of the application's performance.

## How to Use

Prerequistes:

1. You have installed Arduino-App-Lab AND Arduino-IDE (version 2.3.7)
2. The Uno Q is set up and connected to the same network as your laptop / workstation 
3. You can SSH into your Uno Q board, you have a USB connection to the board as well.
4. You have setup your github ssh access on your Uno-q (Process Documentation: https://docs.github.com/en/authentication/connecting-to-github-with-ssh)

### Step 1

Open a Terminal and SSH into your board. Something like this:
````
ssh arduino@<your board's name>
````
Once logged into the board, arduino-app-lab user defined application file systems are located in: /home/arduino/ArduinoApps

using git, you can clone the repo to your local uno-q board.

The Python script will first run the latency tests and print the results to the console. It will then enter a loop, requesting and printing the temperature from each of the three thermocouples every 5 seconds.
