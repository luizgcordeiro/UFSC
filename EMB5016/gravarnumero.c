#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main ( int argc , char ** argv) {

    char run='S',c,filename[105];
    double num,twoexp;
    int i;
    int sign,exponent[11],mantissa[52],k,p;
    while (run=='S' || run=='s') {
        printf("Digite um numero decimal: ");
        scanf("%lf",&num);
        snprintf(filename,100,"%.4lf",num);

        for (i=0;filename[i]!=0;i++) {
            if (filename[i]=='.') {
                filename[i]='_';
            }
        }
        filename[i++]='.';
        filename[i++]='b';
        filename[i++]='i';
        filename[i++]='n';
        filename[i]=0;
        //Clear 
        while ((c=getchar())!=EOF && c!='\n');

        FILE * file=fopen(filename,"wb");

        if (file==NULL) {
            printf("Erro: Nao foi possivel criar o arquivo.");
            getchar();
            break;
        }
        fwrite(&num,sizeof(double),1,file);
        fclose(file);

        printf("Arquivo gravado com sucesso.\n");
        //O numero esta gravado
        //Calcular representacao em bits
        if (num>=0) {
            sign=0;
        } else {
            sign=1;
            num=-num;
        }

        printf("numero: %20lf\n",num);

        //Agora achar o expoente: O numero p tal que 2^p<=num<2^(p+1).
        //Vamos quebrar no caso em que num > ou <1
        p=0;
        twoexp=1;
        printf("EXPONENT:\n");
        if (num>=1) {
            while (num>= 2*twoexp) {
                p++;
                num/=2;
                printf("numero: %20lf\n",num);
            }
        } else {
            while (num<twoexp) {
                p--;
                num*=2;
                printf("numero: %20lf\n",num);
            }
        }

        k=p+1023;
        for (i=10;i>=0;i--) {
            exponent[i]=k%2;
            k-=exponent[i];
            k/=2;
        }

        printf("MANTISSA:\n");
        for (i=0;i<52;i++) {
            num*=2;
            mantissa[i]=((int)num)%2;
            if (mantissa[i]==1) {
                num-=1;
            }
            printf("numero: %20lf\n",num);
        }

        printf("A representacao em bits desse numero e\n\n");
        printf("%d   ",sign);
        for (i=0;i<11;i++) {
            printf("%d",exponent[i]);
        }
        printf("   ");
        for (i=0;i<52;i++) {
            printf("%d",mantissa[i]);
        }
        printf("\n\n");
        printf("Voce quer gravar outro arquivo (S/N)? ");
        run=getchar();
        while ((c=getchar())!=EOF && c!='\n');
    }
    
    
    return 0;
}