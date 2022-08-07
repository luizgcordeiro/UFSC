import sys, os

sys.stdout = open(os.devnull, 'w')
sys.stdin=open("casos.txt")

from coisa import *

sys.stdout = sys.__stdout__
print(A)