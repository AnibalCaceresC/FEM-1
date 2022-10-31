import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
import numpy.linalg as la 

def phi(i,x,nodVec):
    n=len(nodVec)-1
    if i==0:
        def tramo1(x):
            return (nodVec[1]-x)/(nodVec[1]-nodVec[0])
        return np.piecewise(x,[(nodVec[0]<=x) & (x<=nodVec[1])],[lambda x:tramo1(x)]) 
    elif i==n:
        def tramo1(x):
            return (x-nodVec[n-1])/(nodVec[n]-nodVec[n-1])
        return np.piecewise(x,[(nodVec[n-1]<=x) & (x<=nodVec[n])],[lambda x:tramo1(x)]) 
    else:
        def tramo1(x):
            return (x-nodVec[i-1])/(nodVec[i]-nodVec[i-1])
        def tramo2(x):
            return (nodVec[i+1]-x)/(nodVec[i+1]-(nodVec[i]))
        return np.piecewise(x,[(nodVec[i-1]<=x) & (x<=nodVec[i]),(nodVec[i]<=x) & (x<=nodVec[i+1])],[lambda x:tramo1(x),lambda x: tramo2(x)])


def dphi(i,x,nodVec):
  n=len(nodVec)-1
  if i==0:
    def tramo(x):
      return -1/(nodVec[1]-nodVec[0])
    return np.piecewise(x,[(nodVec[0]<=x) & (x<=nodVec[1])],[lambda x:tramo(x)])
  elif i==n: 
    def tramo(x):
      return 1/(nodVec[n]-nodVec[n-1])
    return np.piecewise(x,[(nodVec[n-1]<=x) & (x<=nodVec[n])],[lambda x:tramo(x)])
  else:
    def tramo1(x):
            return 1/(nodVec[i]-nodVec[i-1])
    def tramo2(x):
            return -1/(nodVec[i+1]-(nodVec[i]))
    return np.piecewise(x,[(nodVec[i-1]<=x) & (x<=nodVec[i]),(nodVec[i]<=x) & (x<=nodVec[i+1])],[lambda x:tramo1(x),lambda x: tramo2(x)])    



a =-1; b = 1 #Dominio del problema
crearNodosManual = False;        
if (crearNodosManual):
    nodVec = np.array([a,a+0.2,a+0.5,a+0.9,b])
else: 
    N= 10 #Número de nodos
    nodVec=np.linspace(a,b,N) # generando nodos equiespaciados

''' Gráfica de phi(i,x)'''

'''
i=1
x = np.linspace(0,1,200)
y=phi(i,x,nodVec)
plt.grid()
plt.plot(x,y)
plt.plot(nodVec[i],1,'o')
plt.show()
'''

''' Gráfica derivada dphi(i,x)'''


'''
y1=dphi(i,x,nodVec)
plt.grid()
plt.plot(x,y1)
#plt.plot(nodVec[i],1,'o')
plt.show()
'''

''' preguntar por que define una funcion'''


def f(x):
  return np.e**(-100*(x**2))

''' OTRAS FUNCIONES FUENTE'''

#-1
#np.pi**2 * np.sin(np.pi*x)
#np.e**(-100*(x**2))

nDofs = len(nodVec)-2
print("nDofs:\n",nDofs)

''' Cálculo del vector de carga'''
L = np.zeros(nDofs)
for i in range(0,nDofs):
  def aux(x):
    return f(x)*phi(i+1,x,nodVec)

  r=quad(aux,a,b)
  print(r)
  L[i] = r[0]

print("L:\n",L)


''' Cálculo de la matriz de rigidez'''
K = np.zeros((nDofs,nDofs))
for i in range(0,nDofs):
  for j in range(0,nDofs):
    def aux(x):
      return dphi(j+1,x,nodVec)*dphi(i+1,x,nodVec)
    
    r=quad(aux,a,b)
    K[i,j]=r[0]

print("K:\n",K)



U = la.solve(K,L)

def uh(x):
  resp = 0
  for i in range(nDofs):
    resp = resp+U[i]*phi(i+1,x,nodVec)
  return resp

def u(x):
  return np.exp(-100*(x**2))

'''SOLUCIONES DE LAS DISTINTAS FUNCIONES FUENTE'''

#(x*(x-1))/2
#np.sin(np.pi*x)
#np.exp(-100*(x**2))



xx = np.linspace(-1,1,200)
yy = uh(xx)
zz = u(xx)
plt.grid()
p1 = plt.plot(xx,yy,"g")
p2 = plt.plot(xx,zz,"b")
plt.grid()
p1.extend(p2)
plt.show()



