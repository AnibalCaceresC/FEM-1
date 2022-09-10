import sympy 
from sympy import *
import pprint

x=sympy.symbols('x')

"Ingresamos los valores requeridos"

a=0
b=1
n=6

"Calculo de la longitud (h) de los elementos"

h=(b-a)/(n-1)

print('Tamaño de los elementos h=')
print(h)

"Generación de la lista de nodos"

nodos=[]
for i in range(n):
    i=a+h*i
    nodos.append(i)

print (nodos)


"Creacion de las funciones a trozos"

for i in range (1,len(nodos)-2,1):
    def phi(i,x):
        return sympy.Piecewise((0, x<nodos[i-1]),
                           ((x-nodos[i-1])/(nodos[i]-nodos[i-1]), x<=nodos[i]),
                           ((nodos[i+1]-x)/(nodos[i+1]-nodos[i]), x<=nodos[i+1]),
                           (0, x>nodos[i+1]))


print(phi(2,x))

"Calculo de las derivadas"

for i in range(1,len(nodos)-2,1):
    def deriv(i,x):
        return sympy.diff(phi(i,x),x)


print(phi(2,x))

"Calculo de la matriz de carga K"

K=zeros(len(nodos)-2, len(nodos)-2)

for i in range(0, len(nodos)-2,1):
    for j in range(0, len(nodos)-2, 1):
        K[i,j]=sympy.integrate(deriv(i+1,x)*deriv(j+1,x),(x, nodos[i], nodos[i+2]))


print('la matriz de carga k es')

pprint.pprint(K)







