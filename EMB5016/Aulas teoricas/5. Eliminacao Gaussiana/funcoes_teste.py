import numpy as np
import escalonamento

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

    return type(A[0,0])(prod_diag(escalonamento.triangulariza(A)))
#end def

##########################################
##########################################
##########################################
##########################################
##########################################

def inversivel(m,li=10):
    '''Criar matriz inversível aleatória com entradas inteiras

    Parâmetros
    ----------
    m: ordem da matriz a ser criada
    li (opcional): limite do valor absoluto das entradas da matriz a ser criada

    Saída
    ----------
    Matriz inversível mxm. Tipo numpy.array, entradas float.'''

    if (abs(li)<1) | (m<1):
        print("Parâmetros inválidos.")
        return
    #end if

    A=np.random.randint(low=-li,high=li,size=(m,m))

    while abs(determinante(A))<.5:
        A=np.random.randint(low=-li,high=li,size=(m,m))
    #end while

    A=np.array(A).astype(float)

    return A
#end def

##########################################
##########################################
##########################################
##########################################
##########################################

def unimodular(m,li=10):
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
        L[i,i]=np.random.choice([1,-1])
        U[i,i]=np.random.choice([1,-1])
        for j in range(i+1,m):
            L[i,j]=0
            U[j,i]=0
        #end for
    #end for

    #Troca primeira linha de L com alguma outra
    p=np.random.choice(list(range(m)))
    x=L[0,:].copy()
    L[0,:]=L[p,:]
    L[p,:]=x

    #Troca primeira coluna de L com alguma outra
    p=np.random.choice(list(range(m)))
    x=U[:,0].copy()
    U[:,0]=U[:,p]
    U[:,p]=x

    return np.matrix(L)*U.astype(float)
#end def

##########################################
##########################################
##########################################
##########################################
##########################################

def random_ref(m,n,li=10,verbose=False):
    '''
    Cria uma matriz escalonada inteira aleatória.

    Parametros obrigatorios
    ----------
    m , n : inteiros positivos
        Ordem da matriz

    Parametros opcionais
    ----------
    li : inteiro, opcional.
        Controle das entradas da matriz a ser criada
    verbose : Boolean
        Imprimir informações intermediárias

    Saida
    ----------
    random_escalonada : array-like de dimensao 2.
        Uma matriz do tipo numpy.array, completamente escalonada, com entradas
        inteiras (tipo float), de ordem mxn.
    '''
    A=np.random.randint(low=-li,high=li+1,size=(m,n))
    
    if verbose:
        print("Primeiro, criamos uma matriz {m}x{n}\n\
        aleatória, que depois transformaremos em uma matriz escalonada.")
        print("A=")
        print(A)
    #end if

    #Escolha o número de pivôs
    numero_de_pivos=np.random.choice(range(np.min([m,n])))+1
    #Posições de pivôs
    posicoes_pivos=merge_sort(np.random.choice(list(range(n)),size=numero_de_pivos,replace=False))

    if verbose:
        print(f"Vamos utilizar {numero_de_pivos} pivos.")
        print(f"Posicoes dos pivos: {posicoes_pivos}")

    #Vamos fazer essas serem de fato as posições de pivôs
    for i in range(numero_de_pivos):
        #Cancela entradas à esquerda do i-ésimo pivô
        for j in range(posicoes_pivos[i]):
            A[i,j]=0
        #Cancela entradas acima e abaixo do pivô
        for j in range(m):
            A[j,posicoes_pivos[i]]=0

        #Normaliza o pivô
        A[i,posicoes_pivos[i]]=1
        #end if-else
        if verbose:
            print(f"Arrumando o {i}-esimo pivô:")
            print(A)
        #end for
    #end for

    for i in range(numero_de_pivos,m):
        for j in range(n):
            A[i,j]=0
        #end for
    #end for
    if verbose:
        print("Cancelando as linhas abaixo dos pivos:")
        print(A)
    return A.astype(float)
#end def

#############################################
#############################################
#############################################
#############################################
#############################################
#############################################

def merge_sort(x):
    '''Merge.

    Parâmetros
    ----------
    x: lista desordenada.

    Saída
    ----------
    lista x ordenada por merge sort.'''

    if len(x)<2:
        return x
    else:
        meio=int(len(x)/2)
        return merge_sort_merge(merge_sort(x[:meio]),merge_sort(x[meio:]))
#end def

def merge_sort_merge(x,y):
    '''Concatenação ordenada de listas ordenadas.

    Parâmetros
    ----------
    x: lista ordenada
    y: lista ordenada

    Saída
    ----------
    Lista ordenada que contém as entradas de x e de y.'''

    #i,j: entradas de x e y sendo comparadas
    i,j,lenx,leny=0,0,len(x),len(y)
    l=[]
    while ((i<lenx) & (j<leny)):
        if x[i]<y[j]:
            l.append(x[i])
            i+=1
        else:
            l.append(y[j])
            j+=1
        #end if-else
    #end while

    l.extend(x[i:])
    l.extend(y[j:])
    return l
#end def

##########################################
##########################################
##########################################
##########################################
##########################################



##########################################
##########################################
##########################################
##########################################
##########################################

##########################################
##########################################
##########################################
##########################################
##########################################
