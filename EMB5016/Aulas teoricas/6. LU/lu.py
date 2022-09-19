import numpy as np

def crout(A):
    B=np.matrix(A.copy()).astype(float)
    n=len(A)
    L=np.matrix(np.zeros([n,n])).astype(float)
    U=np.matrix(np.zeros([n,n])).astype(float)

    for i in range(n):
        U[i,i]=1
    #end for

    for k in range(n):
        for i in range(k,n):
            L[i,k]=B[i,k]-(L[i,:k]*U[:k,k])[0,0]
        #end for

        for j in range(k+1,n):
            U[k,j]=(B[k,j]-(L[k,:k]*U[:k,j])[0,0])/L[k,k]
        #end for
    #end for

    return [L,U]
#end def

def res_tri_inf(L,b):
    x=b.copy()
    n=len(b)

    for i in range(n):
        x[i,0]=(b[i]-(L[i,:i]*x[:i,0])[0,0])/L[i,i]
    #end for

    return x
#end def

def res_tri_sup(U,b):
    x=b.copy()
    n=len(b)

    for i in range(n-1,-1,-1):
        x[i,0]=(b[i]-(U[i,i+1:]*x[i+1:,0])[0,0])/U[i,i]
    #end for

    return x
#end def
