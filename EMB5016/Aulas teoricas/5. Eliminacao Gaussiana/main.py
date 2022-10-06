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



A=[[  190,    -9,   -67,   -12,    74,   -37,    30,     0,  1083,    82],
 [   68,   -47,   -56,   -67,    12,   -10,   -37,    -8,   744,   -53],
 [ -116,    63,   143,    53,   -63,    68,    72,     9, -2553,    -1],
 [  -72,    33,   105,    -2,   -41,    63,    44,     4, -2076,    -3],
 [  -34,    20,    47,   -31,     6,    34,    -4,     3,  -980,   140],
 [   22,   -10,   -33,   -57,   111,    16,     6,    -1,   157,    48],
 [   40,   -36,   -90,   -11,    55,  -117,   -17,    -5,  2230,  -134],
 [ -107,   -49,   -24,  -147,    50,     5,   -90,    -9,   142,    37],
 [    9,    -6,    -8,    -8,     2,    -2,    -5,    -1,   115,    -6],
 [  -12,     0,    41,   -24,   -79,    64,   -57,    -1,  -955,    90]]

np.set_printoptions(formatter={'float': lambda x: "{0:6.2f}".format(x)})
X=rref(A,verbose=True)

