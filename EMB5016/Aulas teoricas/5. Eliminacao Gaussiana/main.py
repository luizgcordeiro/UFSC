from escalonamento import *
from funcoes_teste import *
import numpy as np

for i in range(100):
    m=10
    n=10

    R=random_ref(m,n)
    U=unimodular(m)
    A=U@R

    S=rref(A)[0]

    erro=np.max(abs(R-S))
    
    if erro>1.0e-5:
        print("Erro obtido com a matriz")
        print(A.astype(int))
        print("A rref deveria ser")
        print(R.astype(int))
    else:
        print(f"Teste {i} passado")



np.set_printoptions(formatter={'float': lambda x: "{0:6.2f}".format(x)})
#X=rref(A,verbose=True)

