import numpy as np
import time

from functions import *

A=np.array([[1,-8,-220],[81,2,380]])



X=triangularization(A,pivoting="integer",verbose=True,write_latex=True,index_start=1,\
    latex_begin="\\begin{amatrix}{2}{1}",latex_end="\\end{amatrix}"
    )
print()
print(X)
