import time
import numpy as np

n=10000000

A=np.random.random(size=n)
B=np.random.random(size=n)
C=n*[0]

#Numeros aleatorios float entre -100 e 100
for i in range(n):
    A[i]=200*A[i]-100
    B[i]=200*B[i]-100

print("==========")

start=time.time()
for i in range(n):
    C[i]=A[i]+B[i]
#end for
end=time.time()

print(f"Tempo para somar {n} de numeros: {end-start} segundos")
print()

start=time.time()
for i in range(n):
    C[i]=A[i]*B[i]
#end for
end=time.time()

print(f"Tempo para multiplicar {n} de numeros: {end-start} segundos")
print()

start=time.time()
for i in range(n):
    C[i]=A[i]/B[i]
#end for
end=time.time()

print(f"Tempo para dividir {n} de numeros: {end-start} segundos")
print()

start=time.time()

for i in range(n):
    x=A[i]
    A[i]=B[i]
    B[i]=x
#end for
end=time.time()

print(f"Tempo para trocar {n} de numeros: {end-start} segundos")
print("==========")