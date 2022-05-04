# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
    #end if-else
#end def
    
'''
Em Python 3.10, poderia-se usar pattern matching:
    
def fact(n):
    match n:
        case 0:
            return 1
        default:
            return n*fact(n-1)
        #end cases
    #end match
#end def
'''

def binomial(n,m):
    return fact(n)/(fact(m)*fact(n-m))
#enddef
    
def tirarbolinhas_estatistico(A,V,N,k,t):
    
    total_bolinhas=["A" for i in range(A)] + ["V" for i in range(V)]
    
    casos_sucesso=0
    for j in range(t):
        #Mistura as bolinhas
        
        #Escolher um tanto aleatório de bolinhas, e conta quantas são vermelhas
        
        numero_de_azuis=sum([1 for x in random.sample(total_bolinhas,N) if x=="V"])
        
        if numero_de_azuis==k:
            casos_sucesso+=1
        #end if
    #end for
    
    return casos_sucesso/t
#end def
    
def tirarbolinhas_explicito(A,V,N,k):
    #fórmula obtida em aula
    #
    ##Vamos tirar N bolinhas
    #k dessas têm que ser vermelhas.
    #Temos binom(N,k) possibilidades para as posições dessas vermelhas
    #Para cada uma dessas posições, tem uma chance de
    #V(V-1)...(V-k+1)  A(A-1)...(A-(N-k)+1)/((V+A)(V+A-1)...(V+A-N+1))
    #=V!/(V-k)!   A!/(A-(N-k)!)
    #Ao todo: binom(N,k) vezes o número acima

    return binomial(N,k)\
                *(fact(V)/fact(V-k))\
                *(fact(A)/fact(A-(N-k)))\
                *fact(V+A-N)\
                /fact(V+A)
#end def

def prod(x):
    #produto de uma lista x
    if x==[]:
        return 1
    else:
        return x[0]*prod(x[1:])
    #end if-else
#end def
    
def tirarbolinhas_explicito2(A,V,N,k):
    #tentar evitar overflow

    return prod(list(range(N-k+1,N+1)))/fact(k)\
                *prod(list(range(V-k+1,V+1)))\
                *prod(list(range(A-N+k+1,A+1)))\
                /prod(list(range(V+A-N+1,V+A+1)))
#end def