#include <stdio.h>
#include <stdlib.h>

int main() {
    FILE * fp=fopen("test.bin","wb");
    double x[12]={1,-1,2,-2,3,-3,0.5,-0.5,0.25,-0.25,0.75,-0.75};
    fwrite(x,sizeof(double),12,fp);
    fclose(fp);

    return 0;
}