import numpy as np
import Escalonamento

def prod_diag(A):
    '''Produto dos elementos diagonais de uma matriz.

    Parâmetros
    ----------
    A: array_like do numpy

    Saída
    ----------
    Produto dos elementos da diagonal de A.'''

    p=1
    shape=np.shape(A)
    n=min(shape[0],shape[1])

    for i in range(n):
        p*=A[i,i]
    #end for

    return p
#end def

##########################################
##########################################
##########################################
##########################################
##########################################

def determinante(A):
    '''Determinante de uma matriz quadrada.

    Parâmetros
    ----------
    A: matriz numpy.matrix

    Saída
    ----------
    Determinante da matriz A.'''

    return type(A[0,0])(prod_diag(escal.triangulariza(A)))
#end def

##########################################
##########################################
##########################################
##########################################
##########################################

def criar_matriz_inversivel(m,li=10):
    '''Criar matriz inversível aleatória com entradas inteiras

    Parâmetros
    ----------
    m: ordem da matriz a ser criada
    li (opcional): limite do valor absoluto das entradas da matriz a ser criada

    Saída
    ----------
    Matriz inversível mxm. Tipo numpy.matrix, entradas float.'''

    if abs(li)<1 || m<1:
        print("Parâmetros inválidos.")
        return
    #end if

    A=np.random.randint(low=-li,high=li,size=(m,m))

    while abs(determinante(A))<.5:
        A=np.random.randint(low=-li,high=li,size=(m,m))
    #end while

    A=np.matriz(A).astype(float)

    return A
#end def

##########################################
##########################################
##########################################
##########################################
##########################################

def criar_matriz_unimodular(m,li=10):
    '''Criar matriz unimodular (inteira com inversa inteira) aleatória.

    Parâmetros
    ----------
    m: ordem da matriz a ser criada
    li (opcional): controle das entradas da matriz a ser criada

    Saída
    ----------
    Matriz unimodular mxm com entradas float.'''

    L=np.random.randint(low=-li,high=li,size=(m,m))
    U=np.random.randint(low=-li,high=li,size=(m,m))

    for i in range(m):
        L[i,i]=random.choice([1,-1])
        U[i,i]=random.choice([1,-1])
        for j in range(i+1,m):
            L[i,j]=0
            U[j,i]=0
        #end for
    #end for

    #Troca primeira linha de L com alguma outra
    p=random.choice(list(range(m))
    x=L[0,:].copy()
    L[0,:]=L[p,:]
    L[p,:]=x

    #Troca primeira coluna de L com alguma outra
    p=random.choice(list(range(m))
    x=U[:,0].copy()
    U[:,0]=U[:,p]
    U[:,p]=x


    return np.matrix(L*U).astype(float)
#end def
