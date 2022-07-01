import numpy as np
import time

from functions import *

A=np.random.randint(low=-2,high=5,size=(4,4))
#A=np.array([[1,2,-3,4],[1,-4,2,-1]])



#X=triangularization(A,pivoting="integer",verbose=True,write_latex=True,index_start=1,\
#    #latex_begin="\\begin{amatrix}{3}{1}",latex_end="\\end{amatrix}"
#    )

X=np.array([1,-4,3])
Y=np.array([-2,-4,3])

print(prod_vec(X,Y))