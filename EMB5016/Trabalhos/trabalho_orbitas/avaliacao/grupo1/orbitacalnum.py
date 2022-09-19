import numpy as np
import matplotlib.pyplot as plt


def bisection(f, a, b, n=0, tol=1.0e-14):
    # Testando se um dos pontos escolhidoss é solução para a função
    if abs(f(a)) < tol:
        return a
    if abs(f(b)) < tol:
        return b

    #Testando se o intervalo escolhido possui dois valores de sinais diferentes
    if f(a) * f(b) > 0:
        return None
    #Criterio de parada: o método irá se repitir até que o intervalo entre a e b for menor que a tolerancia
    while abs(b - a) > tol:
        #Para x é atribuido o valor da média entre os pontos iniciais
        x = (a + b) / 2
        n += 1
        #Algorítimo checa em qual intervalo a função cruza o eixo x e atualiza o valor de a ou b
        if f(a) * f(x) < 0:
            b = x
        else:
            a = x
        #end else if

    return x

#aqui calcula-se o y, para isso isolou-se x 
def funcao_conica(coef, x, tol=1.0e-12):
    a = coef[2]
    b = 2 * coef[1] * x + 2 * coef[4]
    c = (coef[0] * x * x + 2 * coef[3] * x + coef[5])

    def parabola(w):
        return a * w * w + b * w + c

    if (abs(a) > tol):
        vertice = -b / (2 * a)
        return [
            bisection(parabola, -10, vertice),
            bisection(parabola, vertice, 10)
        ]
    else:
        y = c / b
        return [y, y]
    return (1 / 2) * (x + (y / x))


# escalonamento de matriz
def escalona(A, tol=1.0e-20, verbose=False):
    """
    Recebe:
        A: a matriz a ser escalonada
        tol: tolerancia numérica suportada 
        verbose: se TRUE imprime o passo a passso da função
        
    Retorna:
        A: a matriz A escalonada
    """

    n = len(A)

    if verbose: print(A)

    # escalonamento para cada uma das colunas
    for c in range(n - 1):

        if verbose:
            print("\n\n--------------------")
            print("Eliminaçãoo Gaussiana na coluna %d." % c, end="\n")

        #Procuro um Pivô
        p = c
        while abs(A[p, c]) < tol and p < n - 1:
            p += 1
            assert (abs(A[p, c]) > tol), "O Pivo não nulo o algoritimo falha\n"

        # Se for necessário, troca linhas!
        if p == c:
            if verbose:
                print("Pivo A[%d,%d] = %.6g, não preciso trocar as linhas\n" %
                      (p, c, A[p, c]))
            else:
                # o pivo não está na linha atual faço uma troca de linhas
                if verbose:
                    print(
                        "Pivo A[%d,%d] = %.6g, trocando as linhas %d <=> %d\n"
                        % (p, c, A[p, c], p, c))
                x = -A[c].copy()

                A[c] = A[p]
                A[p] = x

            # Faz o escalonamento para coluna c
            if verbose: print('')
            for l in range(c + 1, n):
                coef = A[l, c] / A[c, c]
                if verbose:
                    print("E_%d - %.2f E_%d -> E_%d)" % (l, coef, c, l))
                A[l] = A[l] - coef * A[c]
            if verbose: print(A, "\n\n")

    return A


# Substituição regressiva
def subs_regressiva(A, verbose=False):

    n = len(A)
    #Substituição Regressiva

    if verbose:
        print("\n\n--------------------")
        print("Substituição Regressiva\n")

    x = [0] * n
    if (A[n - 1, n - 1] == 0):
        x[n - 1] = 1
    else:
        x[n - 1] = (A[n - 1, n]) / A[n - 1, n - 1]

    if verbose:
        print("x_%d = %.6g / %.6g = %.6g" %
              (n - 1, A[n - 1, n], A[n - 1, n - 1], x[n - 1]))

    for i in range(n - 2, -1, -1):
        s = 0
        strsoma = ""
        if verbose: print("x_%d = " % (i), end='')
        for j in range(i + 1, n):
            s += A[i, j] * x[j]
            if verbose: strsoma += "%.6g x_%d + " % (A[i, j], j)

        if (A[i, i] == 0):
            x[i] = 1
        else:
            x[i] = (A[i, n] - s) / A[i, i]

        if verbose:
            print("(%.6g - (%s) )/ %.6g = %.6g" %
                  (A[i, n], strsoma, A[i, i], x[i]))
        if verbose: print("{} \n".format(x))

    return x


# Eliminação Gaussiana
def eliminacao_guassiana(A, verbose=False):
    """
    Algoritimo de Eliminação Gaussiana
    
    Recebe:
        A       => Matriz aumentada de coeficientes
        verbode => Imprime passo a passo?
        
    Retorna:
        x       => Vetor solução
    """
    size = A.shape
    assert (size[0] < size[1]), "Matriz invá¡lida"

    A = escalona(A, 1.0e-10, verbose)
    x = subs_regressiva(A, verbose)

    return (x)


# define se a conica é uma parabola, hiperbole ou elipse
def tipo_conica(a, b, c, tol=10e-2):
    det = a * c - b * b
    if (abs(det) < tol):
        return "parabolica"
    elif (det > 0):
        return "eliptica"
    else:
        return "hiperbolica"


# cria minha matriz com os coeficientes 
def coef_conica(A):
    pontos = np.matrix(A)
    matriz_coef = np.zeros((A.shape[0], 5))
    b = A.shape[0] * [10]
    for indice in range(A.shape[0]):
        x = pontos[indice, 0]
        y = pontos[indice, 1]
        matriz_coef[indice, 0] = x * x
        matriz_coef[indice, 1] = 2 * x * y
        matriz_coef[indice, 2] = y * y
        matriz_coef[indice, 3] = 2 * x
        matriz_coef[indice, 4] = 2 * y

    matriz_transposta = np.transpose(matriz_coef)
    matriz_coef = np.dot(matriz_transposta, matriz_coef)
    b = np.dot(matriz_transposta, b)

    matriz_aum = np.zeros((5, 6))
    for l in range(5):
        for c in range(6):
            if (c == 5): matriz_aum[l, c] = b[l]
            else: matriz_aum[l, c] = matriz_coef[l, c]

    coeficientes = eliminacao_guassiana(matriz_aum)
    coeficientes += [-10]
    return coeficientes

#aqui define-se as distancias entre os pontos, através da média entre eles
def estima(coef, pontos):
    distancia_de_ponto = (pontos[-1, 0] - pontos[-6, 0]) / 4
    previsoes = np.zeros((3, 2))
    for i in range(1, 4):
        previsoes[i - 1, 0] = pontos[-1, 0] + i * distancia_de_ponto

        ys = funcao_conica(coef, previsoes[i - 1, 0])
        if (ys[0] != None) and (ys[1] != None):
            if (abs(ys[0] - pontos[-1, 1]) < abs(ys[1] - pontos[-1, 1])):
                previsoes[i - 1, 1] = ys[0]
            else:
                previsoes[i - 1, 1] = ys[1]
        elif (ys[0] != None):
            previsoes[i - 1, 1] = ys[0]
        elif (ys[1] != None):
            previsoes[i - 1, 1] = ys[1]
    return previsoes

#função para plotar as orbitas
def orbita(A, mostrar=True):

    coef = coef_conica(A)
    tipo = tipo_conica(coef[0], coef[1], coef[2])
    prev = estima(coef, A)


#plota o gráfico da funcao e os pontos importantes
    
    if(mostrar == True):
      t = np.linspace(-10,10, 11000)
      distancia_de_erro = abs(15*(t[1] - t[0]))
      ant = t[0]
      curva1_x = []
      curva1_y = []
      curva2_x = []
      curva2_y = []
      fig, ax = plt.subplots()
      for i in t:
        ys = funcao_conica(coef, i)
        if(abs(i - ant) > distancia_de_erro):
          ax.plot(curva1_x, curva1_y, color='r')
          ax.plot(curva2_x, curva2_y, color='r')
          curva1_x = []
          curva1_y = []
          curva2_x = []
          curva2_y = []
        if(ys[0] != None):
          curva1_x += [i]
          curva1_y += [ys[0]]
          ant = i
        if(ys[1] != None):
          curva2_x += [i]
          curva2_y += [ys[1]]
          ant = i
      
      
      ax.annotate("    Comeco",  xy=(A[0,0], A[0,1]))
      ax.annotate("    Final",  xy=(A[-1,0], A[-1,1]))
      for indi in range(A.shape[0]):
        ax.plot(A[indi,0], A[indi,1], marker='o', color = '0')
      ax.annotate("    Previsoes",  xy=(prev[0,0], prev[0,1]))
      for indi in range(prev.shape[0]):
        ax.plot(prev[indi,0], prev[indi,1], marker='v', color = 'b')
      plt.show()
    return [tipo, prev]
