import time
from escalonamento import *
from funcoes_teste import *
from lu import *

m=50
n=50
testes=100

tempo_lu=0
tempo_gauss=0

A=np.matrix(np.random.randint(low=-10,high=10,size=(m,n))).astype(float)

tempo_inicial=time.time()
LU=crout(A)

L=LU[0]
U=LU[1]
tempo_lu+=(time.time()-tempo_inicial)

for i in range(testes):
    b=np.matrix(np.random.randint(low=-10,high=10,size=(m,1))).astype(float)

    X=np.concatenate([A,b],axis=1);

    tempo_inicial=time.time()
    x=(escalona(X)[0])[:,n]
    tempo_gauss+=(time.time()-tempo_inicial)

    tempo_inicial=time.time()
    y=res_tri_inf(L,b)
    x=res_tri_sup(U,y)
    tempo_lu+=(time.time()-tempo_inicial)
#end for

print("tempo LU: " + str(tempo_lu))
print("tempo Gauss: " + str(tempo_gauss))
