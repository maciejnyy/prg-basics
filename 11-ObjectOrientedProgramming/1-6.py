class Phone:
    def __init__(self, brand, model, battery_level=100):
        self.brand = brand
        self.model = model
        self.battery_level = battery_level
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print(f"{self.brand} {self.model} is now ON.")

    def make_call(self, number):
        if self.is_on and self.battery_level > 0:
            print(f"Calling {number}...")
            self.battery_level = max(0, self.battery_level - 5)
        else:
            print("Cannot make a call. Phone is off or battery is empty.")

    def charge(self, amount):
        self.battery_level = min(100, self.battery_level + amount)
        print(f"Battery charged to {self.battery_level}%.")

    def display_info(self):
        status = "ON" if self.is_on else "OFF"
        print(f"Phone: {self.brand} {self.model}, Status: {status}, Battery: {self.battery_level}%")

if __name__ == "__main__":
    my_phone = Phone("Samsung", "Galaxy S23", 80)
    my_phone.turn_on()
    my_phone.make_call("555-123-456")
    my_phone.charge(15)
    my_phone.display_info()
