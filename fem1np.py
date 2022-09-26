import numpy as np
import matplotlib.pyplot as plt

"Domain data"
a=0
b=1

"Domain decomposition (uniform mesh)"
n=5 #Number of elements 
h=(b-a)/n #element length
np.set_printoptions(precision=6,suppress=True)
print('element length: h=',f"{h:.2f}","\n") #https://blog.teclado.com/python-formatting-numbers-for-printing/

nodos=[] #Mesh node vector 
for i in range(n+1):
    i=a+h*i
    nodos.append(i)

#print("Node list: ",nodos)

Nodos= np.array(nodos) #conversion to array of nodes
print("Node numpy-array: ",Nodos, "\n")

print(len(Nodos))

#https://www.pythonpool.com/numpy-piecewise/
"creación de las funciones a trozos"

x=np.linspace(a,b,10)
print(x)

def phi(i,x):
    if x<Nodos[i-1]:
        return 0
    elif x>=Nodos[i-1] and x<Nodos[i]:
        yy = (x -Nodos[i-1])/(Nodos[i]-Nodos[i-1])
        return yy
    elif x>=Nodos[i] and x<Nodos[i+1]:
        yy = (Nodos[i+1]-x)/(Nodos[i+1]-Nodos[i])
        return yy
    elif x>Nodos[i+1]:
        return 0

phi = np.vectorize(phi)

y = phi(1,x)

plt.plot(x,y)
plt.show

