import time
import numpy as np
from random import randint as ale
def gerar_matriz_tridiagonal(ordem):#funcao para gerar matriz aleatoria
    mat = ""
    for lin in range(ordem):
        for col in range(ordem + 1):
            if(lin == col): mat += str(ale(1, 10)) + ".0,"
            elif(col == ordem) | (lin == col +1) | (lin == col -1): mat += str(ale(1, 10)) + ".0,"
            else: mat += ".0,"
        mat += ';'
    return np.matrix(mat[:-1])
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
def retroSubs(A, tmp,tol=10e-10):
    t = A.shape
    retorno = [];
    l_nul = checar_linhas_nulas(A) #fator de correcao aplicado para evitar erros com linhas nulas
    variaveis = (t[0] - l_nul)*[0] #lista que armazena os valores das variaveis

    if(t[0] - l_nul != t[1] - 1): return "Nao e possivel calcular o valor das variaveis"
    #dois loops para acessar os valores da matriz escalonada do final para o comeco
    for i in reversed(range(t[0] - l_nul)):
        for j in reversed(range(t[1])):
            if(j == (t[1] - 1)): variaveis[i] += A[i,j] #caso seja o valor independente soma no valor da variavel
            elif(j!=i): variaveis[i] -= variaveis[j] * A[i,j] #caso seja um valor dependente de outra variavel realiza a multiplicao e subtrai o valor
        
        
        variaveis[i] /= A[i,i] #divide pelo coficiente que multiplica a variavel para obter o valor dela
        if(abs(variaveis[i]) <= tol): variaveis[i] = 0 # caso a variavel esteja com valor abaixo da tolerancia torna-o 0
    for v in range(t[0] - l_nul):
        variaveis[v] = round(variaveis[v], 4) #Arredondando os valores pra 4 casas decimais
        retorno = variaveis
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
    return retroSubs(A,te) #Retornando o resultado da função de retrosubstituicao
def mtd_thomas(A):
    te = time.time();
    retorno = []
    t = A.shape
    d_pr = [] #variavel para diagonal principal
    d_ci = [] #variavel para diagonal acima da principal
    d_ba = [0] #variavel para diagonal abaixo da principal
    termos_ind = [] #variavel para os temos independentes
    for i in range(t[0]): #loop para obter as diagonais e os termos independentes
        if(i == 0): 
            d_ba += [A[i+1,i]]
            
        elif i == (t[0] -1): 
            d_ci+=[A[i -1,i]]
        else:
            d_ba += [A[i + 1,i]]
            d_ci += [A[i - 1,i]]
        d_pr += [A[i,i]]
        termos_ind += [A[i,t[1] -1]]
    d_ci+=[0]
    # Dividindo a primeira linha pelo primeiro item da diagonal principal
    d_ci[0] /= d_pr[0]
    termos_ind[0] /= d_pr[0]
    
    #Loop para fazer calcular coeficientes referentes a diagonal de cima e aos termos independentes
    for i in range(1, t[0]):
        fator = d_pr[i] - (d_ba[i] * d_ci[i-1])
        d_ci[i] /= fator
        termos_ind[i] = (termos_ind[i] - d_ba[i] * termos_ind[i-1])/fator

    
    variaveis = t[0]*[0]
    #Obtendo o valor das variaveis na ordem correta, por isso com coeficientes negativos
    variaveis[-1] = termos_ind[-1]
    for i in range(-2,-t[0]-1,-1):
        variaveis[i] = termos_ind[i] - d_ci[i] *  variaveis[i+1]
    
    for v in range(t[0]):
        variaveis[v] = round(variaveis[v], 4) #Arredondando os valores pra 4 casas decimais
        retorno = variaveis
    return retorno


