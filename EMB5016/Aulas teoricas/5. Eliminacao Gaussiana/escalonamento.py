import numpy as np

def pivot_partial (x) : return np.argmax(abs(x))

def triangulariza(A,tol=None,pivot=pivot_partial,verbose=False,):
    '''Triangulariza uma matriz A.

    Parametros obrigatorios
    ----------
    A : matriz a ser triangularizada.
      Deve ser implementada como uma lista de listas ou uma numpy.array

    Parametros opcionais
    ----------
    tol : Float, opcional
      Tolerancia numerica
      Padrao 2^(-30) vezes a maior entrada de A em valor absoluto.
    verbose : Boolean, opcional
      Imprimir informaçoes intermediarias
    pivot : Função
      Regra de pivoteamento. Opcional.
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
    T=np.array(A.copy()).astype(float)
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
      print("Vamos triangularizar a matriz")
      print(T)
    #end if

    while (j<n_colunas and n_pivos<n_linhas):
        if verbose:
          print("=====")
          print(f"Vamos pivotear a coluna {j}.")
        #end if

        #Encontra o pivô
        p=pivot(T[:,n_pivos:])+n_pivos

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
                    T[k,j+1:]=T[k,j+1:]-multiplicador*T[p,j+1:]
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
              print("A coluna {j} nao tem pivo.")
        #end if
        #passa pra próxima coluna
        j+=1
    #end while

    return [T,posicao_pivos]
#end def


def retrossubstituicao(A,pospiv=[],tol=1e-10,verbose=False):
  """Retrossubstituição.

  Parâmetros
  ----------
  A: Matriz triangularizada superiormente
  pospiv (opcional): lista com as posições dos pivôs de A
  tol: tolerância numérica.
  verbose: Imprimir informações intermediárias

  Saída
  ----------
  Lista [R,P], em que:
  R: Forma completamente escalonada de A.
  P: Lista com posição dos pivôs de A."""

  if verbose:
    def verboseprint(s='',end='\n'):
      print(s,end)
    #end def
  else:
    def verboseprint(s='',end='\n'):
      return
    #end def
  #end if

  #Faz as cópias usuais para evitar problemas
  R=np.matrix(A.copy()).astype(float)

  verboseprint('Vamos fazer retrosubstituição na matriz ',end='')
  verboseprint(A)
  verboseprint()

  #caso nao saibamos as posições dos pivos, temos que encontrá-los
  posicoes_pivos=pospiv
  if posicoes_pivos==[]:
    verboseprint('Nâo foi dada a posição dos pivôs da matriz.')
    verboseprint('Vamos encontrá-los:')
    i=0
    j=0
    while (i<np.shape(R)[0]):
      while abs(R[i,j])<tol and j<np.shape(R)[1]:
          j+=1
      #end while

      if j==np.shape(R)[1]:
          break
      else:
          posicoes_pivos.append(j)
          i+=1
      #end if-else
    #end while
  #end if

  verboseprint('Os pivôs estao nas colunas ',end='')
  verboseprint(posicoes_pivos)
  verboseprint()

  numero_de_pivos=len(posicoes_pivos)
  for i in range(numero_de_pivos-1,-1,-1):
    verboseprint('=====')
    #Normaliza o pivô, caso necessário
    if abs(R[i,posicoes_pivos[i]]-1)>tol:
      verboseprint('Vamos normalizar o pivô na linha ' + str(i) + '.')
      R[i,posicoes_pivos[i]:]=R[i,posicoes_pivos[i]:]/R[i,posicoes_pivos[i]]
      verboseprint(R)
      verboseprint()
    #end if
    #Aniquila as entradas acima

    verboseprint("Vamos aniquilar as entradas acima do pivô"\
    + " na posição (" + str(i) +","+str(posicoes_pivos[i])+").")
    for k in range(i-1,-1,-1):
      R[k,posicoes_pivos[i]+1:]-=R[k,posicoes_pivos[i]]*R[i,posicoes_pivos[i]+1:]
      R[k,posicoes_pivos[i]]=0
    #end for
    verboseprint(R)
  #end for

  return [R,posicoes_pivos]
#end function

def escalona(A,tol=1e-10,verbose=False):
  """Escalonamento.

  Parâmetros
  ----------
  A: Matriz
  tol: tolerância numérica.
  verbose: Imprimir informações intermediárias

  Saída
  ----------
  Lista [E,P], em que:
  E: Forma completamente escalonada de A.
  P: Lista com posição dos pivôs de A."""

  T=triangulariza(A,tol=tol,verbose=verbose)
  return retrossubstituicao(T[0],pospiv=T[1],tol=tol,verbose=verbose)
#end def
