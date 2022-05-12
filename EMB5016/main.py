from escalonamento import *

n=4
A=np.random.randint(low=-10,high=10,size=(n,n+1))

print(A)

X=escalona(A,verbose=False)[0]

print(A[:,0:n]*X[:,n])
