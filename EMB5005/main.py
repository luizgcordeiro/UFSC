import numpy as np
import time

from functions import *

X=np.random.randint(low=-3,high=3,size=3)
print("X="+str(X))

n=np.array([0,0,0])

while norm(n)<.1:#Faz enquanto a distance de X à reta r for zero
    n=np.random.randint(low=-3,high=3,size=3)
#end while

m=np.array([0,0,0])

while norm(prod_vec(n,m))<.1:#Faz enquanto a distance de X à reta r for zero
    m=np.random.randint(low=-3,high=3,size=3)
#end while



print("X="+str(X))

a=n[0]
b=n[1]
c=n[2]
d=-dot_product(n,X)

print(a)
print(b)
print(c)
print(d)

at=m[0]
bt=m[1]
ct=m[2]
dt=-dot_product(m,X)

print(at)
print(bt)
print(ct)
print(dt)

print("dist(P,pi)=")
print(expression_dist_plane(a,b,c,d))
print("dist(P,nu)=")
print(expression_dist_plane(at,bt,ct,dt))