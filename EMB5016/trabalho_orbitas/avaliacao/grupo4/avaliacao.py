import numpy as np
import orbita

EL=np.load("elipticasxxx.npy",allow_pickle=True)
PAR=np.load("parabolicasxxx.npy",allow_pickle=True)
HIP=np.load("hiperbolicasxxx.npy",allow_pickle=True)
acertos=0
erros=0

for A in EL:
    if orbita.orbita(A,mostrar=False)[0]=="eliptica":
        acertos+=1
    else:
        erros+=1
    #endifelse
#endfor

print("Elipticas: ")
print("Erros: " + str(erros))
print("Acertos: " + str(acertos))

orbita.orbita(EL[0],mostrar=True)
orbita.orbita(EL[1],mostrar=True)
orbita.orbita(EL[2],mostrar=True)
orbita.orbita(EL[3],mostrar=True)
orbita.orbita(EL[4],mostrar=True)

acertos=0
erros=0

for A in PAR:
    if orbita.orbita(A,mostrar=False)[0]=="parabolica":
        acertos+=1
    else:
        erros+=1
    #endifelse
#endfor

print("Parabolicas: ")
print("Erros: " + str(erros))
print("Acertos: " + str(acertos))

orbita.orbita(PAR[0],mostrar=True)
orbita.orbita(PAR[1],mostrar=True)
orbita.orbita(PAR[2],mostrar=True)
orbita.orbita(PAR[3],mostrar=True)
orbita.orbita(PAR[4],mostrar=True)

acertos=0
erros=0

for A in HIP:
    if orbita.orbita(A,mostrar=False)[0]=="hiperbolica":
        acertos+=1
    else:
        erros+=1
    #endifelse
#endfor

print("Hiperbolicas: ")
print("Erros: " + str(erros))
print("Acertos: " + str(acertos))

orbita.orbita(HIP[0],mostrar=True)
orbita.orbita(HIP[1],mostrar=True)
orbita.orbita(HIP[2],mostrar=True)
orbita.orbita(HIP[3],mostrar=True)
orbita.orbita(HIP[4],mostrar=True)