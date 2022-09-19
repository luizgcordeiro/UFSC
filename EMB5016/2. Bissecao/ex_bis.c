#include <stdio.h>
#include <string.h>
#include <math.h>

int main () {
    int n;

    FILE * file=fopen("tabela.txt","wt");
    fprintf(file,"---------------------------\n");
    fprintf(file,"|         n |  n log_2(n) |\n");
    fprintf(file,"---------------------------\n");
    for (n=1;n<=100000;n++) {
        fprintf(file,"| %9d | %9.1lf |\n",n,n*log2((double)n));
    }
    fprintf(file,"---------------------------");
    fclose(file);

    return 0;
}