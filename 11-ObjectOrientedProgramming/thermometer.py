import random

class Thermometer:
    def __init__(self):
        self.is_on = False
        self.temperature = None

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def measure(self):
        if self.is_on:
            self.temperature = round(random.uniform(34.0, 42.0), 1)
        else:
            print("Thermometer is off.")

    def display(self):
        if not self.is_on:
            print("Thermometer is off.")
            return
        if self.temperature is None:
            print("No measurement taken yet.")
            return

        msg = f"Temperature: {self.temperature:.1f}C"
        if self.temperature >= 41.0:
            msg += " (fever) CRITICAL TEMPERATURE!!"
        elif self.temperature >= 37.0:
            msg += " (fever)"
        print(msg)
