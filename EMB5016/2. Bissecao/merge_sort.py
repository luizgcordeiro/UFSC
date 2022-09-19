import numpy as np
import time

def merge(L,R):
    '''
    Faz um merge ordenado das listas L[p:q] e L[q+1:r].
    '''
    X=[]
    i=0
    j=0
    while i<len(L) and j<len(R):
        if L[i]<R[j]:
            X.append(L[i])
            i+=1
        else:
            X.append(R[j])
            j+=1
        #end if-else
    #end while

    return X+L[i:]+R[j:]
#end def

def merge_sort(A):
    if len(A)<=1:
        return A
    else:
        mid=len(A)//2
        L=merge_sort(A[:mid])
        R=merge_sort(A[mid:])
        return merge(L,R)
    #end if-else
#end def

start=time.time()
A=list(np.random.randint(low=-10,high=10,size=1000000000))
end=time.time()

print(f"Tempo: {start-end} segundos")