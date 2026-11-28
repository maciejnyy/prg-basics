from thermometer import Thermometer

def main():
    t = Thermometer()
    t.turn_on()
    t.measure()
    t.display()
    t.turn_off()

if __name__ == "__main__":
    main()
