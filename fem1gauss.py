import sympy 
from sympy import *
import pprint
import matplotlib.pyplot as plt

x=sympy.symbols('x')

"Domain Data"

a=0
b=1


"Domain descomposition (uniform mesh)"

n=5 #Number of elements
h=(b-a)/n #element length

print('element length: h=' , h)


nodos=[] #Mesh node vector
for i in range(n+1):
    i=a+h*i
    nodos.append(i)

print(nodos)
print(len(nodos))

def phi(i,x):
    return sympy.Piecewise((0, x<nodos[i-1]),
    ((x-nodos[i-1])/(nodos[i]-nodos[i-1]),x<=nodos[i]),
    ((nodos[i+1]-x)/(nodos[i+1]-nodos[i]),x<=nodos[i+1]),
    (0,x> nodos[i+1]))


print(phi(2,x))

"Calculo de las derivadas"

def deriv(i,x):
    return sympy.diff(phi(i,x),x)


print(deriv(2,x))


"integral por cuadratura de gauss"

def mult(i,x):
    return (deriv(i+1,x)*deriv(i+1,x))


def intgauss(i,x):
    return ((nodos[i+1]-nodos[i])/2)*((w*mult(p1)+w*mult(p2)))