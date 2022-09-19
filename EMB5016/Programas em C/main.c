#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#define N 4//Numero de colunas das matrizes teste
#define M 4//Numero de linhas das matrizes teste
#define K 1000//Ordem dos numeros aleatorios a serem criados

float maximo(float m, float n);
int numero_de_digitos(float m);
int pot(int m,int k);
void triangularizacao(float *P, float* e,int m,int n,float tol);
void imprimir_matriz(float * a,int m, int n);
void transposicao(int x[M][N], int y[N][M]);

int main() {
  srand(time(NULL));   // Initialization, should only be called once.

  float m[M][N];

  int i,j;
  for (i=0;i<M;i++) {
    for (j=0;j<N;j++) {
      m[i][j]=(float)(rand()%K-(K/2));
    }
  }

  printf("A matriz eh\n");
  imprimir_matriz(*m,M,N);

  printf("\nA forma triangularizada eh\n");
  float e[M][N];
  triangularizacao(*m,*e,M,N,1.0e-5);
  imprimir_matriz(*e,M,N);
  return 0;
}

void triangularizacao(float *P, float* E,int m,int n, float tol) {
  /*Realiza a "trianguarização" de uma matriz M de ordem mxn e
  guarda o resultado numa matriz E. Matrizes consideradas como
  vetores/ponteiros, e portanto devem ser chamadas por &M, &E.

  tol=tolerancia numerica.

  Entrada i,j de M chamada por M[m*i+j]*/

  /*Transforma E em P*/

  int i,j;
  for (i=0;i<m;i++) {
    for (j=0;j<n;j++) {
      E[m*i+j]=P[m*i+j];
    }
  }

  /*Vai coluna-a-coluna*/

  j=0;
  int numero_de_pivos=0;
  while (j<n&&numero_de_pivos<m) {
    /*Procura um pivô na j-ésima coluna.*/
    int maior_coordenada=numero_de_pivos;
    int i;
    for (i=numero_de_pivos+1;i<m;i++) {
      if (abs(E[m*i+j])>abs(E[m*maior_coordenada+j])) {
        maior_coordenada=i;
      }
    }

    if (abs(E[m*maior_coordenada+j])<tol) {
      j++;
      break;
    }

    /*Põe o pivô na posição certa*/
    int k;
    for (k=j;k<n;k++) {
      float x=E[m*numero_de_pivos+k];
      E[m*numero_de_pivos+k]=E[m*maior_coordenada+k];
      E[m*maior_coordenada+k]=x;
    }

    /*Pivoteia*/

    for (i=numero_de_pivos+1;i<m;i++) {
      float multiplicador=E[m*i+j]/E[m*numero_de_pivos+j];
      E[m*i+j]=0;
      int k;
      for (k=j+1;k<n;k++) {
        E[m*i+k]-=multiplicador*E[m*numero_de_pivos+k];
      }
    }

    numero_de_pivos++;
    j++;
  }
}

void imprimir_matriz(float * a, int m, int n) {
  int i,j;

  float maiorelemento=0;
  for (i=0;i<m;i++) {
    for (j=0;j<n;j++) {
      maiorelemento=maximo(maiorelemento,abs(a[m*i+j]));
    }
  }

  int k=numero_de_digitos(maiorelemento);//Tem espaço para sinal.
  for (i=0;i<M;i++) {
    for (j=0;j<N;j++) {
      printf("%*.4f ",k+5,a[m*i+j]);
    }
    printf("\n");
  }
}

float maximo(float m, float n) {
  if (m>n) {
    return m;
  }
  return n;
}

int pot(int m,int k) {
  if (k==0) {
    return 1;
  }
  return m*pot(m,k-1);
}

int numero_de_digitos(float m) {
  int i=0;
  while (pot(10,i)<m) {
    /*Se sai em i=1, tem 1 dígito; se sai em i=2, tem 2...*/
    i++;
  }
  return i+1;//Tem espaço para o sinal;
}


void transposicao(int x[M][N], int y[N][M]) {
  /*Transpõe a matriz em x e grava o resultado em y*/

  int i,j;
  for (i=0;i<M;i++) {
    for (j=0;j<N;j++) {
      y[j][i]=x[i][j];
    }
  }
}
