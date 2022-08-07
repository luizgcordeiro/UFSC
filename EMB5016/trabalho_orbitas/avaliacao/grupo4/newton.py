# Metodo de newton #
def f(n,c,x):
  return x**n - c
def df(n,x):
  return n*x**(n-1)
def metodo_newton(n,c,f,df,x0,tol=10e-10,cont=0,itmax=1000):
    if abs(f(n,c,x0)) < tol:
        return x0
    elif(cont>=itmax): return "erro" 
    else:
        return metodo_newton(n,c,f, df, x0 - f(n,c,x0)/df(n,x0), tol,cont+1,itmax)
def raiz_newton(n,c):
  if(c<0) and (n%2==0): return "Nao existe"
  return metodo_newton(n,c,f,df,c)
