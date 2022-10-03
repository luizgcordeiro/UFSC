import numpy as np

def pivot_partial (x) : return np.argmax(abs(x))

def ref(A,tol=None,pivot=pivot_partial,verbose=False):
    '''Escalona parcialmente uma matriz A.

    Parametros obrigatorios
    ----------
    A : Array-like de dimensão 2
        Matriz a ser escalonada parcialmente.

    Parametros opcionais
    ----------
    tol : Float, opcional
        Tolerancia numerica
        Padrao 2^(-30) vezes a maior entrada de A em valor absoluto.
    verbose : Boolean, opcional
        Imprimir informaçoes intermediarias
    pivot : Funcao, opcional
        Regra de pivoteamento.
        Deve ser uma funcao que toma uma lista ou array-like nao-vazia
        e retorna um indice para essa lista. Por padrao, utiliza uma
        funcao que retorna o indice de maior valor absoluto para fazer
        pivoteamento parcial.

    Saida
    ----------
    Lista [T,P], em que
    T : Forma escalonada de A.
    P : lista com os indices das colunas que tem os pivôs de T.'''

    #Faz cópias
    T=np.array(A).astype(float)
    posicao_pivos = []
    #Grava o tamanho
    n_linhas , n_colunas = np.shape(T)
    #Vê quantos pivôs já foram achados
    n_pivos=0

    if tol==None:
      tol=2**(-30) * np.max(abs(T))
    #end if

    #Linhas na qual trabalharemos
    j=0

    if verbose:
      print("Vamos escalonar parcialmente a matriz")
      print(T)
    #end if

    num_op=0
    while (j<n_colunas and n_pivos<n_linhas):
        if verbose:
          print("=====")
          print(f"Vamos pivotear a coluna {j}.")
        #end if

        #Encontra o pivô
        p=pivot(T[n_pivos:,j])+n_pivos
        if abs(T[p,j])>tol:
            #Encontramos um pivô.
            #Troca linhas caso necessário
            if p != n_pivos:

                for k in range(j,n_colunas):
                  temp=T[p,k]
                  T[p,k]=T[n_pivos,k]
                  T[n_pivos,k]=temp
                #end for
                if verbose:
                  print(f"Precisamos trocar a linha {n_pivos} com a linha {p}.")
                  print(T)
                #end if

                p=n_pivos
            #end if

            #Pivoteia abaixo
            for k in range(p+1,n_linhas):
                if abs(T[k,j])>tol:
                    multiplicador=T[k,j]/T[p,j]
                    num_op+=1
                    T[k,j+1:]=T[k,j+1:]-multiplicador*T[p,j+1:]
                    num_op+=n_colunas-1-j
                    T[k,j]=0
                #end if
            #end for
            if verbose:
              print("Aniquila as entradas abaixo:")
              print(T)
            #end if

            #Conta o pivô a mais
            n_pivos+=1
            posicao_pivos.append(j)
        else:
            if verbose:
              print(f"A coluna {j} nao tem pivo.")
        #end if
        #passa pra próxima coluna
        j+=1
    #end while

    if verbose:
        print(f"Numero de operacoes: {num_op}")
    #end if-else
    return [T,posicao_pivos]
#end def


def retrossub(A,pospiv=[],tol=None,verbose=False):
    """Retrossubstituição.

    Parametros obrigatorios
    ----------
    A : Array-like de dimensao 2
        Matriz parcialmente escalonada

    Parametros opcionais
    ----------
    pospiv : Array-like de dimensao 1
        Lista com as posições dos pivôs de A
    tol : Float, opcional
        Tolerancia numerica
        Padrao 2^(-30) vezes a maior entrada de A em valor absoluto.
    verbose : Boolean, opcional
        Imprimir informaçoes intermediarias

    Saída
    ----------
    Lista [R,P], em que:
    R : Forma completamente escalonada de A.
    P : Lista com posição dos pivôs de A."""

    #Faz as cópias usuais para evitar problemas
    R=np.array(A).astype(float)
    m,n=np.shape(R)

    if tol==None:
        tol=2**(-30) * np.max(abs(R))
    #end if

    if verbose:
        print("Vamos fazer retrosubstituição na matriz")
        print(A)
    #end if

    #caso nao saibamos as posições dos pivos, temos que encontrá-los
    if pospiv==[]:
        if verbose:
            print('Nâo foi dada a posição dos pivôs da matriz.')
            print('Vamos encontrá-los:')
        #end if
        i=0
        j=0
        while (i<m):
            while abs(R[i,j])<tol and j<n:
                j+=1
            #end while

            if j==n:
                break
            else:
                pospiv.append(j)
                i+=1
            #end if-else
        #end while
    #end if

    if verbose:
        print(f"Os pivôs estao nas colunas {pospiv}")
        print()
    #end if
    numero_de_pivos=len(pospiv)
    for i in range(numero_de_pivos-1,-1,-1):
        if verbose:
            print('=====')
        #end if
        #Normaliza o pivô, caso necessário
        if abs(R[i,pospiv[i]]-1)>tol:
            R[i,pospiv[i]+1:]/=R[i,pospiv[i]]
            R[i,pospiv[i]]=1
            if verbose:
                print(f"Vamos normalizar o pivo na linha {i}.")
                print(R)
                print()
            #end if
        #end if


        #Aniquila as entradas acima
        if verbose:
            print(f"Vamos aniquilar as entradas acima do pivo na posição ({i},{pospiv[i]}).")
        #end if
        for k in range(i-1,-1,-1):
            R[k,pospiv[i]+1:]-=R[k,pospiv[i]]*R[i,pospiv[i]+1:]
            R[k,pospiv[i]]=0
        #end for

        if verbose:
            print(R)
        #end if
    #end for

    return [R,pospiv]
#end function

def rref(A,tol=None,pivot=pivot_partial,verbose=False):
    """
    Escalonamento completo.

    Parametros obrigatorios
    ----------
    A : Array-like de dimensao 2
        Matriz a ser completamente escalonada.

    Parametros opcionais
    ----------
    pivot : Funcao, opcional
         Regra de pivoteamento.
         Deve ser uma funcao que toma uma lista ou array-like nao-vazia
         e retorna um indice para essa lista. Por padrao, utiliza uma
         funcao que retorna o indice de maior valor absoluto para fazer
         pivoteamento parcial.
    pospiv : Array-like de dimensao 1, opcional
        Lista com as posições dos pivôs de A
    tol : Float, opcional
        Tolerancia numerica
        Padrao 2^(-30) vezes a maior entrada de A em valor absoluto.
    verbose : Boolean, opcional
        Imprimir informaçoes intermediarias
    
    Saida
    ----------
    Lista [E,P], em que:
    E: Forma completamente escalonada de A.
    P: Lista com posição dos pivôs de A.
    """

    T=ref(A,tol=tol,pivot=pivot,verbose=verbose)
    
    return retrossub(T[0],pospiv=T[1],tol=tol,verbose=verbose)
#end def