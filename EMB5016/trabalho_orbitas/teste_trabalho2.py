import numpy as np
import matplotlib.pyplot as plt
import funcoes_teste
import sys

def orbita_aleatorio(tipo='parabola',dias=10,lim=3,verbose=False,through_zero=False,perc_erro=.05):
  '''Cria aleatoriamente uma quantidade de pontos do plano que retratam
  a orbita de um corpo celeste.
  
    Parâmetros
    ----------
    tipo : string
        Tipo da conica a ser criada. Deve ser "parabolica" (padrao), "eliptica"
        ou "hiperbolica".
    dias : int
        Numero de dias dos quais se tem dados. Padrao 10.
    lim : numero positivo, opcional
        Utilizado para limitar os numeros intermediaros no algoritmo
    verbose : booleanol, opcional
        Imprimir na tela a explicacao do procedimento.
        Valor padrao "True"
    perc_erro : float em [0,1], opcional
        Valor maximo para o erro nos pontos criados. Padrao 0.05

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

  if tipo=='hiperbolica':

    #hiperbole y^2-x^2=1
    def FUNCAO(alpha):
      return np.sqrt(alpha**2+1)
    #end def

    #end for
    A=-1
    B=0
    C=1
    D=0
    E=0
    F=-1
  elif tipo=='eliptica':
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
  else: #if tipo="parabolica"
    verboseprint(
      'Vamos montar a matriz com os pontos na parábola' +'\n'
      'y=x^2 (fica uma proporcao legal com as outras)'+'\n'
      'associados a esses pontos:')
  
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
  
  T=np.random.randint(low=-lim,high=lim,size=(2,2)).astype(float)
  T=T-np.transpose(T)#skew-symmetric matrix
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
  Ftil=(q@np.transpose(qtil-2*nestrela))[0,0]+F

  Coef=[Mtil[0,0], Mtil[0,1], Mtil[1,1], ntil[0,0], ntil[0,1], Ftil]
  #Agora, vamos calcular os pontos da orbita

  pontos_da_orbita=np.zeros([dias,2])
  #print(lista_de_x[0])
  #pontos_da_orbita[0]=]

  for i in range(dias):
    #A primeira entrada e um pouquinho aleatorizada
    pontos_da_orbita[i]=(np.array([x+perc_erro*np.random.random()/dias,FUNCAO(x+perc_erro*np.random.random()/100)])@T)+q
    x+=1/dias
  #end for

  Coef=[Mtil[0,0], Mtil[0,1], Mtil[1,1], ntil[0,0], ntil[0,1], Ftil]

  return [pontos_da_orbita,Coef]
#end def


#HIPERBOLICAS
hiperbolicas=[]
num_hip=0
ruim=0
while num_hip<10000:
  num_dias=np.random.choice(list(range(50,100)))
  X=orbita_aleatorio(tipo="hiperbolica",dias=num_dias,perc_erro=1.0e-2)
  while abs(X[1][5])<.5:
    X=orbita_aleatorio(tipo="hiperbolica",dias=num_dias,perc_erro=1.0e-2)

  M=np.zeros([num_dias,5])
  for i in range(num_dias):
    M[i,0]=X[0][i,0]**2
    M[i,1]=2*X[0][i,0]*X[0][i,1]
    M[i,2]=X[0][i,1]**2
    M[i,3]=2*X[0][i,0]
    M[i,4]=2*X[0][i,1]
  #end for
  #F=(-X[1][5])
  F=-1

  [A,B,C,D,E]=np.linalg.lstsq(M,-np.ones(num_dias),rcond=None)[0]

  det=np.linalg.det([[A,B],[B,C]])
  if det<-1.0e-3:
    num_hip+=1
    hiperbolicas+=[X[0]]
  else:
    ruim+=1
    #plt.plot(X[0][:,0],X[0][:,1],'o')
    #plt.show()
  #end if

#end for
print("Hiperbolicas: " + str(ruim) + " ruins.")

hiperbolicas=np.array(hiperbolicas,dtype=object)
file_to_write=open("hiperbolicasxxx.npy",'wb')
np.save(file_to_write,hiperbolicas)

file_to_write.close()

####PARABOLICAS
parabolicas=[]
ruim=0
num_par=0
while num_par<10000:
  num_dias=np.random.choice(list(range(50,100)))
  X=orbita_aleatorio(tipo="parabolica",dias=num_dias,perc_erro=1.0e-2)
  while abs(X[1][5])<.5:
    X=orbita_aleatorio(tipo="parabolica",dias=num_dias,perc_erro=1.0e-2)

  M=np.zeros([num_dias,5])
  for i in range(num_dias):
    M[i,0]=X[0][i,0]**2
    M[i,1]=2*X[0][i,0]*X[0][i,1]
    M[i,2]=X[0][i,1]**2
    M[i,3]=2*X[0][i,0]
    M[i,4]=2*X[0][i,1]
  #end for
  #F=(-X[1][5])
  F=-1

  [A,B,C,D,E]=np.linalg.lstsq(M,-np.ones(num_dias),rcond=None)[0]

  det=np.linalg.det([[A,B],[B,C]])
  if abs(det)<1.0e-3:
    num_par+=1
    parabolicas+=[X[0]]
  else:
    ruim+=1
  #end if
#end for
print("Parabolicas: " + str(ruim) + " ruins.")

parabolicas=np.array(parabolicas,dtype=object)
file_to_write=open("parabolicasxxx.npy",'wb')
np.save(file_to_write,parabolicas)

file_to_write.close()

#ELIPTICAS
elipticas=[]
ruim=0
num_el=0
while num_el<10000:
  num_dias=np.random.choice(list(range(50,100)))
  X=orbita_aleatorio(tipo="eliptica",dias=num_dias,perc_erro=1.0e-2)
  while abs(X[1][5])<.5:
    X=orbita_aleatorio(tipo="eliptica",dias=num_dias,perc_erro=1.0e-2)

  M=np.zeros([num_dias,5])
  for i in range(num_dias):
    M[i,0]=X[0][i,0]**2
    M[i,1]=2*X[0][i,0]*X[0][i,1]
    M[i,2]=X[0][i,1]**2
    M[i,3]=2*X[0][i,0]
    M[i,4]=2*X[0][i,1]
  #end for
  #F=(-X[1][5])
  F=-1

  [A,B,C,D,E]=np.linalg.lstsq(M,-np.ones(num_dias),rcond=None)[0]

  det=np.linalg.det([[A,B],[B,C]])
  if abs(det)>1.0e-3:
    num_el+=1
    elipticas+=[X[0]]
  else:
    ruim+=1
  #end if

#end for
print("Elipticas: " + str(ruim) + " ruins.")

elipticas=np.array(elipticas,dtype=object)
file_to_write=open("elipticasxxx.npy",'wb')
np.save(file_to_write,elipticas)

file_to_write.close()


show_plot=False
if show_plot:
  plt.plot(X[0][:,0],X[0][:,1],'o')
  plt.show()
#end if

#x=np.load('parabolicas.npy',allow_pickle=True)
