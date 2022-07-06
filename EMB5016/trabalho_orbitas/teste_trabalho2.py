import numpy as np
import funcoes_teste
import trabalho1
import sys

def orbita_aleatorio(tipo='',passo=1,dias=10,lim=3,integer=True,verbose=False,through_zero=False):
  '''Cria aleatoriamente 5 pontos do plano cartesiano que determinam uma cônica.
  
    Parâmetros
    ----------
    tipo : string
        Tipo da conica a ser criada. Deve ser "parabola", "elipse" ou "hiperbole".
        Caso nao se especifique um tipo correto, considera-se "parabola".
    Passo: float, opcional.
        Variacao no passo para montagem da orbita. Padrao 1.
    dias : int
        Numero de dias dos quais se tem dados. Padrao 10.
    lim : numero positivo, opcional
        Utilizado para limitar os numeros intermediaros no algoritmo
    integer : boolean, opcional
        Se "True", os resultados valores criados sao todos inteiros.
        Valor padrao "True"
    verbose : boolean, opcional
        Imprimir na tela a explicacao do procedimento.
        Valor padrao "True"

    Saída
    -----
    conica_aleatorio : lista [X, Coef]
        X é uma matriz 5x2 com suas linhas da forma [x,y], em que [x,y] foram
        os pontos gerados, e Coef=[A,B,C,D,E,F] é uma lista tal que a cônica
        determinada pelos pontos de X é descrita pela equação
        Ax²+2Bxy+Cy²+2Dx+2Ey+F=0.

    Observacoes
    -----------
    O procedimento utilizado é:
    -Escolhem-se 5 valores para x aleatoriamente dentre os inteiros entre
        -lim e lim (exceto 0).
    -Para os pontos especificados acima, conforme o tipo de cônica escolhida,
        são tomados pontos de certas "cônicas padrão", conforme o tipo especificado
        --(x,x^2) da parábola x^2-y=0.
        --(x,1/x) da hipérbole xy-1=0.
        --Alguns val ores padrao para a elipse x^2+y^2=65^2
    -Aplica-se uma função afim inversível nestes pontos.
    -As imagens dos pontos vão pertencer à imagem da "cônica padrão" por esta função.
    '''

  if verbose:
    def verboseprint(s='',end='\n'):
      print(s,end)
    #end def
  else:
    def verboseprint(s='',end='\n'):
      return
    #end def
  #end if

  lista_de_x=np.zeros(dias)

  if tipo=='hiperbole':
    lista_de_x[0]=50*np.random.random()+1.0e-8

    def F(alpha):
      return 1/alpha
    #end def

    r=1
    #end for
    #No caso específico da hipérbole xy-r=0, podemos tomar A=0, B=1, C=D=E=0, F=-2r.
    A=0
    B=1
    C=0
    D=0
    E=0
    F=-2*r
  elif tipo=='elipse':
    #Encontrar pontos de elipses com coordenadas inteiras é um mais chato, então vamos pegar números específicos

    verboseprint(
      'Os números anteriores não são úteis. Vamos montar a matriz com certos pontos na elipse' +'\n'
      'x²+y²-65²=0'+'\n')
    
    
    lista_de_x[0]=50*np.random.random()-25
    

    def F(alpha):
      return np.sqrt((65**2)-(alpha**2))
    #end def

    A=1
    B=0
    C=1
    D=0
    E=0
    F=-(65*65)
  else: 
    verboseprint(
      'Vamos montar a matriz com os pontos na parábola' +'\n'
      'x²-y=0'+'\n'
      'associados a esses pontos:')
  
    lista_de_x[0]=50*np.random.random()-25
    
    def F(alpha):
      return alpha**2
    #end def

    #No caso específico da parábola x^2-1=0, podemos tomar A=2, B=C=D=0, E=-1, F=0
    A=2
    B=0
    C=0
    D=0
    E=-1
    F=0
  #end if-else

  ########
  M=np.matrix(
    [
      [A,B],
      [B,C]
    ]
  ).astype(float)

  n=np.matrix(
    [
      [D,E]
    ]
  )
  ###############
  
  T=funcoes_teste.matriz_inversivel(ordem=2,li=lim)

  if integer:
    while abs(round(funcoes_teste.determinante(T)))-1!=0:
      T=funcoes_teste.matriz_inversivel(ordem=2,li=lim)
    #end while
  else:
    while abs(round(funcoes_teste.determinante(T)))==0:
      T=funcoes_teste.matriz_inversivel(ordem=2,li=lim)
    #end while
  #end if

  if through_zero:
    if tipo=="parabola":
      #A conica original passa pelo zero
      q=np.matrix([[0,0]]).astype(float)
    elif tipo=="elipse":
      #A conica original passa pelo (25,60)
      q=(np.matrix([[25,60]]).astype(float))@T
    elif tipo=="hiperbole":
      #A conica original passa pelo (1,r)
      q=(np.matrix([[1,r]]).astype(float))@T
  else:
    q=np.matrix(np.random.randint(low=-lim,high=lim+1,size=(1,2))).astype(float)
  #
  verboseprint(
    'A função afim que vamos aplicar é\n'+
    'x --> xT+q,\n'+
    'em que\n'+
    'a variável x é um vetor linha com 2 coordenadas\n'+
    'T é a matriz'
  )
  verboseprint(T)
  verboseprint(
    'e q é o vetor'
  )
  verboseprint(q)
  
  #Conforme o relatório, para determinar os coeficientes da cônica imagem, devemos calcular algumas matrizes:
  inversaT=funcoes_teste.inversa_por_escalonamento(T,verbose=False)
  inversaTestrela=funcoes_teste.transposta(inversaT)
  Mtil=np.matmul(np.matmul(inversaT,M),inversaTestrela)
  qtil=np.matmul(q,Mtil)
  nestrela=np.matmul(n,inversaTestrela)
  ntil=nestrela-qtil
  Ftil=np.matmul(q,funcoes_teste.transposta(qtil-2*nestrela))[0,0]+F

  #Agora, vamos calcular os pontos da orbita

  pontos_da_orbita=np.zeros(size=(dias,2))

  pontos_da_orbita[0]=np.matrix([[lista_de_x[0],F(lista_de_x[0])]])*T+q

  def dist(A,B):
    m,n=np.shape(A)
    d=0
    for i in range(m):
      for j in range(n):
        d+=(A[i,j]-B[i,j])**2
      #end for
    #end for

    return np.sqrt(d)
  #end def

  for i in range(1,dias):
    novo_x=lista_de_x[i-1]
    novo_ponto_da_orbita=np.matrix([[novo_x,F(novo_x)]])*T+q

    d=0
    while d<1:
      novo_x=lista_de_x[i-1]+(0.2*np.random.random())

      d+=dist(novo_ponto_da_orbita,np.matrix([[novo_x,F(novo_x)]])*T+q)
      novo_ponto_da_orbita=np.matrix([[novo_x,F(novo_x)]])*T+q
    #end while

    lista_de_x[i]=novo_x
    pontos_da_orbita[i]=novo_ponto_da_orbita
  #end for

  Coef=[Mtil[0,0], Mtil[0,1], Mtil[1,1], ntil[0,0], ntil[0,1], Ftil]

  #Se for inteiro, vamos fazer ficar inteiro de fato
  if integer:
    for i in range(6):
      Coef[i]=round(Coef[i])
    #end for
  #end if
  
  return [pontos_da_orbita,Coef]
#end def

