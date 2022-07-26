#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

#Testes de matrizes pequenas
A=np.matrix(np.random.randint(low=-10,high=10,size=(8,2)).astype(float))

#gauss
def gausseidel(A,b):
    x = np.matrix([[1.0],[1.0],[1.0],[1.0],[1.0]])
    
    t = len(A)
    
    iter=0
    
    while np.all(abs(A*x-b))>1e-8 and iter<100:
        for i in range(t):
            x0 = 0
            
            for j in range(t):
                
                if (j!=i):#Somatórios dos pontos fora da linha principal
                    x0 = x0 + A[i,j] * x[j]
            
            x[i] = (b[i,0] - x0) / A[i,i]
        
        iter+=1
    
    return x

#orbita
def orbita(A, mostrar=True):
    
    t = len(A)
    tol = 1e-14
    #b caso F=1
    b = np.matrix(np.zeros([t,1])).astype(float)
    b.fill(-1.0)
    #b caso F=0
    b2 = np.matrix(np.zeros([t,1])).astype(float)
    
    eqconica = np.matrix(np.zeros([t,5])).astype(float)
    
    for i in range (t): #Gerar matriz das equações conicas dados pelos pontos
        eqconica[i,0] = A[i,0] * A[i,0]
        eqconica[i,1] = 2*(A[i,0] * A[i,1])
        eqconica[i,2] = A[i,1] * A[i,1]
        eqconica[i,3] = 2*A[i,0]
        eqconica[i,4] = 2*A[i,1]
        #eqconica[n,5]
        
    solu = gausseidel(np.transpose(eqconica)*eqconica, np.transpose(eqconica)*b)#Multiplicamos pela transposta a eq e b
    #A multiplicação pela tranposta é feita por causa do critério de convergência
    #Gauss converge caso é diagonalmente dominante ou positiva definida, oque a multiplicação pela transposta ajuda a ser
    
    if abs(np.max((eqconica*solu)-b))<tol:#Quando F é algum número, dividimos tudo por F e teremos F=1
        F = 1
    
    else:#Quando o F da equação equivale a 0
        solu = gausseidel(np.transpose(eqconica)*eqconica, np.transpose(eqconica)*b2)
        F = 0
        
    det = solu[0,0]*solu[2,0] - solu[1,0]*solu[1,0]#Determinante de [A B][B C]
    
    if abs(det)<tol:#Determinante 0
        tipo ='parabola'
        
    if det>tol:#Determinante maior que 0
        tipo ='elipse'
    
    if det<-tol:#Determinante menor que 0
        tipo ='hiperbole'
    
    n = t-2
    delx = A[n+1,0]-A[n,0]#Variação entre pontos
    xprox = np.array([A[t-1,0] + 0.5*delx,A[t-1,0] + delx,A[t-1,0]+1.2*delx])#
    yprox = np.array([0,0,0])

    def f(y,x):#função raiz
        prox = np.array([solu[2,0],2*x*solu[1,0] + 2*solu[4,0], solu[0,0]*x*x + 2*x*solu[3,0] + F ])
        return prox[0]*y*y + prox[1]*y + prox[2]#Cy^2 + (2Bxy + 2Ey) + (Ax^2 + 2Dx + F) = 0
    
    def f1(y,x):#derivada
        prox = np.array([solu[2,0],2*x*solu[1,0] + 2*solu[4,0], solu[0,0]*x*x + 2*x*solu[3,0] + F ])
        return 2*prox[0]*y + prox[1]#2Cy + (2Bx + 2E) = 0
    
    for i in range (3):
        chute = A[t-1,1] + 0.05
        iter = 0
        while (f(chute,xprox[i])>tol or f(chute,xprox[i])<-tol) and iter<100:#loop da determinação da raiz por newton
            chute = chute - (f(chute,xprox[i]) / f1(chute,xprox[i]))
            iter+=1
            
        yprox[i] = chute
    
    if mostrar:#plotar grafico caso mostrar=true
    
        xcoord = np.array(np.zeros(t+3)).astype(float)
        for i in range(t):#coordenadas x com 3 proximos chutes
            xcoord[i] = A[i,0]
        xcoord[t] = xprox[0]
        xcoord[t+1] = xprox[1]
        xcoord[t+2] = xprox[2]
        
        ycoord = np.array(np.zeros(t+3)).astype(float)
        for i in range(t):#coordenadas y com 3 proximos chutes
            ycoord[i] = A[i,1]
        ycoord[t] = yprox[0]
        ycoord[t+1] = yprox[1]
        ycoord[t+2] = yprox[2]
        
        plt.scatter(xcoord,ycoord)
        plt.show()
     
    return tipo, np.array([[xprox[0],yprox[0]],[xprox[1],yprox[1]],[xprox[2],yprox[2]]])



#Testes
EL=np.load("parabolicasxxx.npy",allow_pickle=True)
acertos=0
erros=0

for A in EL[:5]:
    orbita(A,mostrar=True)
#endfor

print("Erros: " + str(erros))
print("Acertos: " + str(acertos))
