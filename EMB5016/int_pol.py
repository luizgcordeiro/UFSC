import escalonamento

def int_pol_lin(x,y):
    n=len(x)-1

    A=np.matrix(np.zeros([n+1,n+1]).astype(float))

    for i in range(n+1):
        A[i,1]=1
    #end for

    for i in range(n+1):
        for j in range(1,n+1):
            A[i,j]=x[i]**j
        #end for
    #end for

    A=escalonamento.escalona(np.concatenate([A,y],axis=1))

    def f(t):
        sum=0
        for i in range(n+1):
            prod=1
            for j in range(n+1):
                if j!=i:
                    prod*=(t-x[i])(x[j]-x[i])
                #end if
            #end for
            sum+=y[i]*prod
        #end for
    #end def

    return f
#end def
