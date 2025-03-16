from matplotlib import pyplot as plt
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

#Investigar como graficar los datos de la lista de datos, listas de comprension
promedios = [i[2] for i in datos]
nombres = [i[0] for i in datos]
print(nombres)
print(promedios)
plt.bar(nombres,promedios)
plt.xlabel('Nombre')
plt.ylabel('Promedio')
plt.ylim(0,12)
plt.show()