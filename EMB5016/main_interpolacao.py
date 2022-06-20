import matplotlib.pyplot as plt
import numpy as np
from int_pol import *

n=10

x=np.random.choice(range(2*n),n+1,replace=False)
y=np.random.randint(low=-10,high=10,size=n+1)
#y=np.random.randint(low=-10,high=10,size=n+1)

n=len(x)

print("==========")
print("SISTEMA LINEAR:")

f=int_pol_lin(x,y)

for i in range(n):
    print("x="+str(x[i]))
    print("y="+str(y[i]))
    print("f(x)="+str(f(x[i])))
    print("\n")
#end for

print("==========")
print("LAGRANGE:")
l=lagrange(x,y)

for i in range(n):
    print("x="+str(x[i]))
    print("y="+str(y[i]))
    print("f(x)="+str(l(x[i])))
    print("\n")
#end for

print("==========")
print("GREGORY-NEWTON:")
g=gregory_newton(x,y)

for i in range(n):
    print("x="+str(x[i]))
    print("y="+str(y[i]))
    print("g(x)="+str(g(x[i])))
    print("\n")
#end for

dom=np.arange(np.min(x),np.max(x),0.01)

ran=dom.copy()

for i in range(np.shape(ran)[0]):
    ran[i]=g(dom[i])
#end for

xx=[]
yy=[]
for i in range(len(x)):
    xx+=[x[i]]
    yy+=[y[i]]
#end for
#plt.pyplot.plot(dom, ran)
plt.pyplot.plot(dom,ran)
plt.pyplot.scatter(x,y,marker='x')
plt.pyplot.show()
