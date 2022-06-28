import numpy as np
import matplotlib.pyplot as plt

import funcoes_teste
import escalonamento
import newton
#import aula8

def trabalho1_conica(X,verbose=False,tol=1.0e-14,plot=True):
  '''
  Esta função toma 5 pontos do plano cartesiano, dados em
  uma matriz X, e determina se existe uma única cônica
  não-degenerada que passa por esses pontos.

  Os pontos da cônica devem ser inseridos por meio de uma
  matriz do tipo numpy, que pode ser introduzida na forma
  X=numpy.matrix([[x0,y0],[x1,y1],[x2,y2],[x3,y3],[x4,y4]])
  em que [x0,y0],...,[x4,y4] são os pontos distintos que
  o usuário quer utilizar.

  Você também pode utilizar a opção "verbose=True", caso
  queira imprimir os passos intermediários e algumas
  outras informações no console.
  
  O valor "tol" é a tolerância computacional.

  Caso você queira obter um gráfico com a cônica e os
  pontos de interesse, utilize a opção "plot=True"

  Esta função retorna uma tupla [t,S], em que t é o tipo
  de cônica determinada pelos pontos (como uma string), e
  S=[A,B,C,D,E,F]
  é uma tupla de números, que descrevem uma equação do
  tipo
  Ax²+2Bxy+Cy²+2Dx+2Ey+F=0
  que determina tal cônica.
  '''

  if verbose:
    def verboseprint(s=''):
      print(s)
    #end def
  else:
    def verboseprint(s=''):
      return
    #end def
  #end if-else

  if np.shape(X)[0]!=5 or np.shape(X)[1]!=2 :
    print(
      'Erro: Matrix de pontos não é válida.'+'\n'
      +'Tente novamente.'
    )
    return
  #end if

  verboseprint('=====')

  verboseprint('Os pontos inseridos foram')
  verboseprint(X)
  verboseprint('=====')
  verboseprint(
    'Para determinar se existe uma cônica que passa por'+'\n'
    +'esses pontos, devemos determinar se existem números'+'\n'
    +'A, B, C, D e E tais que os pontos acima satisfazem à'+'\n'
    +'equação'+'\n'
    +'Ax^2+2Bxy+Cy^2+2Dx+2Ey+F=0'
  )
  verboseprint('=====')
  verboseprint(
    'Substituindo os valores para x e y dados pelos pontos'+'\n'
    'acima, obtemos as seguintes equações:'
  )

  if verbose:
    for i in range(5):
      verboseprint(
        '('+str(X[i,0]*X[i,0])+'A)'
        +'+('+str(2*X[i,0]*X[i,1])+'B)'
        +'+('+str(X[i,1]*X[i,1])+'C)'
        +'+('+str(2*X[i,0])+'D)'
        +'+('+str(2*X[i,1])+'E)'
        +'+F'
        +'=0,'
      )
    #end for
  #end if
  verboseprint(
    'que é um sistema linear com 5 equações nas variáveis\n'+
    'A, B, C, D, E e F.'
  )
  
  #Vamos gravar essas variáveis em uma lista, para uso posterior
  vars=['A','B','C','D','E','F']

  verboseprint('=====')

  verboseprint('A matriz deste sistema linear é')

  M=np.matrix(np.zeros([5,6])).astype(float)

  for i in range(5):
    M[i,0]=X[i,0]*X[i,0]
    M[i,1]=2*X[i,0]*X[i,1]
    M[i,2]=X[i,1]*X[i,1]
    M[i,3]=2*X[i,0]
    M[i,4]=2*X[i,1]
    M[i,5]=1
  #end for

  verboseprint(M)
  verboseprint('=====')
  verboseprint('A forma escalonada completa de M é')
  
  #Como eu fiz os VPLs e estudei direito, basta usar um programa já criado anteriormente e economizar tempo
  K=escalonamento.escalona(M,tol=tol,verbose=False)
  E=K[0]
  pivos=K[1]
  
  verboseprint(E)
  verboseprint('=====')

  if len(pivos)<5:
    verboseprint(
      'Essa matriz tem mais do que uma variável livre, e'+'\n'
      +'portanto existem equações quadráticas não-triviais e'+'\n'
      +'não-equivalentes (i.e., que não são uma múltipla da'+'\n'
      +'outra) que são satisfeitas pelos pontos dados.'+'\n'
    )
    verboseprint('')
    print(
      'Não existe exatamente uma cônica não-degenerada que'+'\n'
      +'passa por esses pontos. Ou seja, ou existe mais do que'+'\n'
      +'uma cônica não-degenerada que passa pelos pontos dados,\n'+
      'ou só existem cônicas degeneradas que passam por esses\n'+
      'pontos.'
    )
    print('')
    print('Não podemos prosseguir.')
    return
  #end if

  verboseprint(
    'Esta matriz tem exatamente uma coluna sem pivô, que'+'\n'
    +'determina uma única variável livre para a solução geral'+'\n'
    +'do sistema linear.'
  )

  #Vamos determinar qual é a coluna que não tem pivô
  col_livre=0
  while col_livre in pivos:
    col_livre=col_livre+1
  #end while

  verboseprint(
    'Neste caso, a variável livre determinada por esta'+'\n'
    'coluna é '
    +vars[col_livre]
  )

  verboseprint('')
  verboseprint(
    'Para encontrar a equação da cônica (a menos de um\n'
    'múltiplo não-nulo), basta igualar esta variável livre a\n'
    '1.'
  )

  #Agora, vamos gravar os valores das variáveis/coeficientes A, B, C, D, E e F. Vamos utilizar essas mesmas letras como os nomes delas. Mas é um pouco mais fácil primeiro gravar os valores delas em ordem, conforme ela seja ou não a variável livre, e depois dar os seus valores também em ordem.
  #Para determinar o valor das variáveis não-livres, basta utilizar a forma escalonada completa da matriz M, que já foi calculada
  valores_coefs=[0,0,0,0,0,0]

  valores_coefs[col_livre]=1
  for i in range(5):
    #O i-ésimo pivô, que corresponde à i-ésima variável dependente, está na entrada (i,pivos[i]) da matriz E
    valores_coefs[pivos[i]]=-E[i,col_livre]
  #end for

  #Vamos renomear
  A=valores_coefs[0]
  B=valores_coefs[1]
  C=valores_coefs[2]
  D=valores_coefs[3]
  E=valores_coefs[4]
  F=valores_coefs[5]

  verboseprint('=====')
  verboseprint(
    'Portanto, a única cônica que passa pelos pontos dados é'+'\n'
    +'a dada pela equação'+'\n'
    +'Ax^2+2Bxy+Cy^2+2Dx+2Ey+F=0,'+'\n'
    +'em que'
  )
  if verbose:
    for i in range(6):
      verboseprint(vars[i]+'='+str(valores_coefs[i]))
    #end for
  #end if
  verboseprint('=====')
  verboseprint(
    'OBSERVAÇÃO: Se utilizarmos os pontos dados acima na\n'
    'expressão\n'
    'Ax^2+2Bxy+Cy^2+2Dx+2Ey+F,\n'
    'obtemos, respectivamente, os valores'
  )

  delt=0
  for i in range(5):
    avalicao=A*(X[i,0]**2)+2*B*X[i,0]*X[i,1]+C*(X[i,1]**2)+2*D*X[i,0]+2*E*X[i,1]+F
    verboseprint(avalicao)
    delt=max(delt,abs(avalicao))
  #end for
  #Se A, B, C, D, E, F fossem calculados exatamente, as expressões acima ficariam
  #do tipo
  #(A+erro)x^2+2(B+erro)xy+(C+erro)y^2+2(D+erro)x+2(E+erro)y+(F+erro)=del
  #que se reduz a algo do tipo
  #erro(x^2+y^2+x+y+1)=del,
  #e portanto erro=del(x^2+y^2+x+y+1)<~del
  verboseprint(
    'e, portanto, o erro acumulado no cálculo de cada\n'
    'coeficiente dentre A, B, C, D, E e F é da ordem de\n'
    +str(delt)+'.'
  )

  verboseprint('=====')

  verboseprint(
    'Agora, lembre-se que a cônica determinada pela equação\n'
    'acima é não-degenerada se, e somente se, a matriz'
  )
  verboseprint(
    '[[A B D],'+'\n'
    +' [B C E],'+'\n'
    +' [D E F]]'
  )
  verboseprint('tem determinante não-nulo.')

  det_deg=funcoes_teste.determinante(np.matrix([
    [A, B, D],
    [B, C, E],
    [D, E, F]
  ]))

  verboseprint('Neste caso, o determinante é '+str(det_deg))

  maxcoef=max(abs(A),abs(B),abs(C),abs(D),abs(E),abs(F))

  #Vamos analisar o erro no cálculo do determinante acima: Em cada entrada da matriz, aparece um erro da ordem de 'delt'; ao fazer os produtos das diagonais (como na regra de sarrus), aparece um erro da ordem de 3*maxcoef^2*delt+3*maxcoef*delt^2. Como 'delt' deve ser pequeno, e maxcoef>=1 (pois a variável livre froi atribuída valor 1), podemos dizer que o erro no cálculo do produto de cada diagonal será da ordem de 4*maxcoef^2*delt. Como são consideradas 6 diagonais, isso se acumula a um erro da ordem de 24*maxcoef^2*delt
  
  if abs(det_deg)<tol+(24*maxcoef*maxcoef*delt):
    verboseprint('Para fins computacionais, esse determinante é nulo.')
    print('A cônica é degenerada.')
    return
  #end if

  verboseprint(
    'Esse determinante é não-nulo, e a cônica é\n'
    'não-degenerada.'
  )

  verboseprint('=====')
  verboseprint(
    'Agora, lembre-se que para determinar o tipo de cônica'+'\n'
    'que é determinada por essa equação, devemos analisar o'+'\n'
    'determinante da matriz'
  )
  verboseprint(
    '[[A B],'+'\n'
    +' [B C]].'
  )
  
  det_tip=funcoes_teste.determinante(np.matrix([
    [A, B],
    [B, C]
  ]))

  verboseprint('O determinante é '+str(det_tip))

  #Por uma análise similar à feita acima,  o erro no cálculo desse determinande 2x2 será ad ordem de 2*(2*maxcoef*delt+delt^2)~4*maxcoef*delt

  verboseprint('=====')
  if abs(det_tip)<tol+4*maxcoef*delt:
    verboseprint('Para fins computacionais, esse determinante é nulo.')
    print('A cônica é uma parábola.')
    tipodeconica='parábola'
  elif det_tip>0:
    verboseprint('Esse determinante é positivo.')
    print('A cônica é uma elipse.')
    tipodeconica='elipse'
  else:
    verboseprint('Esse determinante é negativo.')
    print('A cônica é uma hipérbole.')
    tipodeconica='hipérbole'
  #end if

  if plot:
    verboseprint('=====')
    verboseprint(
      'Por fim, vamos plotar a cônica que passa pelos pontos'+'\n'
      +'dados.'
    )

    #Procedimento adaptado de https://stackoverflow.com/questions/29582089/how-to-plot-an-ellipse-by-its-equation-on-python
    #Para o tamanho dos eixos, consideramos um retângulo ao redor dos pontos dados pelo usuário, que pode ser obtido simplesmente considerando os maiores valores para x e y
    xmin=min([X[0,0],X[1,0],X[2,0],X[3,0],X[4,0]])
    xmax=max([X[0,0],X[1,0],X[2,0],X[3,0],X[4,0]])
    ymin=min([X[0,1],X[1,1],X[2,1],X[3,1],X[4,1]])
    ymax=max([X[0,1],X[1,1],X[2,1],X[3,1],X[4,1]])

    #Vamos deixar um pouco de folga ao redor dos pontos dados pelo usuário, digamos aumentando o retângulo em 25% em cada direção
    xscale=xmax-xmin
    yscale=ymax-ymin

    #Criamos os eixos conforme comentários acima
    x_axis=np.linspace(xmin-.25*xscale,xmax+.25*xscale,200)
    y_axis=np.linspace(ymin-.25*yscale,ymax+.25*yscale,200)

    #Agora, fazemos um grid com x_axis e y_axis os intervalos que limitam os eixos horizontal e vertical, respectivamente.
    #Ao mesmo tempo, transformamos "x_axis" e "y_axis" em grids. Assim, "x_axis" funciona como se fosse a projeção na primeira entrada do nosso grid, e "y_axis" como se fosse a projeção na segunda entrada.
    x_axis,y_axis=np.meshgrid(x_axis,y_axis)
    #Daí, a função "Z(x,y)=Ax^2+2Bxy+Cy^2+2Dx+2Ey+F" pode ser escrita em termos dessas projeções
    Z=(A*(x_axis**2))+(2*B*x_axis*y_axis)+(C*y_axis*y_axis)+2*D*x_axis+2*E*y_axis+F

    #Então, basta fazer o contorno dos pontos no grid que satisfazem "Z(x,y)=0"
    plt.contour(x_axis,y_axis,Z,[0])

    #Vamos também desenhar e marcar os pontos dados pelo usuário, para ficar mais bonitinho
    plt.plot(X[:,0],X[:,1],'o')
    for i in range(5):
      plt.text(X[i,0],X[i,1],'('+str(round(X[i,0],2))+','+str(round(X[i,1],2))+')')
    #end for

    #Mostra o plot:
    plt.show()
  #end if

  return [tipodeconica,[A,B,C,D,E,F]]
#end def

###############################
#Abaixo, a função que resolve a parte do trabalho que requer encontrar pontos de intersecção da cônica com uma reta.
  
def trabalho1_int(X,c,verbose=False,tol=1.0e-10,plot=True):
  '''
  Esta função determina a cônica via
  trabalho1_conica(X,verbose,tol,plot=False)
  e então retorna uma tupla I, contendo todos os pontos
  de intersecção da reta x=c com a cônica acima.

  Caso a opção "plot=True" seja selecionada, será mostrado
  um gráfico com a cônica e a reta x=c
  
  Para mais informações, veja a documentação da função
  trabalho1_conica.
  '''

  verb=verbose
  def verboseprint(s=''):
    if verbose:
      print(s)
    #end if
  #end def

  valores_coefs=trabalho1_conica(X,verbose=verb,tol=tol,plot=False)

  #Pode ser que os pontos não determinem uma cônica
  if type(valores_coefs)==type(None):
    print(
      'Os pontos dados não determinam uma única cônica não-\n'
      '-degenerada.'
    )

    return
  #end if

  #Caso contrário, siga em frente
  A=valores_coefs[1][0]
  B=valores_coefs[1][1]
  C=valores_coefs[1][2]
  D=valores_coefs[1][3]
  E=valores_coefs[1][4]
  F=valores_coefs[1][5]
  
  verboseprint('=====')

  verboseprint(
    'Vamos determinar a intersecção da reta'+'\n'
    +'x='+str(c)+'\n'
    +'com a cônica determinada acima.'
  )
  verboseprint('=====')

  #A quadrática abaixo é obtida na mão, fazendo manipulações triviais:
  verboseprint(
    'Substituindo esse valor de x na equação da cônica,'+'\n'
    +'obtemos a equação'+'\n'
    +'('+str(C)+'y^2)+('+str((2*B*c)+(2*E))+'y)+('+str((A*c*c)+(2*D*c)+F)+')=0,'+'\n'
    +'na variável y.'
  )

  #Aqui, temos vários casos a considerar:  
  if abs(C)<tol:
    #-Caso C=0, então a equação é afim: ay+b=0, com a e b dados conforme acima. Temos dois subcasos:
    verboseprint(
      'A equação é linear.'
    )
    verboseprint('=====')
    if abs((2*B*c)+(2*E))<tol:
      #--Caso a=0, então a equação vira b=0. Neste caso, o conjunto solução é vazio (caso b!=0), ou é a reta real inteira (caso b=0). Mas o segundo caso implicaria que a cônica não-degenerada contém a reta x=c, o que não pode ser. Então neste caso, o conjunto solução é vazio.
      verboseprint('Não existe ponto de intersecção')
      I=[]
    else:
      #--Caso a!=0, então só há a solução y=-b/a.
      verboseprint('Existe somente um ponto de intersecção:')
      I=[-((A*c*c)+(2*D*c)+F)/((2*B*c)+(2*E))]
      verboseprint('y='+str(I[0]))
    #end if
  else:
    #-Caso C!=0, aplicamos a fórmula de Bháskara
    verboseprint(
      'A equação é quadrática, com discriminante igual a'
    )
  
    discriminante=(((2*B*c)+(2*E))*((2*B*c)+(2*E)))-(4*C*((A*c*c)+(2*D*c)+F))
    verboseprint(str(discriminante)+'.')

    verboseprint('=====')
    if abs(discriminante)<tol:
      verboseprint('Existe somente um ponto de intersecção:')
      #-b/2a, a fórmula usual
      I=[-((2*B*c)+(2*E))/(2*C)]
      verboseprint('y='+str(I[0]))
    elif discriminante<0:
      verboseprint('Não existe ponto de intersecção')
      I=[]
    else:
      verboseprint('Existem dois pontos de intersecção:')
      
      #Vamos calcular a raiz do discriminante utilizando o método de Newton na função f(x)=x^2-discriminante, o que já foi feito na aula 7
      def g(x):
        return x*x-discriminante
      #end def

      raizdiscriminante=semana7.newton(g,1.0,verbose=False)
      I=[(-((2*B*c)+(2*E))-raizdiscriminante)/(2*C),(-((2*B*c)+(2*E))+raizdiscriminante)/(2*C)]
      verboseprint('y='+str(I[0]))
      verboseprint('e')
      verboseprint('y='+str(I[1]))
    #end if-else (quadrática tem quantas raízes)
  #end if-else (quadrática ou linear)

  ######################################
  #Parte da plotagem copiada da função anterior
  if plot:
    verboseprint('=====')
    verboseprint(
      'Por fim, vamos plotar a cônica que passa pelos pontos'+'\n'
      +'dados, e a reta x=c.'
    )

    #Consideramos também uma largura suficiente para mostrar a reta x=c
    xmin=min([X[0,0],X[1,0],X[2,0],X[3,0],X[4,0],float(c)])
    xmax=max([X[0,0],X[1,0],X[2,0],X[3,0],X[4,0],float(c)])
    ymin=min([X[0,1],X[1,1],X[2,1],X[3,1],X[4,1]])
    ymax=max([X[0,1],X[1,1],X[2,1],X[3,1],X[4,1]])

    xscale=xmax-xmin
    yscale=ymax-ymin

    x_axis=np.linspace(xmin-.25*xscale,xmax+.25*xscale,200)
    y_axis=np.linspace(ymin-.25*yscale,ymax+.25*yscale,200)

    x_axis,y_axis=np.meshgrid(x_axis,y_axis)
    Z=(A*(x_axis**2))+(2*B*x_axis*y_axis)+(C*y_axis*y_axis)+2*D*x_axis+2*E*y_axis+F

    plt.contour(x_axis,y_axis,Z,[0])

    plt.plot(X[:,0],X[:,1],'o')
    for i in range(5):
      plt.text(X[i,0],X[i,1],'('+str(round(X[i,0],2))+','+str(round(X[i,1],2))+')')
    #end for

    #Vamos desenhar a reta x=c
    plt.plot([c,c],[ymin-.25*yscale,ymax+.25*yscale])

    for i in I:
      plt.plot([c],[i],'o')
      plt.text(c,i,'('+str(round(c,2))+','+str(round(i,2))+')')
    #end for

    plt.show()
  #end if

  return I

#end def