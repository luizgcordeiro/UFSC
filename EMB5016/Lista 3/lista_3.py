import numpy as np

#Resolução da Lista de Exercícios 3

#Exercício 1

def sin(x):
    #Implementacao da funcao sin(x) por serie de Taylor
    soma=0
    soma_ant=-1
    termo=x
    n=0
    while soma!=soma_ant:
        soma_ant=soma
        soma+=termo
        n+=1
        termo=-termo*(x/(2*n))*(x/(2*n+1))
    #end while

    return soma
#end sin

def cos(x):
    #Implementacao da funcao cos(x) por serie de Taylor
    soma=0
    soma_ant=-1
    termo=1
    n=0
    while soma!=soma_ant:
        soma_ant=soma
        soma+=termo
        n+=1
        termo=-termo*(x/(2*n-1))*(x/(2*n))
    #end while

    return soma
#end cos

#Exercício 2

def invsqrt(x):
    #Implementacao da x^(-1/2) por serie de Taylor baseada em 1
    if x<=1:
        soma=0
        soma_ant=-1
        termo=1
        n=0
        while soma!=soma_ant:
            soma_ant=soma
            soma+=termo
            n+=1
            termo=-termo*((2*n-1)/(2*n))*(x-1)
        #end while

        return soma
    else:
        return 1/invsqrt(1/x)
    #end if-else
#end def

#Exercício 3

def reverter(L):
    '''Reverte a propria lista L'''
    l=len(L)//2
    for i in range(l):
        x=L[i]
        L[i]=L[-1-i]
        L[-1-i]=x
    #end for
    return L
#end def


def reversa(L):
    '''Cria uma copia invertida de L'''
    l=len(L)
    A=[None]*l
    for i in range(l):
        A[i]=L[-1-i]
    #end for
    return A
#end def
L=np.random.randint(low=-10,high=10,size=20)

#Exercício 4

def ordena(L):
    '''Cria uma copia ordenada da lista L'''
    #Merge-s ort iterativo
    A=L.copy()
    n=len(A)
    l=1 #tamanho dos blocos a serem merged

    ###print(f"=====\nLista a ser ordenada: A={A}")
    while (l<n):
        ###print(f"=====\nTamanho dos blocos: {l}")
        k=0
        while k<n:
            p=min(k+l,n)
            q=min(k+2*l,n)
            L=A[k:p].copy()
            R=A[p:q].copy()
            ###print(f"-----\nMerge A[{k},{p})={L} e A[{p},{q})={R}")
            i=0
            j=0
            s=k

            #Faz o merge
            while (i<p-k) and (j<q-p):
                ###print(f"  Nova lista: {A[k:s]}")
                ###print(f"  A[{k+i},{p})={L[i:]}")
                ###print(f"  A[{p+j},{q})={R[j:]}")
                if L[i]<R[j]:
                    ###print("  A primeira entrada da primeira lista e menor")
                    A[s]=L[i]
                    i+=1
                else:
                    ###print("  A primeira entrada da segunda lista e menor")
                    A[s]=R[j]
                    j+=1
                #end if-else
                s+=1
                ###print("  ...")
            #end while
            ###print(f"  Nova lista: {A[k:s]}")
            ###print(f"  A[{k+i},{p})={L[i:]}")
            ###print(f"  A[{p+j},{q})={R[j:]}")

            #Cola os restos
            ###if (i<p-k):
                ###print("\n  Vamos colar a primeira lista no novo resultado.")
            ###elif (j<q-p):
                ###print("\n  Vamos colar a segunda lista no novo resultado.")
            #end if
            while (i<p-k):
                A[s]=L[i]
                i+=1
                s+=1
            #end while
            while (j<q-p):
                A[s]=R[j]
                j+=1
                s+=1
            #end while

            ###print(f"Resultado: A[{k},{q})={A[k:q]}")
            k+=2*l
        #end while
        l*=2
    #end while

    return A
#end def

#Exercício 5

def pot2(n):
    '''2^n'''
    if n<1:
        return 1/pot2(-n)
    else:
        p=1
        for i in range(n):
            p*=2
        #end for
        return p
    #end if-else
#end def

def logaritmo_base2(x):
    '''Calcula o logaritmo em base 2 de x'''
    if x==1:
        return 0
    # Encontra o inteiro l tal que 2^l<=x<2^(l+1)

    l=0
    pot2l=1
    if x>1:
        while 2*pot2l<=x:
            l+=1
            pot2l*=2
        #end while
    else:
        while 2*x<pot2l:
            l-=1
            pot2l/=2
        #end while
        l-=1
        pot2l/=2
    #end if-else

    #Atualiza x=x/2^l
    x/=pot2l

    #Entra na iteracao. O arredondamento e feito por baixo, entao em algum momento estabiliza
    pot2m53=pot2(-53)
    b=1/2
    while (b>=pot2m53*abs(l)):
        if (x*x<2):
            x*=x
        else:
            x*=x/2
            l+=b
        #end if-else
        b/=2
    #end while

    return l
#end def

#Exercício 6

def Collatz(x):
    j=0
    while x!=1:
        if x%2==0:
            x//=2
        else:
            x=3*x+1
        #end if-else
        j+=1
    #end while
    return j
#end def