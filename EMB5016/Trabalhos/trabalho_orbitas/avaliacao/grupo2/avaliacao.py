import numpy as np
import orbita

EL=np.load("elipticasxxx.npy",allow_pickle=True)
PAR=np.load("parabolicasxxx.npy",allow_pickle=True)
HIP=np.load("hiperbolicasxxx.npy",allow_pickle=True)
acertos=0
erros=0

for A in EL:
    if orbita.orbita(A,mostrar=False)[0]=="elipse":
        acertos+=1
    else:
        erros+=1
    #endifelse
#endfor

print("Elipticas: ")
print("Erros: " + str(erros))
print("Acertos: " + str(acertos))

for i in range(5):
    orbita.orbita(EL[i],mostrar=True)
#end if

acertos=0
erros=0

for A in PAR[:1]:
    if orbita.orbita(A,mostrar=False)[0]=="parabola":
        acertos+=1
    else:
        erros+=1
    #endifelse
#endfor

print("Parabolicas: ")
print("Erros: " + str(erros))
print("Acertos: " + str(acertos))

for i in range(5):
    orbita.orbita(PAR[i],mostrar=True)
#end if

acertos=0
erros=0

for A in HIP:
    if orbita.orbita(A,mostrar=False)[0]=="hiperbole":
        acertos+=1
    else:
        erros+=1
    #endifelse
#endfor

print("Hiperbolicas: ")
print("Erros: " + str(erros))
print("Acertos: " + str(acertos))

for i in range(5):
    orbita.orbita(HIP[i],mostrar=True)
#end if