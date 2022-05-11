import numpy as np

def triangulariza(A,tol=1.0e-10,verbose=False):
    '''Esta função triangulariza uma matriz A com pivotação parcial.

    Parâmetros
    ----------
    A: matriz a ser triangularizada.
    tol: tolerância numérica.
    verbose: Imprimir informações intermediárias

    Saída
    ----------
    Lista [T,P], em que
    T: Forma escalonada de A.
    P: lista com os índices das colunas que têm os pivôs de T.'''

    if verbose:
      def verboseprint(s='',end='\n'):
        print(s,end)
      #end def
    else:
      def verboseprint(s='',end='\n'):
        return
      #end def
    #end if


    #Faz cópias
    B=(np.matrix(A).copy()).astype(float)
    posicao_pivos=[]
    #Grava o tamanho
    ordem=np.shape(B)
    n_linhas=ordem[0]
    n_colunas=ordem[1]
    #Vê quantos pivôs já foram achados
    numero_de_pivos=0

    #Linhas na qual trabalharemos
    j=0

    verboseprint("Vamos triangularizar a matriz")
    verboseprint(B)

    while (j<n_colunas and numero_de_pivos<n_linhas):
        verboseprint("=====")
        verboseprint("Vamos pivotear a coluna " + str(j) + ".")

        #Encontra o pivô
        p=np.argmax(abs(B[numero_de_pivos:,j]))+numero_de_pivos

        if abs(B[p,j])>tol:

            #verboseprint("O pivô da coluna " + str(j) " está na linha " + str(p) + ".")

            #Encontramos um pivô.
            #Troca linhas caso necessário
            if p!=numero_de_pivos:
                verboseprint("Precisamos trocar a linha " + \
                    str(numero_de_pivos) + " com a linha " + str(p) + ".")
                l=B[p,:].copy()
                B[p,:]=B[numero_de_pivos,:]#.copy() já é feito automaticamente
                B[numero_de_pivos,:]=l
                verboseprint(B)
            #end if

            #Pivoteia abaixo
            for k in range(numero_de_pivos+1,n_linhas):
                if abs(B[k,j])>tol:
                    multiplicador=B[k,j]/B[numero_de_pivos,j]
                    B[k,j+1:]=B[k,j+1:]-multiplicador*B[numero_de_pivos,j+1:]
                    B[k,j]=0;
                #end if
            #end for
            verboseprint("Aniquila as entradas abaixo:")
            verboseprint(B)

            #Conta o pivô a mais
            numero_de_pivos+=1
            posicao_pivos.append(j)
        else:
            verboseprint("A coluna " + str(j) + " não tem pivô.")
        #end if
        #passa pra próxima coluna
        j+=1
    #end while

    return [B,posicao_pivos]
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
