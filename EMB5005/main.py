import numpy as np
import time

from functions import *

#A=np.random.randint(low=-2,high=5,size=(4,4))
A=np.array([[1,2,-3,4],[1,-4,2,-1]])



X=triangularization(A,pivoting="integer",verbose=True,write_latex=True,index_start=1,latex_begin="\\begin{amatrix}{3}{1}",latex_end="\\end{amatrix}")

print(X[2])