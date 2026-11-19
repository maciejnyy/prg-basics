import matplotlib.pyplot as plt
import math

x = []
y = []

for n in range(0, 361):
    x.append(n)
    y.append(math.sin(math.radians(n)))

plt.plot(x, y)
plt.show()
