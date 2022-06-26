import numpy as np
import time

from functions import *

A=np.random.randint(low=-10,high=10,size=(4,4))
print(type(A))
triangularization(A,pivoting="integer",verbose=True)