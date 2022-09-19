#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main ( int argc , char ** argv) {

    char run='S',gravar='S',c,filename[105];
    double num,num_or;
    int i,j;
    char sign,exponent[12],mantissa[53],k,p;

    exponent[11]=0;
    mantissa[52]=0;
    while (run=='S' || run=='s') {
        printf("==========\n");
        printf("Digite um numero decimal: ");
        scanf("%lf",&num_or);

        while ((c=getchar())!=EOF && c!='\n');
        num=num_or;
        
        //Calcular representacao em bits
        //SINAL
        if (num>=0) {
            sign='0';
        } else {
            sign='1';
            num=-num;
        }

        //EXPOENTE: O numero p tal que 2^p<=num<2^(p+1), transladado 1023
        //Vamos quebrar no caso em que num > ou <1
        p=0;
        if (num>=1) {
            while (num>= 2) {
                p++;
                num/=2;
            }
        } else {
            while (num<1) {
                p--;
                num*=2;
            }
        }

        k=p+1023;
        printf("exponent:%d\n",k);
        for (i=10;i>=0;i--) {
            printf("exponent:%d\n",k);
            j=k%2;
            exponent[i]='0'+j;
            k-=j;
            k/=2;
        }
        printf("exponent:%d\n",k);

        //Operações bit a bit para lidar com a mantissa
        num-=1;//Tira a parte inteira, faz ser somente a mantissa
        for (i=0;i<52;i++) {
            num*=2;
            mantissa[i]='0'+((int)num%2);
            if (mantissa[i]=='1') {
                num-=1;
            }
        }

        printf("A representacao em bits desse numero e\n\n");
        printf("%c   ",sign);
        printf(exponent);
        printf("   ");
        printf(mantissa);

        printf("\n\n");

        printf("Voce quer grava-lo num arquivo (S/N)? ");
        gravar=getchar();
        while ((c=getchar())!=EOF && c!='\n');

        if (gravar=='S' || gravar=='s') {

            snprintf(filename,100,"%.4lf",num_or);

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

            FILE * file=fopen(filename,"wb");

            if (file==NULL) {
                printf("Erro: Nao foi possivel criar o arquivo.");
                getchar();
                break;
            }

            fwrite(&num_or,sizeof(double),1,file);
            printf("Arquivo %s gravado com sucesso.\n",filename);
            fclose(file);
        }
            
        printf("\n");
        printf("Voce quer representar outro numero (S/N)? ");
        run=getchar();
        while ((c=getchar())!=EOF && c!='\n');
    }

    
    return 0;
}