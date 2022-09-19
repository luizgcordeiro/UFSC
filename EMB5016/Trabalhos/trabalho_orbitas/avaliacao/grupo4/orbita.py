import matrizes_gauss_thomas as gauss
import newton 
import numpy as np
#importamos os modulos necessarios#
#sistema que descobre os coeficientes da conica#
def orbita(A,mostrar=True):
  sistema = np.zeros((A.shape[0],6))
  for i in range(A.shape[0]):
        x = A[i, 0]
        y = A[i, 1] 
        sistema[i, 0] = x*x #coeficiente A
        sistema[i, 1] = 2*x*y #coeficiente B
        sistema[i, 2] = y*y #coeficiente C
        sistema[i, 3] = 2*x #coeficiente D
        sistema[i, 4] = 2*y #coeficiente E
        sistema[i, 5] = 2 #termo -F
  tol = 10e-3
  transposta = np.transpose(sistema) #utilizamos o nopy para obter a transposta
  novo_sistema = np.dot(transposta, sistema) #ultilizamos nopy para multiplicar a matriz transposta pela matriz sistema
  coeficientes = gauss.escalonamento(novo_sistema) #usamos o escalonamento para resolver o sistema
  determinante = coeficientes[0]*coeficientes[2] - coeficientes[1]*coeficientes[1] #calculamos a determinante para descobrir o tipo de conica
  if abs(determinante) < tol:
    return ["parabolica"]
  elif determinante < 0:
    return["hiperbolica"]
  elif determinante > 0:
    return["eliptica"]