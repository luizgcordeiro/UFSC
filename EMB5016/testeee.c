#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main (int argc , char ** argv ) {
    printf("Numero de argumentos: %d\n\n",argc);

    // argc=len(argv)
    int i,soma=0;

    for (i=1;i<argc;i++) {
        soma+=atoi(argv[i]);
    }

    printf("A soma dos argumentos e %d\n",soma);
    return 0;
}