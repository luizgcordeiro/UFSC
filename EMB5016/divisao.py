#Teste para ver o quao mais lento que divisao é que multiplicacao

import numpy as np
import time

n=10000000

x=np.random.random(n)
y=np.random.random(n)

start_time=time.time()

for i in range(n):
    x[i]*y[i]
#end for

t=time.time()-start_time

print("Tempo para " + str(n) + " multiplicações: " + str(t) + " segundos.")

start_time=time.time()

for i in range(n):
    y[i]/x[i]
#end for

t=time.time()-start_time

print("Tempo para " + str(n) + " divisoes: " + str(t) + " segundos.")
