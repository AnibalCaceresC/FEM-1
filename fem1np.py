import numpy
import matplotlib

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

"creación de las funciones a trozos"

x=numpy.linspace(a,b)
for i in range (1, len(Nodos)-2, 1):
    def phi(i,x):
        return numpy.piecewise(x, [x<Nodos[i-1], x<Nodos[i], x<Nodos[i+1], x>Nodos[i+1]],[lambda x:0, lambda x:(x-Nodos[i-1])/(Nodos[i]-Nodos[i-1]), lambda x:(Nodos[i+1]-x)/(Nodos[i+1]-Nodos[i]), lambda x: 0])



print(phi(2,x))



