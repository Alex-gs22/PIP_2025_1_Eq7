from matplotlib import pyplot as plt
from numpy import sort
import numpy as np
from packaging.markers import Marker

archivo = open("../Archivos/Calificaciones_con_nombre.csv")
contenido = archivo.readlines()

print(contenido)
datos = [i.split(",") for i in contenido]
datos = [[i[0],list(map(int,i[1:]))] for i in datos]
print(datos)

#Calcular el promedio de cada alumno y agregar el resultado
#a la lista asociada al usuario

datos = [[ i[0], i[1], sum(i[1])/len(i[1]) ] for i in datos]
print(datos)

#datos.sort(key = lambda x: x[2])

promedios = [i[2] for i in datos]
nombres = [i[0] for i in datos]

promedioGrupo = sum(promedios)/len(promedios)
referencia = [0 for i in promedios]
vector = np.array(promedios)
desviacion = np.std(vector)
print(promedioGrupo)
print(desviacion)
promedios_std = [(i - promedioGrupo)/desviacion for i in promedios]
print(promedios_std)
plt.plot(nombres, promedios_std, marker = "o")
plt.plot(nombres, referencia, marker = "*")
plt.show()
