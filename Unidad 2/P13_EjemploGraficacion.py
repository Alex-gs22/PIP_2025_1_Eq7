# y = mx + b

x = [i for i in range (-5,5+1,1)]
print(x)

m = 5
b = 2

y = [i*m+b for i in x]

print(y)

from matplotlib import pyplot as plt

plt.plot(x,y, marker = "x")
plt.show()

#Practica Numero 4