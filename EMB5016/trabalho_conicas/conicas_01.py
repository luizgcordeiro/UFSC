# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 14:50:32 2022

@author: Gabriel
"""
import numpy as np
import matplotlib.pyplot as plt

#Pontos aleatorios
A=np.matrix(np.random.randint(low=-10,high=10,size=(5,2)).astype(float))

#b caso F=1
b = np.matrix([[-1.0],[-1.0],[-1.0],[-1.0],[-1.0]])
#b caso F=0
b2 = np.matrix([[0.0],[0.0],[0.0],[0.0],[0.0]])


def gausseidel(A,b):
    x = np.matrix([[1.0],[1.0],[1.0],[1.0],[1.0]])
    
    t = len(A)
    
    iter=0
    
    while np.max(abs(A*x-b))>1e-8 and iter<100:
        for i in range(t):
            x0 = 0
            
            for j in range(t):
                
                if (j!=i):#Somatórios dos pontos fora da linha principal
                    x0 = x0 + A[i,j] * x[j]
            
            x[i] = (b[i,0] - x0) / A[i,i]
        
        iter+=1
    
    return x

def conica(A,b):
    
    print ('Pontos iniciais:',A)
    tol = 1e-8
    eqconica = np.matrix(np.zeros([5,5])).astype(float)
    
    #Matrizes determinante para checar lineariadade entre os pontos:
    L1 = np.matrix([[A[0,0], A[0,1], 1],[A[1,0], A[1,1], 1],[A[2,0], A[2,1], 1]])#Pontos 123
    L2 = np.matrix([[A[0,0], A[0,1], 1],[A[1,0], A[1,1], 1],[A[3,0], A[3,1], 1]])#Pontos 124
    L3 = np.matrix([[A[0,0], A[0,1], 1],[A[1,0], A[1,1], 1],[A[4,0], A[4,1], 1]])#Pontos 125
    L4 = np.matrix([[A[0,0], A[0,1], 1],[A[2,0], A[2,1], 1],[A[3,0], A[3,1], 1]])#Pontos 134
    L5 = np.matrix([[A[0,0], A[0,1], 1],[A[2,0], A[2,1], 1],[A[4,0], A[4,1], 1]])#Pontos 135
    L6 = np.matrix([[A[0,0], A[0,1], 1],[A[3,0], A[3,1], 1],[A[4,0], A[4,1], 1]])#Pontos 145
    L7 = np.matrix([[A[1,0], A[1,1], 1],[A[2,0], A[2,1], 1],[A[3,0], A[3,1], 1]])#Pontos 234
    L8 = np.matrix([[A[1,0], A[1,1], 1],[A[2,0], A[2,1], 1],[A[4,0], A[4,1], 1]])#Pontos 235
    L9 = np.matrix([[A[1,0], A[1,1], 1],[A[3,0], A[3,1], 1],[A[4,0], A[4,1], 1]])#Pontos 245
    L10 = np.matrix([[A[2,0], A[2,1], 1],[A[3,0], A[3,1], 1],[A[4,0], A[4,1], 1]])#Pontos 345
    
    #Determinantes:
    D1 = abs(np.linalg.det(L1))
    D2 = abs(np.linalg.det(L2))
    D3 = abs(np.linalg.det(L3))
    D4 = abs(np.linalg.det(L4))
    D5 = abs(np.linalg.det(L5))
    D6 = abs(np.linalg.det(L6))
    D7 = abs(np.linalg.det(L7))
    D8 = abs(np.linalg.det(L8))
    D9 = abs(np.linalg.det(L9))
    D10 = abs(np.linalg.det(L10))
    
    #Checar se algum desses determinantes é nulo:
    if (D1<tol) or (D2<tol) or (D3<tol) or (D4<tol) or (D5<tol) or (D6<tol) or (D7<tol) or (D8<tol) or (D9<tol) or (D10<tol):
        print ('Não gera equação conica')
        return None
    
    for i in range (5): #Gerar matriz das equações conicas dados pelos pontos
        eqconica[i,0] = A[i,0] * A[i,0]
        eqconica[i,1] = 2 * (A[i,0] * A[i,1])
        eqconica[i,2] = A[i,1] * A[i,1]
        eqconica[i,3] = 2 * A[i,0]
        eqconica[i,4] = 2 * A[i,1]
        
    solu = gausseidel(np.transpose(eqconica)*eqconica, np.transpose(eqconica)*b)#Multiplicamos pela transposta a eq e b
    #A multiplicação pela tranposta é feita por causa do critério de convergência
    #Gauss converge caso é diagonalmente dominante ou positiva definida, oque a multiplicação pela transposta ajuda a ser
    
    if abs(np.max((eqconica*solu)-b))<tol:#Quando F é algum número, dividimos tudo por F e teremos F=1
        F = 1
    
    else:#Quando o F da equação equivale a 0
        solu = gausseidel(np.transpose(eqconica)*eqconica, np.transpose(eqconica)*b2)
        F = 0
    
    #Checar se é uma conica degenerativa com det de [A B D][B C E][D E F]
    deg0 = np.matrix([[solu[0], solu[1], solu[3]],[solu[1], solu[2], solu[4]],[solu[3], solu[4], F]], float)
    deg = abs(np.linalg.det(deg0))
    if deg<tol:
        print('Gera uma cônica degenerativa')
        return None
    
    det = solu[0,0]*solu[2,0] - solu[1,0]*solu[1,0]#Determinante de [A B][B C]
    if abs(det)<tol:#Determinante 0
        print ('É uma conica do tipo Parabola')
        
    if det>tol:#Determinante maior que 0
        print ('É uma conica do tipo Elipse')
    
    if det<-tol:#Determinante menor que 0
        print ('É uma conica do tipo Hiperbole')
    
    xcoord = 1
    ycoord = 1
    iter = 0
    iteri = 0
    
    #Encontrar pontos de interseção:
    if abs(2 * solu[0,0] * xcoord + 2 * solu[3,0])<tol:#Checar se chute inicial é bom
        xcoord = 0.5
        
    while iter<100 or abs(solu[0,0] * xcoord* xcoord + 2 * xcoord * solu[3,0] + F)>tol:#Descobre x quando y=0
        xcoord = xcoord - (solu[0,0] * xcoord* xcoord + 2 * xcoord * solu[3,0] + F) / (2 * solu[0,0] * xcoord + 2 * solu[3,0])
        iter+=1
    
    if abs(2 * solu[2,0] * ycoord + 2 * solu[4,0])<tol:#Checar se chute inicial é bom
        ycoord = 0.5
        
    while iteri<100 or abs(solu[2,0] * ycoord* ycoord + 2 * ycoord * solu[4,0] + F)>tol:#Descobre y quando x=0
        ycoord = ycoord - (solu[2,0] * ycoord* ycoord + 2 * ycoord * solu[4,0] + F) / (2 * solu[2,0] * ycoord + 2 * solu[4,0])
        iteri+=1
    
    print ('Coordenas de interseção:',np.matrix([[xcoord,0],[0,ycoord]]))
    
    xcoord = np.array([xcoord, 0, A[0,0], A[1,0], A[2,0], A[3,0], A[4,0]])#Coordenadas x do grafico
    ycoord = np.array([0, ycoord, A[0,1], A[1,1], A[2,1], A[3,1], A[4,1]])#Coordenadas y do grafico
    
    plt.scatter(xcoord, ycoord)#Grafico de pontos
    plt.show()#Plota grafico
    
    print ('Uma das equações é:', solu[0],'* x^2','+', solu[1],'* 2xy','+', solu[2],'* y^2','+', solu[3],'* 2x','+', solu[4],'* 2y','+', F)    
    return None
