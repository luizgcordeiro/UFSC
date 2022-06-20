import numpy as np
import escalonamento

def int_pol_lin(x,y):
    n=len(x)-1

    A=np.matrix(np.zeros([n+1,n+2]).astype(float))

    for i in range(n+1):
        A[i,0]=1
        A[i,n+1]=y[i]
    #end for

    for i in range(n+1):
        for j in range(1,n+1):
            A[i,j]=x[i]**j
        #end for
    #end for
    
    A=escalonamento.escalona(A)[0]

    def f(t):
        soma=0
        for i in range(n+1):
            soma+=A[i,n+1]*(t**i)
        #end def
        return soma
    return f
#end def

def lagrange(x,y):
    n=len(x)-1

    def f(t):
        sum=0
        for i in range(n+1):
            prod=1
            for j in range(n+1):
                if j!=i:
                    prod*=(t-x[j])/(x[i]-x[j])
                #end if
            #end for
            sum+=y[i]*prod

        #end for

        return sum
    #end def

    return f
#end def


def diferenca_dividida(x,y,k,i):
    if k==0:
        return y[i]
    else:
        return (diferenca_dividida(x,y,k-1,i+1)-diferenca_dividida(x,y,k-1,i))/(x[i+k]-x[i])
    #end if-else
#end def    

def gregory_newton(x,y):
    n=len(x)

    def f(t):
        soma=y[0]
        for k in range(1,n):
            prod=1
            for j in range(k):
                prod*=(t-x[j])
            #end for
            soma+=diferenca_dividida(x,y,k,0)*prod
        #end for

        return soma
    #end def

    return f
#end def
