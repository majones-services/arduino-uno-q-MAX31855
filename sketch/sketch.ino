
#include <Arduino_RouterBridge.h>
#include "Adafruit_MAX31855.h"

// Thermocouple Pin Definitions
#define MAXDO   3
#define MAXCLK  5
#define MAXCS1  4
#define MAXCS2  6
#define MAXCS3  7

// initialize the Thermocouples
Adafruit_MAX31855 thermo1(MAXCLK, MAXCS1, MAXDO);
Adafruit_MAX31855 thermo2(MAXCLK, MAXCS2, MAXDO);
Adafruit_MAX31855 thermo3(MAXCLK, MAXCS3, MAXDO);

// Helper function to test a thermocouple and print its status
void testThermocouple(Adafruit_MAX31855 &thermocouple, const char* sensorName) {
  delay(100); // Small delay for sensor stability
  double c = thermocouple.readCelsius();
  char buffer[128]; // Buffer to hold the formatted string

  if (isnan(c)) {
    uint8_t e = thermocouple.readError();
    snprintf(buffer, sizeof(buffer), "%s - Thermocouple fault(s) detected!\n", sensorName);
    Monitor.print(buffer); delay(10);

    if (e & MAX31855_FAULT_OPEN) { Monitor.print("  FAULT: Thermocouple is open - no connections.\n"); delay(10); }
    if (e & MAX31855_FAULT_SHORT_GND) { Monitor.print("  FAULT: Thermocouple is short-circuited to GND.\n"); delay(10); }
    if (e & MAX31855_FAULT_SHORT_VCC) { Monitor.print("  FAULT: Thermocouple is short-circuited to VCC.\n"); delay(10); }
  } else {
    // Use snprintf for portable float-to-string conversion with the degree symbol
    snprintf(buffer, sizeof(buffer), "Internal Temp: %s - %.2f °C\n", sensorName, c);
    Monitor.print(buffer); delay(10);
  }
}

double get_temp1() {
  return thermo1.readCelsius();
}

double get_temp2() {
  return thermo2.readCelsius();
}

double get_temp3() {
  return thermo3.readCelsius();
}

// A simple function to test round-trip latency. It does nothing.
void ping() {
  // This function is intentionally empty.
}

void setup() {
    Serial.begin(115200);

    if (!Bridge.begin()) {
        Monitor.print("cannot setup Bridge\n"); delay(10);
    }

    if(!Monitor.begin()){
        Monitor.print("cannot setup Monitor\n"); delay(10);
    }

    Monitor.print("MAX31855 test\n"); delay(10);
    delay(500); // Wait for MAX chips to stabilize

    // Initialize and test each sensor
    Monitor.print("Initializing sensor 1...\n"); delay(10);
    if (!thermo1.begin()) {
        Monitor.print("ERROR initializing sensor 1.\n"); delay(10);
    } else {
        testThermocouple(thermo1, "THERMO1");
    }

    Monitor.print("Initializing sensor 2...\n"); delay(10);
    if (!thermo2.begin()) {
        Monitor.print("ERROR initializing sensor 2.\n"); delay(10);
    } else {
        testThermocouple(thermo2, "THERMO2");
    }

    Monitor.print("Initializing sensor 3...\n"); delay(10);
    if (!thermo3.begin()) {
        Monitor.print("ERROR initializing sensor 3.\n"); delay(10);
    } else {
        testThermocouple(thermo3, "THERMO3");
    }

    // Register methods with the Bridge
    if (!Bridge.provide("get_temp1", get_temp1)) {
        Monitor.print("Error providing method: get_temp1\n"); delay(10);
    }
    if (!Bridge.provide("get_temp2", get_temp2)) {
        Monitor.print("Error providing method: get_temp2\n"); delay(10);
    }
    if (!Bridge.provide("get_temp3", get_temp3)) {
        Monitor.print("Error providing method: get_temp3\n"); delay(10);
    }
    if (!Bridge.provide("ping", ping)) {
        Monitor.print("Error providing method: ping\n"); delay(10);
    }

    Monitor.print("Setup DONE.\n"); delay(10);
}

void loop() {
  // The Bridge library handles incoming requests in the background.
  delay(100);
}
