import numpy as np
import matplotlib.pyplot as plt

x= np.linspace(-10, 2, 15)

y= np.piecewise(x, [x<0,((x>=0)&(x<10)),x>=10], [lambda x:x**2, lambda x: 10-x, lambda x:2*x +3])

print(y)

plt.plot(x,y)
plt.show()


x=np.linspace(a,b)
for i in range (1, len(Nodos)-2, 1):
    def phi(i,x):
        return np.piecewise(x, [x<Nodos[i-1], 
        x<Nodos[i], x<Nodos[i+1], x>Nodos[i+1]],
        [lambda x:0, 
        lambda x:(x-Nodos[i-1])/(Nodos[i]-Nodos[i-1]), 
        lambda x:(Nodos[i+1]-x)/(Nodos[i+1]-Nodos[i]), 
        lambda x: 0])
