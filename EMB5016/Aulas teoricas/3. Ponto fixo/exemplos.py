# Testes para calcular sqrt(7)
def g(x): return x**2 -7+x
def h(x): return 7-x**2+x
def k(x): return (7-x**2)/(2*(x**2)+1) +x
def n(x): return (x**2+7)/(2*x)

# Teste para inverter numeros
def g(x,c): return x*(2-c*x)

# Teste criterios de parada e numero de iteracoes distintos
for i in range(7):
    print(f"Iteracao {i}: x={x};")
    i+=1
    # Troque a funcao aqui
    x=g(x)