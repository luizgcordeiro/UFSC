def k(x): return (7-x*x)/(2*x*x+1) +x
def n(x): return (x**2+7)/(2*x)

def g(x,c): return x*(2-c*x)
c=1.5
x=1

for i in range(7):
    print(f"Iteracao {i}: x={x};")
    i+=1
    x=g(x,c)