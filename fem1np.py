import numpy as np
import matplotlib as mpl

"Domain data"
a=0
b=1

"Domain decomposition (uniform mesh)"
n=6 #Number of elements 
h=(b-a)/n #element length
np.set_printoptions(precision=2,suppress=True)
print('element length: h=',f"{h:.2f}","\n") #https://blog.teclado.com/python-formatting-numbers-for-printing/

nodos=[] #Mesh node vector 
for i in range(n+1):
    i=a+h*i
    nodos.append(i)

#print("Node list: ",nodos)

Nodos= np.array(nodos) #conversion to array of nodes
print("Node numpy-array: ",Nodos, "\n")


#https://www.pythonpool.com/numpy-piecewise/
"creación de las funciones a trozos"

x=np.linspace(a,b)
for i in range (1, len(Nodos)-2, 1):
    def phi(i,x):
        return np.piecewise(x, [x<Nodos[i-1], x<Nodos[i], x<Nodos[i+1], x>Nodos[i+1]],[lambda x:0, lambda x:(x-Nodos[i-1])/(Nodos[i]-Nodos[i-1]), lambda x:(Nodos[i+1]-x)/(Nodos[i+1]-Nodos[i]), lambda x: 0])



print(phi(2,x))



