#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 15:34:24 2022

@author: knuth
"""

from functions import fact, binomial, tirarbolinhas_estatistico, tirarbolinhas_explicito, tirarbolinhas_explicito2

print('\
Uma piscina de bolinhas tem V bolinhas vermelhas e A bolinhas azuis.\n\
Você tira N bolinhas dessa piscina, e pergunta qual a chance que\n\
exatamente k dessas bolinhas sejam vermelhas.\n\
\n\
Use as funções\n\
    tirarbolinhas_estatistico(A,V,N,k,t)\n\
e\n\
    tirarbolinhas_explicito(A,V,N,k)\n\
para calcular essa probabilidade por com uma amostragem de tamanho t\n\
e com uma fórmula explícita, respectivamente.\
')

