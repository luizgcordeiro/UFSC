import numpy as np
import time

from functions import *

A=np.random.randint(low=-2,high=5,size=(4,4))
print(type(A))

X=triangularization(A,pivoting="integer",verbose=True,write_latex=True,index_start=1)

print(X[2])