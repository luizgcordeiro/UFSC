import time
from random import seed, randint

def f(constante, numerador, x):
    """
    Função utilizada nos metodos iterativos para encontrar constante n de um numero
    Quando retorna 0, o x é a constante n do numerador
    
    Recebe:
        constante: indice da constante
        numerador: numero dentro da constante
        x: um valor aproximado para a constante
        
    Retorna:
        x^numerador - constante
    """
    return x**numerador - constante

def df_exata(numerador,x):
    """
    Derivada exata da função f para o metodo iterativo de newton
    
    Recebe:
        numerador: numero dentro da constante
        x: um valor aproximado para a constante
        
    Retorna:
        x^numerador - constante
    """
    return numerador*(x**(numerador-1))


def df_prox(constante, numerador,x_atual, x_anterior, tol):
    """
    Derivada aparoximada da função f para os metodo iterativos da secante
    
    Recebe:
        constante: indice da constante
        numerador: numero dentro da constante
        x_atual: um valor aproximado para a constante no passo atual 
        x_anterior: um valor aproximado para a constante no anterior
        tol: tolerancia maxima 
        
    Retorna:
        derivada aproximada
    """
    dx = (x_atual - x_anterior)
    
    if(abs(dx) < tol): 
        return 0
    
    return (f(constante,numerador,x_atual) - f(constante,numerador,x_anterior))/dx


def bissecao(constante, numerador, tol, iteracoes_maxima):
    """
    Metodo da Bissecao para calcular constante de uma funcao
    
    Recebe:
        constante: indice da constante
        numerador: numero dentro da constante
        tol: tolerancia maxima aceita
        iteracoes_maxima: numero maximo de iterações
        
    Retorna:
        constante da funcao, nuemro de iteracoes, erro
    """
    
    
    if(constante < 0) and (numerador % 2 == 0): 
        return "Erro", 0, 0
    
    #define o intervalo de busca
    if(abs(constante) < 1): 
        intervalo = [-1, 1]
    elif(constante > 0): 
        intervalo = [0, constante]
    else: 
        intervalo = [constante, 0] #intervalo para constante negativa
        
    erro = abs((intervalo[1]-intervalo[0])/2.0)
    contador = 0
    
    while(contador < iteracoes_maxima):
        
        if(abs(intervalo[0] - intervalo[1]) < tol):
            return intervalo[0], contador+1, erro
        
        #determina o valor medio no intervalo de busca
        media = abs(intervalo[1] - intervalo[0])/2 + intervalo[0]
        
        # encontra os valores de y na funcao 
        inicial = f(constante,numerador,intervalo[0])
        meio = f(constante,numerador,media)
        final = f(constante,numerador,intervalo[1])
                    
        
        if(abs(inicial) < tol): 
            return intervalo[0], contador +1, erro
        elif(abs(meio) < tol): 
            return media, contador +1, erro
        elif(abs(final) < tol): 
            return intervalo[1], contador +1, erro
        
        
        if(final*meio < 0): 
            intervalo[0] = media
        else: 
            intervalo[1] = media
        contador += 1
        
        erro = abs(intervalo[1]-intervalo[0])/2.0
        
    return "Erro", 0, 0
        
    
       
def newton(x0, constante, numerador, tol, iteracoes_maxima):
    """
    Metodo de newton para calcular constante de uma funcao
    
    Recebe:
        x0: chute inicial
        constante: indice da constante
        numerador: numero dentro da constante
        tol: tolerancia maxima aceita
        iteracoes_maxima: numero maximo de iterações
        
    Retorna:
        constante da funcao, nuemro de iteracoes, erro
    """
    
    contador = 0
    x_atual = x0
    x_anterior = x0 - 1
    
    erro = abs(x_atual - x_anterior)
    
    
    while((contador < iteracoes_maxima) and (erro>tol)):
        
        x_anterior = x_atual
        funcao = f(constante,numerador,x_anterior)
        derivada = df_exata(numerador,x_anterior)
        
        if(abs(derivada) <= tol): 
            return x_anterior, contador + 1, erro
        
        x_atual = x_anterior - funcao/derivada
        contador += 1
        
        erro = abs(x_atual - x_anterior)
        
    if(contador != iteracoes_maxima): 
        return x_atual, contador + 1, erro
    else: 
        return "Erro", 0, 0


def secante(x0, constante, numerador, tol, iteracoes_maxima):
    """
    Metodo da secante para calcular constante de uma funcao
    
    Recebe:
        x0: chute inicial
        constante: indice da constante
        numerador: numero dentro da constante
        tol: tolerancia maxima aceita
        iteracoes_maxima: numero maximo de iterações
        
    Retorna:
        constante da funcao, nuemro de iteracoes, erro
    """
    
    contador = 0
    x_atual = x0
    x_anterior = x0 - 1
    
    erro = abs(x_atual - x_anterior)
    
    while((contador < iteracoes_maxima) and (abs(f(constante,numerador,x_atual)) > tol)):
        
        funcao = f(constante, numerador, x_atual)
        derivada = df_prox(constante, numerador, x_atual, x_anterior, tol)
        
        if(derivada < tol): 
            return x_anterior, contador + 1, erro
        
        x_anterior = x_atual
        x_atual = x_anterior - funcao/derivada
        contador += 1
        erro = abs(x_atual - x_anterior)
        
    
    if(contador != iteracoes_maxima): 
        if(abs(f(constante, numerador, x_atual)) > tol): return "Erro",0, 0 #erro ocasionado pelo limite de armazenamento do float, fazendo com que convirja de forma errada
        return x_atual, contador + 1, erro
    else: 
        return "Erro",0, 0
    
def raiz_n(x,n,tol=10e-12):
    return newton(x, x, n, tol, 2000)[0]
