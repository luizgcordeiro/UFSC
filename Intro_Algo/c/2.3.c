#include <stdio.h>
#include <stdlib.h>
#include <time.h>
//#include <stdarg.h> // function arguments
//#include <math.h> // math
#include <string.h>

void print_int_vector(int * v , int n) {
  //Prints an an-sized integer vector v

  printf( "[" );
  int i;
  for (i=0;i<n-1;i++) {
    printf(" %d ,",v[i]);
  }
  printf(" %d ]",v[i]);
  return;
}

void create_int_vector ( int * v , int n ) {
  //Randomly creates an n-sized integer vector v

  srand(time(NULL));

  for ( int i=0;i<n;i++) {
    v[i]=rand()%100;
  }
  return;
}

void merge (int * A , int p , int q , int r) {
    //Merges A[p,q] and A[q+1,r], where p<=q<r
    int n1=q-p+1;
    int n2=r-q;
    int L[n1] , R[n2];
    for (int i=0;i<n1;i++) {
        L[i]=A[p+i];
    }
    for (int j=0;j<n2;j++) {
        R[j]=A[q+1+j];
    }
    int i=0,j=0,k=p;
    while (i<n1 && j<n2) {
        if (L[i]<=R[j]) {
            A[k++]=L[i++];
        } else {
            A[k++]=R[j++];
        }
    }

    while (i<n1) {
        A[k++]=L[i++];
    }

    while (j<n2) {
        A[k++]=R[j++];
    }
}

void merge_sort ( int * A , int p , int r ) {
    if (p==r) {
        return;
    }
    int q=(p+r)/2;
    merge_sort(A,p,q);
    merge_sort(A,q+1,r);
    merge(A,p,q,r);
}

/*int main( int argc , char ** argv ) {
    srand(time(NULL));

    int n=100000000;
    int number=10;

    int * v[number];
    for (int i=0;i<number;i++) {
        v[i]=malloc(n*sizeof(int));
        create_int_vector(v[i],n);
        merge_sort(v[i],0,n-1);
    }


    return 0;
}*/

int main() {
    double N[4];
    for (int i=0;i<4;i++) {
        scanf("%lf",N+i);
    }
    
    double media=(2*N[0]+3*N[1]+4*N[2]+N[3])/10;
    
    printf("Media: %.1lf\n",media);
    if (media>=7.0) {
        printf("Aluno aprovado.\n");
    } else if (media<5.0) {
        printf("Aluno reprovado.\n");
    } else {
        printf("Aluno em exame.\n");
        double exame;
        scanf("%lf",&exame);
        printf("Nota do exame: %.1lf\n",exame);
        media=(media+exame)/2;
        if (media>=5.0) {
            printf("Aluno aprovado.\n");
        } else {
            printf("Aluno reprovado.\n");
        }
        printf("Media final: %.1lf\n",media);
    }
    return 0;
}