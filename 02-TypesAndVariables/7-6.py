###
# The speed of vehicles on a highway in Poland
# must be between 40 and 140 km/h.
#
speed = int(input('Enter vehicle speed: '))
speed_ok = 40 <= speed <= 140
print(f'Speed is valid: {speed_ok}')
