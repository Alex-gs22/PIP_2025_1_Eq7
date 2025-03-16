cadena = "3+5/2"
print(eval(cadena))

import math

cadena = "math.pow(2,3)"
print(eval(cadena))

x =[i for i in range(-10, 10, 1)]
y = [eval("math.pow(i,2)") for i in x]
print(y)

from matplotlib import pyplot as plt
plt.plot(x,y)
plt.show()