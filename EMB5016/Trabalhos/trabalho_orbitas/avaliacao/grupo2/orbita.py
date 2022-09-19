import matplotlib.pyplot as plt
import numpy as np
import radiciacao as raiz
import eliminacao_gaussiana as gauss
def determinante_O2(A):#funcao que calcula determinante de ordem 2
    return A[0][0]*A[1][1] - A[1][0]*A[0][1]

def erro(v): 
    """
    Funcao que checa se existe algum erro no argumento v.
    
    Argumentos:
        v: argumento a ser checado.
        
    Retorno:
        Retorna uma string contendo o erro, ou retorna False caso nao seja encontrado um erro
    """
    if("Erro" in str(v)):
        return str(v)
    return False
def f_par(a, b, c,x): 
    """
    Funcao que representa uma funcao matematica de parabolica.
    
    Recebe:
        a: coeficiente do termo quadratico da parabolica
        b: coeficiente do termo quadratico da parabolica
        c: termo independente da parabolica
        
    Retorna:
        a*x*x + 2*b*x + c
    """
    return a*x*x + 2*b*x + c

def df_par(a, b, x): # derivada da funcao parabolica
    """
    Funcao que representa uma funcao matematica de parabolica.
    
    Recebe:
        a: coeficiente do termo quadratico da parabolica
        b: coeficiente do termo quadratico da parabolica
        
    Retorna:
        2*a*x +2*b
    """
    return 2*a*x + 2*b
def metodo_newton_par(x0,a,b,c, tol, itmax, df_0 = False): #metodo de newton que recebe coeficientes da conica e repassa para funcao e a derivada
    """
    Metodo de newton para calcular uma raiz de uma funcao parabolica
    
    Recebe:
        x0: chute inicial
        a: coeficiente do termo quadratico da parabolica
        b: coeficiente do termo quadratico da parabolica
        c: termo independente da parabolica
        tol: tolerancia
        itmax: numero maximo de iterações
        df_0 (opcional): valor booleano que autoriza um retorno especial
    Retorna:
        Retorna a raiz da funcao caso encontre-a. 
        Se atingir o numero maximo de iteracoes retorna uma mensagem de erro
        informando; se a derivada da funcao for 0 no ponto e df_0 for True,
        retorna o valor de x nesse ponto, se df_0 for False retorna um erro.
    """
    cont_it = 0
    x_at = x0
    x_ant = x0
    erro = 1
    while(cont_it < itmax) & (erro >= tol):
        x_ant = x_at
        funcao = f_par(a,b,c,x_at)
        derivada = df_par(a,b,x_at)
        if(abs(derivada) <= tol):
            if(df_0): return x_at
            else: return "Erro: Divisao por zero"
        
        x_at = x_at - funcao/derivada
        erro = abs((x_at-x_ant))
        
        cont_it+=1
        
    if(cont_it != itmax): return x_at
    else:
        return "Erro: Max Iteracoes"

def f_conica(A,B,C,D,E,F, x, div_zero = False, tol=10e-14): 
    """
    Funcao que representa uma funcao matematica de uma conica:
    A*x*x + 2*B*x*y + C*y*y + 2*D*x + 2*E*y + F = 0
    Recebe:
        A: coeficiente do termo quadratico de x
        B: coeficiente do termo linear misto
        C: coeficiente do termo quadratico de y
        D: coeficiente do termo linear de x
        E: coeficiente do termo linear de y
        F: termo independente
        
    Retorna:
        Dois valores possiveis de y para resolver a equacao. Esses valores
        podem ser iguais.
    """
    parte_independente = A*x*x + 2*D*x + F
    b = (B*x + E)
    chute = 0
    #Condicoes para o chute
    if(abs(C) > tol): chute = -b/C #vertice
    elif(abs(b) > tol): chute = -parte_independente/2*b
    return [metodo_newton_par(chute + 1, C, b, parte_independente, tol, 100,div_zero), metodo_newton_par(chute -1, C, b, parte_independente, tol, 100,div_zero)]
def rotacao_ponto(ponto,rad):
    """
    Funcao que rotaciona um ponto de uma conica em 'rad' radianos
    Recebe:
        ponto: ponto a ser rotacionado na forma (x,y)
        rad: valor de radianos que o ponto deve ser rotacionado
    Retorna:
        Coordenandas do ponto rotacionado
    """
    x,y = ponto[0], ponto[1]
    novo_x = x*np.cos(rad) - y*np.sin(rad)
    novo_y = x*np.sin(rad) + y*np.cos(rad)
    return novo_x,novo_y


def conica_sem_B(A,B,C,D,E,F):
    """
    Funcao que encontra coeficientes de uma conica identica a recebida
    sem o termo B.
    Recebe:
        A: coeficiente do termo quadratico de x
        B: coeficiente do termo linear misto
        C: coeficiente do termo quadratico de y
        D: coeficiente do termo linear de x
        E: coeficiente do termo linear de y
        F: termo independente
    Retorna:
        O angulo em radianos em que a conica foi rotacionado para zerar o
        termo B, e os coeficientes A,B,C,D,E,F de uma conica (com B=0)
    """
    if(A == C): ang = np.pi/4
    else: ang = np.arctan(2*B/(A-C))/2
    cos = np.cos(ang)
    sin = np.sin(ang)
    _A = A*cos*cos + 2*B*cos*sin + C*sin*sin
    _B = 0
    _C = A*sin*sin - 2*B*sin*cos + C*cos*cos
    _D = (D*cos + E*sin)
    _E = (-D*sin + E*cos)
    return ang,_A,_B,_C,_D,_E,F
def dist_entre_pontos(ponto1, ponto2):
    """
    Funcao que calcula a distancia entre dois pontos.
    Recebe:
        ponto1: ponto na forma (x,y)
        ponto2: ponto na forma (x,y)
    Retorna:
        Valor da distancia entre os pontos
    """
    cateto1 = ponto1[0] - ponto2[0]
    cateto2 = ponto1[1] - ponto2[1]
    return raiz.raiz_n(cateto1*cateto1+cateto2*cateto2, 2)
def plot_con(coeficientes,tipo_con,pontos,estimativas,p_graf=1000, tol=10e-14):
    """
    Funcao que plota o grafico da orbita com os pontos dados e tambem as
    estimativas de posicoes nos proximos dias
    Recebe:
        coeficientes: lista com coeficientes de uma conica
        tipo_con: tipo da conica
        pontos: pontos recebidos da orbita
        estimativas: estimativas da posicao do objeto nos proximos dias
        p_graf (opcional): quantidade de pontos para o grafico da orbita
        tol (opcional): tolerancia
    Retorna:
        ---
    """
    
    A,B,C,D,E,F = coeficientes
    
    #O grafico e feito em diversas curvas, ja que alguns valores de x podem ter 2 valores correspondentes em y e vice-versa
    x_c, x_b, y_c, y_b, t= [],[],[],[],[] #criando as variaveis para armazenar os pontos
    
    
    c_q = (B*B - A*C)
    c_l = (2*B*E - 2*D*C)/2
    t_i = (E*E - C*F)
    fator_x0 = 0
    if(abs(c_q) > tol):fator_x0 = -c_l/c_q
    elif(abs(c_q) > tol): fator_x0 = -t_i/(2*c_l)
    encontro = [metodo_newton_par(fator_x0 -1, c_q, c_l, t_i, tol, 1000,True), "Erro",metodo_newton_par(fator_x0 +1, c_q, c_l, t_i, tol, 1000,True), "Erro"]
    
    if not erro(encontro[0]):
        encontro[1] = f_conica(A,B,C,D,E,F, encontro[0], True, tol)
        encontro[1] = encontro[1][0]
    if not erro(encontro[2]):
        encontro[3] = f_conica(A,B,C,D,E,F, encontro[2], True, tol)
        encontro[3] = encontro[3][0]
    fig, ax = plt.subplots()
    tam = pontos.shape[0]
    angulo,_A,_B,_C,_D,_E,_F = conica_sem_B(A,B,C,D,E,F)
    
    #definindo dominios de x e y e o foco orbitado para cada tipo de conica
    if(tipo_con == "parabolica"):
        if(abs(_C) <= tol): 
            vertice = (-_D/_A, ((-_D*_D)/_A + _F)/(-2*_E))
            foco_orbitado = (vertice[0], vertice[1] - _E/(2*_A))
            distancia_focal = abs(_E/(2*_A))
        else: 
            vertice = (((-_E*_E)/_C + _F)/(-2*_D),-_E/_C)
            foco_orbitado = (vertice[0] - _D/(2*_C), vertice[1])
            distancia_focal = abs(_D/(2*_C))
        vertice = rotacao_ponto(vertice, angulo)
        foco_orbitado = rotacao_ponto(foco_orbitado, angulo)
        dom_x= [foco_orbitado[0] - 6*distancia_focal, foco_orbitado[0] + 6*distancia_focal]
        dom_y= [foco_orbitado[1] - 6*distancia_focal, foco_orbitado[1] + 6*distancia_focal]
    else:
        centro = (-_D/(_A), -_E/(_C))
        termo = (-F + _D*_D/_A +_E*_E/_C)
        fatores_a_b = (termo/_C, termo/_A)
        foco_orbitado = (0,0)
        foco_2 = (0,0)
        
        #definindos os fatores a,b,c de acordo com a conica
        a = raiz.raiz_n(abs(fatores_a_b[0]),2)
        b = raiz.raiz_n(abs(fatores_a_b[1]),2)
        if(tipo_con == "hiperbolica"): c = raiz.raiz_n(a*a + b*b, 2)
        elif(tipo_con == "eliptica"): 
            if(a > b): 
                tmp = b
                b = a
                a = tmp
            c = raiz.raiz_n(-a*a + b*b, 2)
            
        #definindo o foco orbitado de acordo com a quantidade de pontos mais proximos a ele do que ao outro foco
        lado = -1 #variavel que armazena o coeficiente de c
        cont_vezes_perto_foco = 0
        if(fatores_a_b[0] > fatores_a_b[1]):
            for p in range(tam):
                x, y = rotacao_ponto((pontos[p,0],pontos[p,1]), -angulo)
                if(y > centro[1]): cont_vezes_perto_foco+=1
            if(cont_vezes_perto_foco > tam/2): lado =1
            foco_orbitado = (centro[0], centro[1] + c*lado)    
            foco_2 = (centro[0], centro[1] - c*lado)  

        else:
            for p in range(tam):
                x, y = rotacao_ponto((pontos[p,0],pontos[p,1]), -angulo)
                if(x > centro[0]): cont_vezes_perto_foco+=1
            if(cont_vezes_perto_foco > tam/2): lado =1
            foco_orbitado = (centro[0] + c*lado, centro[1])
            foco_2 = (centro[0] - c*lado, centro[1])
        
        #rotacionado os pontos
        foco_orbitado = rotacao_ponto(foco_orbitado, angulo)
        foco_2 = rotacao_ponto(foco_2, angulo)
        centro = rotacao_ponto(centro,angulo)
        
        #definindo os dominios para conforme o tipo de conica
        if(tipo_con == "hiperbolica"):
            menor = pontos[0,0]
            maior = pontos[0,0]
            for p in range(tam):
                x = abs(pontos[p,0])
                y = abs(pontos[p,1])
                if(abs(x - foco_orbitado[0]) > maior): maior = abs(x - foco_orbitado[0])
            if(maior <1): maior += 1
            dom_x= [foco_orbitado[0]-maior, foco_orbitado[0]+ maior]
            dom_y = [foco_orbitado[1]-maior, foco_orbitado[1]+ maior]
        else:
            if(a> b): maior = a*1.1
            else: maior = b*1.1
            dom_x = [centro[0] - (maior), centro[0] + (maior)]
            dom_y = [centro[1] - (maior), centro[1] + (maior)]
    
    t = np.linspace(dom_x[0],dom_x[1], p_graf) #Lista com "p_graf" pontos dentro do intervalo que foi informado pelo usuario
    
    dist_ponto = 1.1*abs(t[0] - t[1])
    cont = 0
    
    #corrigindo possiveis descontinuidades no grafico
    for i in t:
       i_ant = t[cont -1]
       if(not erro(encontro[1])):
          if(encontro[0] > i_ant) and (encontro[0] < i):
              t = np.insert(t, cont, encontro[0])
              cont+=1
       if(not erro(encontro[3])):
          if(encontro[2] > i_ant) and (encontro[2] < i):
              t = np.insert(t, cont, encontro[2])
          cont+=1
          
    i_ant = t[0]
    for i in t: #loop para aplicar a funcao da conica em cada ponto de t
    
        tol_graf= 10e-14
        valores_de_f = f_conica(A,B,C,D,E,F,i,1,tol_graf) 
        ponto_y0 = (i,valores_de_f[0])
        ponto_y1 = (i,valores_de_f[1])
       
        #os pontos validos sao adicionados as listas
        if not erro(valores_de_f): 
            if(abs(i - i_ant) >= dist_ponto): # caso tenha uma diferença entre pontos maior que 1, ele imprime uma parte curva
              ax.plot(x_c, y_c, color ='b')
              ax.plot(x_b, y_b, color ='b')
              x_c, x_b, y_c, y_b = [],[],[],[]
            if(tipo_con != "hiperbolica"): #se nao for uma hiperbolica adiciona os dois pontos as curvas
                x_c += [i]
                y_c += [valores_de_f[0]]
                x_b += [i]
                y_b += [valores_de_f[1]]
                i_ant = i   
            else: #se for uma hiperbolica impoe que o ponto a ser adicionado deve estar mais proximo do foco orbitado do que do outro foco
                if(dist_entre_pontos(foco_orbitado, ponto_y0) <= dist_entre_pontos(foco_2, ponto_y0)):
                    x_c += [i]
                    y_c += [valores_de_f[0]]
                    i_ant = i   
                if(dist_entre_pontos(foco_orbitado, ponto_y1) <= dist_entre_pontos(foco_2, ponto_y1)):
                    x_b += [i]
                    y_b += [valores_de_f[1]]
                    i_ant = i  
        
        #correcao de descontinuidades na curva
        if(not erro(encontro)) and (not erro(ponto_y0[1]) or not erro(ponto_y1[1])):
            if(abs(i - encontro[0]) < tol):
                x_c += [i]
                y_c += [encontro[1]]
                x_b += [i]
                y_b += [encontro[1]]
                i_ant = i
            elif(abs(i - encontro[2]) < tol):
                x_c += [i]
                y_c += [encontro[3]]
                x_b += [i]
                y_b += [encontro[3]]
                i_ant = i
            
    #plotando a ultima parte da curva
    ax.plot(x_c, y_c, color ='b')
    ax.plot(x_b, y_b, color ='b')
    
    #plotando os pontos da curva e as estimativas
    cor = 'g'
    for p in range(tam):
        x = pontos[p,0]
        y = pontos[p,1]
        ax.plot(x,y, marker = 'o', color=cor,linewidth=0.5)
        if(cor == 'g'): cor = 'y'
        elif(cor == 'y'): cor = 'b'
        else: cor ='g'
        if(p == 0): ax.annotate("    Inicio",  xy=(x,y))   
        elif(p == tam-1): ax.annotate("    Fim", xy=(x,y))  
    distancia_x_1dia = pontos[tam-1,0] - pontos[tam-2,0]

    for p in range(estimativas.shape[0]):
        x = estimativas[p,0]
        y = estimativas[p,1]
        ax.plot(x,y, marker = 'x', color='r')
        if(p==0):ax.annotate("Previsoes \n\n", xy=(x,y))
    ax.plot(foco_orbitado[0], foco_orbitado[1], marker = 'o')
    
    #modificando os limites do grafico para os dominios da orbita
    ax.set(xlim=(dom_x),ylim=(dom_y))
    plt.show()
    
def orbita(A,mostrar=True,tol=10e-4):
    """
    Obtem o tipo de orbita do objeto conforme os pontos recebidos em A,
    tambem faz estimativas da posicao do objeto e caso o argumento mostrar for
    True, gera o grafico da orbita com os pontos informados e as previsoes.
    Recebe:
        A: Array de dimensao 2, contendo os pontos de posicao do objeto
        mostrar (opcional): valor booleano que autoriza gerar o grafico da orbita
        tol (opcional): tolerancia
    Retorna:
        Uma Lista contendo uma string com o tipo de orbita, e um array de
        dimensao 2 contendo as previsoes para a posicao do objeto nos 3 proximos
        dias.
    """
    #Criando um sistema com uma equacao de conica para cada ponto
    
    pontos = np.matrix(A)
    ordem = pontos.shape[0] #quantidade de pontos
    matriz = np.zeros((ordem,5))
    b = ordem*[1] #termo independente, F= -1
    
    for i in range(ordem):
        matriz[i, 0] = pontos[i, 0]*pontos[i, 0]    #A
        matriz[i, 1] = pontos[i, 0]*pontos[i, 1]*2  #B
        matriz[i, 2] = pontos[i, 1]*pontos[i, 1]    #C
        matriz[i, 3] = pontos[i, 0]*2               #D
        matriz[i, 4] = pontos[i, 1]*2               #E
    
    #solucao de minimos quadrados
    transposta = np.transpose(matriz)
    matriz = np.dot(transposta, matriz)
    b = np.dot(transposta, b)
    
    #aplicando escalonamento para resolver o sistema
    matriz_estendida = np.hstack((matriz, np.atleast_2d(b).T))
    res = gauss.escalonamento(matriz_estendida)
    
    res+=[-1]
    A,B,C,D,E,F = res
    tipo_con = determinante_O2([[A,B],[B,C]]) #armazenando o valor da determinante que define o tipo de conica
    
    #definindo o tipo de conica
    if(abs(tipo_con) < tol): tipo_con = "parabolica"
    elif(tipo_con < 0): tipo_con = "hiperbolica"
    else: tipo_con = "eliptica" 
    
    #calculando as previsoes
    estimativas = np.ndarray((3,2),dtype=float)
    tam = pontos.shape[0]
    distancia_x_1dia = (pontos[tam-1,0] - pontos[tam-4,0])/3 #distancia media entre os pontos nos ultimos 3 dias
    for n in range(1,4):
        x = pontos[tam-1,0] + n*distancia_x_1dia
        y = f_conica(A,B,C,D,E,F, x)
        if(erro(y[0]) and erro(y[1])): #corrigindo falhas caso o ultimo ponto caia no vertice ou perto dele
            x = pontos[tam-1,0] - n*distancia_x_1dia
            y = f_conica(A,B,C,D,E,F, x)
        
        if(not erro(y)): #se existirem dois valores possiveis, faz os seguintes procedimentos
            ponto_y0 = (x,y[0])
            ponto_y1 = (x,y[1])
            ponto_final = (pontos[tam-1,0],pontos[tam-1,1])
            sentido_y = pontos[tam-1,1] - pontos[tam-2,1]
            
            #tendencias de movimento em y (aumentando ou diminuindo)
            dist_y0 = ponto_y0[1] - ponto_final[1]
            dist_y1 = ponto_y1[1] - ponto_final[1]
            
            #se as tendencias forem iguais, verifica qual ponto esta mais proximo ao foco
            if(dist_y0*dist_y1 > 0):
                if(dist_entre_pontos(ponto_y0, ponto_final) < dist_entre_pontos(ponto_y1, ponto_final)):
                    y = y[0]
                else: y = y[1]
            
            #se nao for, define o y de acordo com a tendencia de movimento
            elif(dist_y0*sentido_y > 0): y = y[0] 
            else: y = y[1]
        
        #se so existe um valor possivel, define y como este
        elif(not erro(y[0])): 
            y = y[0]
        else:
            y = y[1]
            
        estimativas[n-1][0] = x
        estimativas[n-1][1] = y
    if(mostrar): plot_con(res, tipo_con,pontos,estimativas,10000,tol)
    return [tipo_con, estimativas]




