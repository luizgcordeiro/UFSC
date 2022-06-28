import numpy as np
import funcoes_teste
import trabalho1
import sys

def conica_aleatorio(tipo='',lim=3,integer=True,verbose=False):
  '''Cria aleatoriamente 5 pontos do plano cartesiano que determinam uma cônica.
  
    Parâmetros
    ----------
    tipo : string
        Tipo da conica a ser criada. Deve ser "parabola", "elipse" ou "hiperbole".
        Caso nao se especifique um tipo correto, considera-se "parabola".
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

  verboseprint(
    'Primeiro, vamos escolher 5 números aleatórios' +'\n'
    'entre '+ str(-lim) + ' e ' + str(lim)
    )

  lista_de_x=[]

  while len(lista_de_x)!=5:
    i=float(np.random.randint(low=-lim,high=lim+1))
    while i in lista_de_x or i==0:
      i=float(np.random.randint(low=-lim,high=lim+1))
    #end while

    lista_de_x=lista_de_x+[i]
  #end while

  verboseprint('Os números escolhidos foram:')
  verboseprint(lista_de_x)

  if tipo=='hiperbole':
    r=1
    if integer:
      for i in range(5):
        r=np.lcm(r,round(lista_de_x[i]))
      #end for
    #end if

    verboseprint(
      'Vamos montar a matriz com os pontos na hipérbole' +'\n'
      'xy-'+str(r)+'=0'+'\n'
      'associados a esses pontos:')

    X=np.matrix([[lista_de_x[0],r/lista_de_x[0]]])
    for i in range(1,5):
      X=np.concatenate(
          (
            X,
            np.matrix([[lista_de_x[i],r/lista_de_x[i]]])
          ),
        axis=0
        )
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
    
    
    X=np.matrix(
      [
        [39,52],
        [-25,60],
        [39,-52],
        [-39,-52],
        [-25,-60]
      ]
    )

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
  
    X=np.matrix([[lista_de_x[0],lista_de_x[0]*lista_de_x[0]]])
    for i in range(1,5):
      X=np.concatenate(
          (
            X,
            np.matrix([[lista_de_x[i],lista_de_x[i]*lista_de_x[i]]])
          ),
        axis=0
        )
    #end for
    #No caso específico da parábola x^2-1=0, podemos tomar A=2, B=C=D=0, E=-1, F=0
    A=2
    B=0
    C=0
    D=0
    E=-1
    F=0
  #end if-else
    
  verboseprint(X)
  verboseprint(
    'Agora, vamos aplicar uma função afim inversível'+'\n'
    'nesses pontos, para obter uma cônica não-trivial.'
    )

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

  q=np.matrix(np.random.randint(low=-lim,high=lim+1,size=(1,2))).astype(float)

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

  #A imagem dos pontos em X é
  Y=np.matmul(X,T)+q

  Coef=[Mtil[0,0], Mtil[0,1], Mtil[1,1], ntil[0,0], ntil[0,1], Ftil]

  #Se for inteiro, vamos fazer ficar inteiro de fato
  if integer:
    for i in range(5):
      for j in range(2):
        Y[i,j]=round(Y[i,j])
      #end for
    #end for
    for i in range(6):
      Coef[i]=round(Coef[i])
    #end for
  #end if
  
  return [Y,Coef]
#end def

X_h=conica_aleatorio(tipo="hiperbole")
X_e=conica_aleatorio(tipo="elipse")
X_p=conica_aleatorio(tipo="parabola")

#Checar se a hiperbole esta boa

type_of_conic=sys.argv[1]
print(type_of_conic)
if type_of_conic=="p":
    X=X_p
elif type_of_conic=="h":
    X=X_h
elif type_of_conic=="e":
    X=X_e


C=trabalho1.trabalho1_conica(X[0],verbose=True)
print("Coeficientes: "
print(C[1])

