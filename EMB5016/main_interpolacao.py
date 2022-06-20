import numpy as np
from int_pol import *

n=8

x=list(range(n+1))
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
    print("f(x)="+str(g(x[i])))
    print("\n")
#end for