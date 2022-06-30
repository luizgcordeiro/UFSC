import matplotlib.pyplot as plt
import numpy as np
import time

def colinearidade(A): #essa funcao verifica a colinearidade dos pontos na matriz recebida
    tam = A.shape
    A = np.matrix(A)
    #Este codigo calcula a determinante para uma matriz com cada combinacao possivel entre 3 pontos recebidos em A
    #A matriz sempre tem sua ultima coluna com elementos iguais a 1
    for i in range(tam[0]):
        Ps = np.array(3*[[0.0,0.0,1.0]])
        for j in range(i+1,tam[0]):
            for z in range(j+1,tam[0]):
                Ps[0,0],Ps[0,1] = A[i, 0], A[i, 1]
                Ps[1,0],Ps[1,1] = A[j, 0], A[j, 1]
                Ps[2,0],Ps[2,1] = A[z, 0], A[z, 1]
                det = determinante_O3(Ps)
                if(det == 0): return 1  #retorna 1 caso alguma determinante for igual a 0, indicando colinearidade
    return 0 # retorna 0 caso todos os pontos forem nao colineares
def determinante_O3(A): #funcao que calcula determinante de ordem 3
    return A[0][0]*A[1][1]*A[2][2] + A[0][1]*A[1][2]*A[2][0] + A[0][2]*A[1][0]*A[2][1] - A[2][0]*A[1][1]*A[0][2] - A[2][1]*A[1][2]*A[0][0] - A[2][2]*A[1][0]*A[0][1]
def determinante_O2(A):#funcao que calcula determinante de ordem 2
    return A[0][0]*A[1][1] - A[1][0]*A[0][1]

#inicio das funcoes para a eliminacao gaussiana
def subt_linhas(A, l1, l2, quo,tol=10e-10):
    #Realiza a subtracao: l1 - quo * l2 (elemento a elemento)
    for j in range(A.shape[1]):
        A[l1,j] -= quo * (A[l2,j])
        if(abs(A[l1,j]) < tol): A[l1,j] = 0 #Checa se o numero e maior que a tolerancia, senao for torna-o 0
def troca_linhas(A, l1, l2): #Funcao que troca de lugar l1 e l2
    cp_l1 = A[l1].copy()
    cp_l2 = A[l2].copy()
    
    A[l1] = cp_l2
    A[l2] = cp_l1
def checar_linhas_nulas(A,tol=10e-10):
    l_nul = 0 #variavel para quantidade de linhas nulas
    t = A.shape
    #Dois loops para checar todos os termos da matriz linha a linha
    for i in range(t[0]):
        ele_n_nulo = 0 #variavel para quantidade de elemento nao nulos
        for j in range(t[1] - 1): #Nao checa o termo independente
            if(abs(A[i,j]) > tol): ele_n_nulo = 1
        if(ele_n_nulo == 0): l_nul += 1
    return l_nul
def retroSubs_dp(A, tol=10e-10):
    t = A.shape
    l_nul = checar_linhas_nulas(A) #fator de correcao aplicado para evitar erros com linhas nulas
    variaveis = (t[0] - l_nul)*[0] #lista que armazena os valores das variaveis
    
    variaveis_att= t[0]*[0] #lista que armazena quais variaveis da matriz foram atualizadas
    variaveis = t[0]*[0] #lista que armazena o valor das variaveis
    #dois loops para acessar os valores da matriz escalonada do final para o comeco, exceto a coluna do termo independente
    for i in reversed(range(t[0] - l_nul)):
        for j in reversed(range(t[1] - 1)):
            coeficiente = A[i,j] #obtendo o coeficiente da variavel
            if(abs(coeficiente) > tol): #Se o coeficiente for diferente de 0 
                if((i != j)): #e se nao for o coeficiente da propria variavel
                    if(variaveis_att[j] == 0): variaveis[j] = 1.0; #chuta o valor "1" para uma variavel que ainda nao foi atualizada, mas que outra variavel depende de seu valor
                    variaveis[i] -= variaveis[j]*coeficiente #como e um valor dependente de outra variavel realiza a multiplicao e subtrai o valor
                variaveis_att[j] = 1 #definindo que a variavel foi atualizada
        variaveis[i] += A[i, t[1] - 1] #somando o valor independente
                
    return variaveis
def retroSubs(A, tmp,tol=10e-10):
    t = A.shape
    retorno = [];
    l_nul = checar_linhas_nulas(A) #fator de correcao aplicado para evitar erros com linhas nulas
    variaveis = (t[0] - l_nul)*[0] #lista que armazena os valores das variaveis
    if(t[0] - l_nul != t[1] - 1): #Verificando se temos linhas nao nulas suficientes para obter o valor das variaveis
        #Realizando retrosubstituicao incompleta
        variaveis_dp = A.copy() 
        variaveis_att = t[1] * [0] #lista que armazena quais variaveis da matriz foram atualizadas
        #dois loops para acessar os valores da matriz escalonada do final para o comeco
        for i in reversed(range(t[0] - l_nul)): 
            for j in reversed(range(t[1])):
                variaveis_dp[i, j] = A[i,j]/A[i,i] #dividindo a linha pelo valor do item da linha que esta na diagonal principal
                if(variaveis_att[j] == 1): # Se a variavel da coluna ja foi atualizada, subtrai o valor que representa do termo independente e torna o seu coeficiente 0
                    for v in reversed(range(t[1])):
                        if(v == j): variaveis_dp[i, v] = 0 #tornando o coeficiente 0
                        elif(abs(variaveis_dp[i,j]) > tol): 
                            a = variaveis_dp[j, v] #obtendo o valor da variavel
                            b = variaveis_dp[i,j] #coeficiente da variavel na linha atual
                            variaveis_dp[i, v] -= a*b #subtrai o valor do termo independente
            variaveis_att[i] = 1 #guardando a informacao de que foi atualizada
        return variaveis_dp
    else:
        #dois loops para acessar os valores da matriz escalonada do final para o comeco
        for i in reversed(range(t[0] - l_nul)):
            for j in reversed(range(t[1])):
                if(j == (t[1] - 1)): variaveis[i] += A[i,j] #caso seja o valor independente soma no valor da variavel
                elif(j!=i): variaveis[i] -= variaveis[j] * A[i,j] #caso seja um valor dependente de outra variavel realiza a multiplicao e subtrai o valor
            
            
            variaveis[i] /= A[i,i] #divide pelo coficiente que multiplica a variavel para obter o valor dela
            if(abs(variaveis[i]) <= tol): variaveis[i] = 0 # caso a variavel esteja com valor abaixo da tolerancia torna-o 0
        for v in range(t[0] - l_nul):
            retorno += [variaveis[v]] 
        #print("Metodo Gaussiano - Tempo de execucao: " + str(time.time() - tmp) + "s") #Impressao do tempo de execucao
        return retorno
                
def escalonamento(A,tol=10e-10):
    te = time.time(); # Marca o inicio do tempo do processo de escalonamento
    A = np.matrix(A)
    t = A.shape #Guarda o tamanho da matriz
    pivo = 0
    l_pivo = -1 #variavel para linha do pivo atual
    for i in range(t[0]): #loop para passar por todas as linhas
        pivo = A[i,i]
        cont = i + 1
        while (abs(pivo) <= tol) & (cont < t[0]): #loop para encotrar o pivo
            A[i,i] = 0; #definindo pra 0 ja que menor que tolerancia
            troca_linhas(A, i, cont)
            pivo = A[i,i]
            cont+=1
        l_pivo = i
        
        #loop para subtrair a linha do pivo das outras linhas de baixo, de modo que os elementos abaixo do pivo sejam zerados
        for l in range(i,t[0]): 
            if(l != i) & (abs(pivo) > tol): subt_linhas(A, l, i, (A[l, l_pivo]/ pivo)) 
    
    # Codigo pra imprimir a matriz escalonada
    #print("Matriz Escalonada:")
    #print(A, end = "\n")
    
    return retroSubs(A,te,tol) #Retornando o resultado da função de retrosubstituicao

#Fim da eliminacao gaussiana

#funcao conica recebe:
    #pontos: lista com 5 pontos no plano xy
    #dom_x: dominio de x para o grafico que sera gerado
    #p_graf: quantidade de pontos para o grafico
    #tol: tolerancia numerica da funcao
#Essa funcao imprime: os valores dos coeficientes e o termo independente  da conica que contem os pontos informados,
#O tipo dessa conica, e as interseccoes dessa conica com os eixos
#retorna o tempo de execucao total da funcao caso em caso de sucesso, caso algum erro seja encontrado retorna uma mensagem informando o erro
def conica(pontos, dom_x = [-1,-1], p_graf=1000, tol=10e-10):
  te = time.time()
  pontos = np.matrix(pontos)
  if(pontos.shape != (5,2)): return "Matriz de pontos invalida"
  if(colinearidade(pontos)): return "Os Pontos sao colineares"
  
  coeficientes = np.matrix(np.zeros((5,6), dtype=np.float64))
  tam = coeficientes.shape
  
  #Calculando os coeficientes de A,B,C,D,E para cada ponto
  #equacao: Ax² + Bxy + Cy² + 2Dx + 2Ey = -F
  for i in range(tam[0]):
      coeficientes[i, 0] = pontos[i, 0]*pontos[i, 0] 
      coeficientes[i, 1] = pontos[i, 0]*pontos[i, 1]
      coeficientes[i, 2] = pontos[i, 1]*pontos[i, 1]
      coeficientes[i, 3] = pontos[i, 0]*2
      coeficientes[i, 4] = pontos[i, 1]*2
      coeficientes[i, 5] = 1 #assumindo F = -1 para poder calcular os coeficientes
  r_cf = escalonamento(coeficientes,tol) #Chamando a funcao de escalonamento para obter os coeficientes A,B,C,D,E
  if(type(r_cf) == type(np.matrix(""))): #Verficando se o resultado do escalonamento foi uma matriz
      t = r_cf.shape
      #O metodo de escalonamento retorna uma matriz apenas quando nao consegue executar a retrosubstituicao completa(matriz com linhas nulas)
      #realizando a correcao do valor de F, porque como ha linhas nulas o valor F tem de ser nulo para a equacao "0x² + 0xy + 0y² + 2*0x + 2*0y = -F" ser verdadeira
      r_cf = np.delete(r_cf, t[1] - 1, 1) #removendo a coluna do F
      r_cf =  np.hstack((r_cf, np.atleast_2d(5*[0]).T)) #adicionando uma coluna de zeros para o F
      r_cf = retroSubs_dp(r_cf) # Realizando a retrosubstituicao em que as variaveis ficam dependentes de outras
      #o valor de retorno e uma solucao que resolve o sistema
      r_cf += [0] #Adicionando o valor de F ao conjunto de coeficientes da conica
  else: r_cf += [-1.0] #Adicionando o valor de F ao conjunto de coeficientes da conica

  #O código parece fazer sentido
  
  #imprimindo A,B,C,D,E,F
  print("Coeficientes da Conica e o termo independente(F): ")
  cont = 0
  for cf in r_cf:
      print("%c = %.7f" % (chr(65 + cont), cf))
      cont+=1
      
  #Matriz para descobrir se a conica e degenerada
  m_deg = np.array([[r_cf[0], r_cf[1], r_cf[3]],
                           [r_cf[1], r_cf[2], r_cf[4]],
                           [r_cf[3], r_cf[4], r_cf[5]]])
  if(determinante_O3(m_deg) == 0): return "Conica degenerada"
  
  #Matriz para descobrir o tipo de conica
  m_tipo_con = np.array([[r_cf[0], r_cf[1]],
                           [r_cf[1], r_cf[2]]])
  det_tipo = determinante_O2(m_tipo_con)
  if(abs(det_tipo) < tol): tipo_con = "Parabola"
  elif(det_tipo > 0): tipo_con = "Elipse"
  else: tipo_con = "Hiperbole"
  print("\nTipo da conica: %s" % tipo_con, end = "\n\n")
  
  #interseccoes: Os pontos de interseccao sao sempre raizes de parabolas ja que se x = 0, a equacao da conica se torna Cy² + 2Ey + F = 0
  # e se y = 0, Ax² + 2Dx + F = 0
  
  #interseccoes com eixo X
  print("Interseccoes com eixo X: ") 
  #definindo o chute
  if(abs(r_cf[0]) > tol):
      vertice = -r_cf[3]/r_cf[0] #vertice da parabola
      chuteX1 = vertice + tol
      chuteX2 = vertice - tol
  else: 
      chuteX1 = pontos[0,0]
      chuteX2 = pontos[0,0]
  #metodo de newton para Ax² + 2Dx + F = 0
  x1 = metodo_newton_conica(chuteX1, r_cf[0], r_cf[3], r_cf[5], 10e-12, 10000)
  x2 = metodo_newton_conica(chuteX2, r_cf[0], r_cf[3], r_cf[5], 10e-12, 10000)
  if("Erro" in str(x1)): print("Nao intercede o eixo X") #se algum erro ocorreu significa que a funcao nao tem interseccao no eixo
  elif(abs(x1 - x2) < tol): print("(%.6f, 0.000000)" % x1) # se o x1 e o x2 forem iguais imprime apenas 1 deles
  else:
      print("(%.6f, 0.000000)" % x1)
      print("(%.6f, 0.000000)" % x2)
      
      
  print("\nInterseccoes com eixo Y: ") 
  #definindo o chute
  if(abs(r_cf[2]) > tol): 
      vertice = -r_cf[4]/r_cf[2] #vertice da parabola
      chuteY1 = vertice + tol
      chuteY2 = vertice - tol
  else: 
      chuteY1 = pontos[0,1]
      chuteY2 = pontos[0,1]
  #metodo de newton para Cy² + 2Ey + F = 0
  y1 = metodo_newton_conica(chuteY1, r_cf[2], r_cf[4], r_cf[5], 10e-12, 10000)
  y2 = metodo_newton_conica(chuteY2, r_cf[2], r_cf[4], r_cf[5], 10e-12, 10000)
  if("Erro" in str(y1)): print("Nao intercede o eixo Y") #se algum erro ocorreu significa que a funcao nao tem interseccao no eixo
  elif(abs(y1 - y2) < tol): print("(%.6f, 0.000000)" % y1) #se o y1 e o y2 forem iguais imprime apenas 1 deles
  else:
      print("(%.6f, 0.000000)" % y1)
      print("(%.6f, 0.000000)" % y2)
      
  if(dom_x[0] == dom_x[1]): #definindo valor do dominio de x no grafico, caso nao tenha sido informado
      dom_x[0] = pontos[0,0] #valor inicial igual a coordenada x do primeiro ponto
      dom_x[1] = pontos[4,0] #valor final igual a coordenada x do ultimo ponto

  #Gerando o grafico da conica
  #O grafico e feito em duas curvas, ja que alguns valores de x podem ter 2 valores correspondentes em y e vice-versa
  x_c, x_b, y_c, y_b, t= [],[],[],[],[] #criando as variaveis para armazenar os pontos
  
  t = np.linspace(dom_x[0],dom_x[1], p_graf) #Lista com "p_graf" pontos dentro do intervalo que foi informado pelo usuario
  cont = 0
  i_ant = t[0]
  fig, ax = plt.subplots()
  for i in t: #loop para aplicar a funcao da conica em cada ponto de t
      
      yi = f_conica(r_cf[0],r_cf[1],r_cf[2],r_cf[3],r_cf[4],r_cf[5],i) #funcao da conica que retorna dois valores para o x informado
      if("Erro" not in str(yi)): #os pontos validos sao adicionados as listas
          if(abs(i - i_ant) >= 1): # caso tenha uma diferença entre pontos maior que 1, ele imprime uma parte curva
              ax.plot(x_c, y_c, color ='b')
              ax.plot(x_b, y_b, color ='b')
              x_c, x_b, y_c, y_b = [],[],[],[]
              
          if(abs(yi[0]) < tol): yi[0] = 0
          if(abs(yi[1]) < tol): yi[1] = 0
          x_c += [i]
          y_c += [yi[0]]
          x_b += [i]
          y_b += [yi[1]]
          i_ant = i
  #mostrando o grafico
  ax.plot(x_c, y_c, color ='b')
  ax.plot(x_b, y_b, color ='b')
  #adicionando os pontos de inteseccao ao grafico
  if("Erro" not in str(x1)) & ("Erro" not in str(y1)):
      if(abs(x1) < tol) | (abs(x2) < tol) | (abs(y1) < tol) | (abs(y2) < tol):
          ax.plot(0, 0, marker = 'o')
          ax.annotate("  Int. eixo x e y:\n  (%.2f, %.2f)" %(0,0), xy=(0,0))
  if("Erro" not in str(x1)):
      if(abs(x1) > tol):
          ax.plot(x1, 0, marker = 'o')
          ax.annotate("  Int. eixo x:\n  (%.2f, %.2f)" %(x1,0), xy=(x1,0))
  if("Erro" not in str(x2)):
      if(abs(x2) > tol):
          ax.plot(x2, 0, marker = 'o')
          ax.annotate("  Int. eixo x:\n  (%.2f, %.2f)" %(x2,0), xy=(x2,0))
  if("Erro" not in str(y1)):
      if(abs(y1) > tol):
          ax.plot(0, y1, marker = 'o')
          ax.annotate("  Int. eixo y:\n  (%.2f, %.2f)" %(0,y1), xy=(0,y1))
  if("Erro" not in str(y2)):
      if(abs(y2) > tol):
          ax.plot(0, y2, marker = 'o')
          ax.annotate("  Int. eixo y:\n  (%.2f, %.2f)" %(0,y2), xy=(0,y2))
  #adicionando os pontos iniciais
  for pot in pontos:
      pt = [pot[0,0],pot[0,1]]
      ax.plot(pt[0],pt[1], marker = 'o')
      ax.annotate("  (%.2f, %.2f)" %(pt[0],pt[1]), xy=(pt[0],pt[1]))
  print("\nGrafico gerado para x no intervalo: [%.2f, %.2f]" % (dom_x[0], dom_x[1]))
  plt.show()
  return "Tempo de Execucao: %.7f" % (time.time() - te)



# funcao de parabola que tem as mesmas interseccoes com um eixo que a funcao da conica
#coeficientes recebidos sao A e D(no caso de y = 0) ou C e E(no caso de x = 0), juntos ao termo independente e por fim o x
def f(C_q, C_l, T_i, x): 
    return C_q*x*x + 2*C_l*x + T_i

def df(C_q, C_l, x): # derivada da funcao parabola
    return 2*C_q*x + 2*C_l
def metodo_newton_conica(x0,C1,C2,Ti, erro, itmax): #metodo de newton que recebe coeficientes da conica e repassa para funcao e a derivada
    cont_it = 0
    x_at = x0
    x_ant = x0
    er = erro + 1
    while(cont_it < itmax) & (er >= erro):
        x_ant = x_at
        funcao = f(C1,C2,Ti,x_ant)
        derivada = df(C1,C2,x_ant)
        if(abs(derivada) <= erro): return "Erro: divisao por zero"
        x_at = x_ant - funcao/derivada
        er = abs((x_at-x_ant))
        cont_it+=1
    if(cont_it != itmax): return x_at
    else: return "Erro: Max Iteracoes"

#funcao da conica, recebe todos os coeficientes, o termo independente e o x
#retorna 2 possiveis valores para y(esses valores podem ser identicos)
def f_conica(A,B,C,D,E,F,x): 
    result = A*x*x + 2*D*x + F
    b = (B*x + 2*E)/2
    chute = 0
    if(abs(C) > 10e-10): chute = -b/C #vertice
    return [metodo_newton_conica(chute + 1, C, b, result, 10e-10, 10000), metodo_newton_conica(chute -1, C, b, result, 10e-10, 10000)]
