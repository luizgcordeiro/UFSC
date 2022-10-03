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



A=np.array([[ -79, 15, 46,-57,101,-24, 40, 86, -3, 45],
 [ -71, 29, 31,-34, 50,-55, 45,-24, -7,-49],
 [ -51, 22, -3, -8, 11,-66,  7,-41, -6,-61],
 [  66, -5,-59, 67,-126,  5,-83,-94,  0,-20],
 [ -72, 19, 12,-51,131,-165, 88,-19, -5,-102],
 [  27, 24,-28, 38,-96,-19,-87,-66, -7, -2],
 [ -71, 17,-53, 28,-62,-37,-128,-80, -6,-32],
 [  10, -4, -3,  4, -6  ,9  ,-5,  4,  1,  8],
 [  21, -6, 60,-66,149,-35, 53, 84,  3,100],
 [  33, -2,-14, -3,  1, 19,-86,128,  0,142]])

np.set_printoptions(formatter={'float': lambda x: "{0:6.2f}".format(x)})
#X=rref(A,verbose=True)

