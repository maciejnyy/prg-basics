import time
t = int(input('Enter time in seconds: '))
while t > 0:
    if t == 5: print('five')
    elif t == 4: print('four')
    elif t == 3: print('three')
    elif t == 2: print('two')
    elif t == 1: print('one')
    else: print(t)
    time.sleep(1)
    t -= 1
print('zero')
