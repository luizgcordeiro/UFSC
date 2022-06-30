import numpy as np
import matplotlib.pylab as plt

# Método do ponto  fixo
def ponto_fixo(f, coef, p0, tol, nmax, verbose=False):
    
    """
    Algoritimo do ponto fixo
    
    Recebe:
        f       => função a ser encontrada a raiz
        coef    => coeficientes da minha função
        p0      => Chute inicial
        tol     => tolerancia máxima permitida para o erro
        nmax    => número máximo de iterações
        verbose => Mostra passo a passo?
        
    Retorna: 
        p    => Raiz de f
    """
    
    assert tol>0, "Tolerancia deve ser maior que 0"
    assert nmax>0, "Numero máximo de iterações deve ser maior que 0"
    
    n=0
    if verbose:
        print("  n           p                erro")
        print(f"{n:3}       {p0:.6e}")
    
    n+=1 
    p_velho = p0
    p_novo = f(coef, p_velho)
    erro = abs(p_novo - p_velho)
    if verbose:
        print(f"{n:3}       {p_novo:.6e}        {erro:.3e}")
    
    #duas condiÃ§Ãµes de limite
    while erro>tol and n<nmax:
        n += 1
        p_velho = p_novo
        p_novo = f(coef, p_velho)
        erro = abs(p_novo-p_velho)
        if verbose:
            print(f"{n:3}       {p_novo:.6e}        {erro:.3e}")
            
    return p_novo


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
    
    n=len(A)
    
    if verbose: print(A)
        
    
    # escalonamento para cada uma das colunas
    for c in range(n-1):
        
        if verbose:
            print("\n\n--------------------")
            print("Eliminaçãoo Gaussiana na coluna %d." % c, end="\n")
        
        
        #Procuro um Pivô  
        p=c
        while abs(A[p,c])<tol and p<n-1:
            p+=1
            assert(abs(A[p,c])>tol), "O Pivo não nulo o algoritimo falha\n"
        
        
        # Se for necessário, troca linhas!
        if p==c:
            if verbose:
                print("Pivo A[%d,%d] = %.6g, não preciso trocar as linhas\n"
                      % (p, c, A[p,c]))
            else: 
                # o pivo não está na linha atual faço uma troca de linhas
                if verbose:
                    print("Pivo A[%d,%d] = %.6g, trocando as linhas %d <=> %d\n"
                          % (p, c, A[p,c], p, c))
                x = -A[c].copy()

                A[c] = A[p]
                A[p] = x
            
            # Faz o escalonamento para coluna c
            if verbose: print('')
            for l in range(c+1, n):
                coef = A[l, c]/ A[c,c]
                if verbose: print("E_%d - %.2f E_%d -> E_%d)" % (l, coef, c, l))
                A[l] = A[l] - coef*A[c] 
            if verbose: print(A, "\n\n")
            
    return A 


# Substituição regressiva
def subs_regressiva(A, verbose=False):
    
    n=len(A)
            
    #Não posso inicar a substituição regressiva
 
    #assert(A[n-1, n-1] != 0), "A[%d, %d] = 0, Não existe solução única" % (n-1, n-1)
      
        
    #Substituição Regressiva
    
    if verbose:
        print("\n\n--------------------")
        print("Substituição Regressiva\n")
        
    x = [0]*n
    if(A[n-1, n-1]==0):
        x[n-1] = 1
    else: 
        x[n-1] = (A[n-1, n])/A[n-1, n-1]

    
    if verbose:
        print("x_%d = %.6g / %.6g = %.6g" % (n-1, A[n-1, n], A[n-1, n-1], x[n-1]))
    
    
    for i in range(n-2, -1, -1):
        s = 0
        strsoma = ""
        if verbose: print("x_%d = " % (i), end ='')
        for j in range(i+1, n):
            s+= A[i,j]*x[j]
            if verbose: strsoma += "%.6g x_%d + " % (A[i,j], j)
        
        if(A[i,i]==0):
            x[i] = 1
        else:
            x[i] = (A[i,n] - s)/A[i,i]
        
        if verbose: 
            print("(%.6g - (%s) )/ %.6g = %.6g" % (A[i,n], strsoma, A[i,i], x[i]))
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
    assert(size[0] < size[1]), "Matriz invá¡lida"
    
    A = escalona(A, 1.0e-10, verbose)
    x = subs_regressiva(A, verbose)
    

    return(x)

#pontos utilizados no relatório

# parabola
#A = np.array( [[1, 1], [2,4], [3, 9], [5,25], [6,36]], dtype=np.float64)

#elipse
#def elipse(x):
#    return np.sqrt(((1/9)*x*x - 1)/-(1/4))

#A = np.array( [[2, elipse(2)], [3,elipse(3)], [0.5, elipse(0.5)], [0.7,elipse(0.7)], [1,elipse(1)]], dtype=np.float64)

#hiperbole
#def hiperbole(x):
    #b = abs((-1+(1/9)*x*x)/(1/9))
    #return np.sqrt(b)
#A = np.array( [[8, hiperbole(8)], [4, hiperbole(4)], [5, hiperbole(5) ], [6, hiperbole(6)], [7, hiperbole(7)]], dtype=np.float64)


# funcoes auxiliares de hiperbole, parabola elipse e raiz quadrada
def raiz_quad(y, x):
    return (1/2)*(x + (y/x))

def raiz_x(coef, x):
    b = abs((-2*coef[3]*x - coef[5])/coef[0])
    return ponto_fixo(raiz_quad, b, 3, 1E-20, 100)

def parabola(coef, x):
    return (-coef[0]/2*coef[4])*x*x - coef[5]

def elipse(coef, x):
    b = abs((coef[0]*x*x - 1)/-coef[2])
    return ponto_fixo(raiz_quad, b, 3, 1E-20, 100)

def hiperbole(coef, x):
    b = abs((coef[2]*x*x - 1)/coef[0])
    return ponto_fixo(raiz_quad, b, 3, 1E-20, 100)

# cria minha matriz com os coeficientes lineares
def coef_conica(x,y, F):
    coef = np.zeros(6)
    coef[0] = x*x
    coef[1] = 2*x*y
    coef[2] = y*y
    coef[3] = 2*x
    coef[4] = 2*y
    coef[5] = F
    
    
    return coef


def conica(A):
    """
    Programa que calcula um conica que passa por 5 pontos nao colineares
    Mostra no grafico os pontos e a conica
    
    Recebe:   
        A  => Matriz 2x5, contendo os pontos da conica
    
    Retorna:
        Nada
    """
    

    #Verifica se os pontos são não colineares para todas as possivel combinaçoes
    for i in range(0, 3):
        for j in range(i+1, len(A)-1):
            for z in range(j+1, len(A)):
                B = np.array([[A[i][0], A[i][1], 1],
                              [A[j][0], A[j][1], 1],
                              [A[z][0], A[z][1], 1]])
                det = np.linalg.det(B)
                assert (det!=0), "Os pontos devem ser não colineares"              
        

    m_coef = np.zeros(30).reshape(5,6) #Aumentada
    for i in range(0, 5):
        provisoria = coef_conica(A[i][0], A[i][1], 1)
        m_coef[i] = provisoria
    
    type = 1;
    
    # verifica se tem linha nula, se tiver é parabola
    escalona(m_coef, 1.0e-10)
    if m_coef[len(m_coef)-1][len(m_coef)-1] == 0:
        m_coef = np.zeros(30).reshape(5,6) #Aumentada
        type = 0
        for i in range(0, 5):
            provisoria = coef_conica(A[i][0], A[i][1], 0)
            m_coef[i] = provisoria
        
            
    
    # chama minha funçao gauss para resolver o sistema e determinar os coeficientes
    coef_funcao = eliminacao_guassiana(m_coef, False)
    coef_funcao.append(type)
    
    
    #Determina se a matriz conica é degenerada
    deg = np.array([[coef_funcao[0], coef_funcao[1], coef_funcao[3]],
                    [coef_funcao[1], coef_funcao[2], coef_funcao[4]],
                    [coef_funcao[3], coef_funcao[4], coef_funcao[5]]], dtype=np.float64)
    
    
    assert (np.linalg.det(deg) != 0), "Conica Degenerada, erro no programa"
    
    
    # determina o tipo de conica
    tipo = ""
    tipo_m = np.array([[coef_funcao[0], coef_funcao[1]],
                       [coef_funcao[1], coef_funcao[2]]], dtype=np.float64)
    
    det = np.linalg.det(tipo_m)
    if det == 0:
        tipo = "parabola"
    elif det > 0:
        tipo = "elipse"
    else:
        tipo = "hiperbole"         
        
        
    
#plota o gráfico da funcao e os pontos importantes
    
    #determina a intersecção da conica
    p = ponto_fixo(raiz_x, coef_funcao, 5, 1E-20, 100)
    
    
    if tipo == "parabola":    
        x = np.linspace(-10, 10, 100)
        plt.plot(x, parabola(coef_funcao, x), "b-")
        
        #plota os pontos iniciais
        for i in range(0, len(A)):    
            plt.plot(A[i][0], A[i][1], "g.")
        #plota a interccao com o eixo x
        plt.plot(p, 0, "r.")
        
    elif tipo == "elipse":
        y_raiz = 0
        x = np.linspace(-p, p, 10000)
        for i in range(0, 10000):  
            plt.plot(x[i], elipse(coef_funcao, x[i]), "b.")
            plt.plot(x[i], -(elipse(coef_funcao, x[i])), "b.")
        
        #plota os pontos iniciais
        for i in range(0, len(A)):    
            plt.plot(A[i][0], A[i][1], "g.")
        #plota a interccao com o eixo x
        plt.plot(p, 0, "r.")
        plt.plot(-p, 0, "r.")
        
        #plota a interccao com o eixo y
        y_raiz = elipse(coef_funcao, 0)
        plt.plot(0, y_raiz, "r.")
        plt.plot(0, -y_raiz, "r.")
        
        
    else:
        #plota uma hiperbole
        y_raiz = 0
        x = np.linspace(-10, 10, 100)
        for i in range(0, 100):    
            plt.plot(hiperbole(coef_funcao, x[i]), x[i], "b.")
            plt.plot(-(hiperbole(coef_funcao, x[i])), x[i], "b.")
        
        #plota os pontos iniciais
        for i in range(0, len(A)):    
            plt.plot(A[i][0], A[i][1], "g.")
        plt.plot(p, 0, "r.")
        plt.plot(-p, 0, "r.")
    
    plt.title(tipo)
    plt.grid()
    plt.show()

#conica(A)