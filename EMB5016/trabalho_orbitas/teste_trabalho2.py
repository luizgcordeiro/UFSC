import numpy as np
import matplotlib.pyplot as plt
import funcoes_teste
import sys

def orbita_aleatorio(tipo='parabola',dias=10,lim=3,integer=True,verbose=False,through_zero=False):
  '''Cria aleatoriamente uma quantidade de pontos do plano que denotam a orbita de um corpo celeste.
  
    Parâmetros
    ----------
    tipo : string
        Tipo da conica a ser criada. Deve ser "parabola" (padrao), "elipse"
        ou "hiperbole".
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
    orbita_aleatorio : lista [X, Coef]
        X : array-like de dimensão 2
          Tem o mesmo numero de linhas que o parametro 'dias'. Cada linha
          é um array de tamanho 2, da forma [x,y]. Esses pontos sao aproximacoes
          (com pequenos erros, para melhor simular uma situacao real) de pontos
          da orbita de um objeto celeste sob a acao da gravidade
        Coef : array [A,B,C,D,E,F]
          Lista tal que a órbita real e descrita pela equação
          Ax²+2Bxy+Cy²+2Dx+2Ey+F=0.
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

  x=-np.random.random()#numero entre -1 e 0

  if tipo=='hiperbole':

    lista_de_x[0]*=np.random.choice([-1,1])
    #hiperbole y^2-x^2=1
    def FUNCAO(alpha):
      return np.sqrt(dias**2+1)
    #end def

    r=1
    #end for
    A=-1
    B=0
    C=1
    D=0
    E=0
    F=-1
  elif tipo=='elipse':
    #elipse y^2-x^2=1

    def FUNCAO(alpha):
      return np.sqrt(1-(alpha**2))
    #end def

    
    A=1
    B=0
    C=1
    D=0
    E=0
    F=-1
  else: #if tipo="parabola"
    verboseprint(
      'Vamos montar a matriz com os pontos na parábola' +'\n'
      'y=x^2 (fica uma proporcao legal com as outras)'+'\n'
      'associados a esses pontos:')
  
    lista_de_x[0]*=np.random.choice([-1,1])
    
    def FUNCAO(alpha):
      return (alpha**2)
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
  M=np.array(
    [
      [A,B],
      [B,C]
    ]
  ).astype(float)

  n=np.array(
    [
      [D,E]
    ]
  )
  ###############
  
  T=np.random.randint(low=-lim.high=lim,size=(2,2)).astype(float)

  T=np.transpose(T)@T#auto-adjunta positiva, em particular sem -1 como autovalor
  T=(np.eye(2)-T)@np.linalg.inv(np.eye(2)+T)  #Transformada de Caley; matriz unitária/ortogonal
  #Multiplica por uma matriz do tipo [[1,-a],[b,1]], com a e b pequenos;
  #Matriz proxima a identidade, logo nao muda muito de uma isometria, mas um pouco sim.
  T=np.array([[1, -(1/2)*np.random.random()],[(1/2)*np.random.random(),1]])@T
  
  #Arrumar a a versao que passa pelo 0
  q=np.random.randint(low=-lim,high=lim+1,size=(1,2)).astype(float)

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
  inversaT=np.linalg.inv(T)
  inversaTestrela=np.transpose(inversaT)
  Mtil=inversaT@M@inversaTestrela
  qtil=q@Mtil
  nestrela=n@inversaTestrela
  ntil=nestrela-qtil
  Ftil=q@np.transpose(qtil-2*nestrela)[0,0]+F

  #Agora, vamos calcular os pontos da orbita

  pontos_da_orbita=np.zeros([dias,2])
  #print(lista_de_x[0])
  #pontos_da_orbita[0]=]

  for i in range(dias):
    #A primeira entrada e um pouquinho aleatorizada
    pontos_da_orbita[i]=(np.array([x,FUNCAO(x)])@T)+q
    x+=1/dias
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

X=orbita_aleatorio(tipo="elipse",dias=10,passo=1)
#print(X[0][:,0])
#print(X[0][:,1])
print(X[0])
plt.plot(X[0][:,0],X[0][:,1],'o')
plt.show()