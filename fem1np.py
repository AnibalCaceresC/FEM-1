import numpy

"ingresamos los valores requeridos"

a=0
b=1
n=6

"calculo de la longitud (h) de los elementos"

h=(b-a)/(n-1)

print('Tamaño de los elementos h=')
print(h)

"Generacion de la lista de nodos"

nodos=[]
for i in range(n):
    i=a+h*i
    nodos.append(i)

print(nodos)

Nodos= numpy.array(nodos) #convertimos la lista de nodos en array


print(Nodos)

print(Nodos[0])

