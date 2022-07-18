import sympy as sp

import numpy as np

def conica(X,verbose=True,plot=True):
    '''
    Determina a conica representada por uma equacao quadratica.

    Parametros
    ----------
    X : array-like [A,B,C,D,E,F]
        Coeficientes da equacao quadratica
        Ax^2+2Bxy+Cy^2+2Dx+2Ey+F=0
        
    Saida
    -----
    conica : Varias informacoes, dependendo do tipo de conica.
    '''

    x, y = sp.symbols("x y")
    A,B,C,D,E,F=X

    print(f"Temos:\nA={A},\nB={B},\nC={C},\nD={D},\nE={E},\nF={F}.")


    print("\nA equacao da conica e")
    
    sp.pprint(sp.Eq((A*x**2+2*B*x*y+C*y**2+2*D*x+2*E*y+F),0))
    
    Delta=sp.Matrix([[A,B,D],[B,C,E],[D,E,F]]).det()
    delta=sp.Matrix([[A,B],[B,C]]).det()
    s=A+C
    
    print(f"-------\nPASSO 1\n"+\
          f"-------\n"+\
            f"Determinar o tipo de conica por meio de analise de determinantes.\n")
    print(  f"Delta=det([[A,B,D],\n"+\
            f"           [B,C,E],\n"+\
            f"           [D,E,F]])={Delta}.\n"+\
            f"delta=det([A,B],\n"+\
            f"          [B,C]]).={delta}\n"+\
            f"s=A+C={s}.")

    print()
    print("-------\nPASSO 2\n"+\
          "-------\n"+\
          "Usar a tabela para determinar o tipo de conica.\n")
    if Delta!=0:
        if delta<0:
            print("Delta!=0 e delta<0: Hiperbole.")
        elif delta==0:
            print("Delta!=0 e delta=0: Parabola.")
        else:
            if s*Delta<0:
                print("s*Delta<0 e delta>0: Elipse.")
            else: #Positive
                print("s*Delta>0 e delta>0: Vazio.")
            #end if-else
        #end if-else
    else:
        if delta<0:
            print("Delta=0 e delta<0: Duas retas concorrentes.")
        elif delta==0:
            print("Delta=0 e delta=0: Uma reta ou duas retas paralelas.")
        else:
            print("Delta=0 e delta>0: Um ponto.")
        #end if-else
    #end if-else

    print()
    print("-------\nPASSO 3\n-------")
    print("Encontrar as solucoes da equacao")
    t=sp.Symbol('t')
    sp.pprint(sp.Eq(sp.simplify((t-A)*(t-C)-B**2),0))
#end def

X=[1,-2,0,3,-4,5]

conica(X)