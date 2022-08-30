#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main ( int argc , char ** argv) {

    unsigned char bits[sizeof(double)];
    char run='S',gravar='S',c,filename[105];
    double num,twoexp;
    int i,j;
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

        printf("\n\nA representacao em memoria deste numero e\n");
        memcpy(&bits,&num,sizeof(double));
        printf("%u ",bits[7]/128);
        printf("%u%u%u%u%u%u%u",
            (bits[7]/64)%2,
            (bits[7]/32)%2,
            (bits[7]/16)%2,
            (bits[7]/8)%2,
            (bits[7]/4)%2,
            (bits[7]/2)%2,
            (bits[7])%2);
        printf("%u%u%u%u ",
            (bits[6]/128)%2,
            (bits[6]/64)%2,
            (bits[6]/32)%2,
            (bits[6]/16)%2);
        
        printf("%u%u%u%u",
            (bits[6]/8)%2,
            (bits[6]/4)%2,
            (bits[6]/2)%2,
            (bits[6])%2);
        
        for (i=5;i>=0;i--) {
            printf("%u%u%u%u%u%u%u%u",
            (bits[i]/128)%2,
            (bits[i]/64)%2,
            (bits[i]/32)%2,
            (bits[i]/16)%2,
            (bits[i]/8)%2,
            (bits[i]/4)%2,
            (bits[i]/2)%2,
            (bits[i])%2);
        }

        printf("\n\n");

        printf("Voce quer grava-lo num arquivo (S/N)? ");
        gravar=getchar();
        while ((c=getchar())!=EOF && c!='\n');

        if (gravar=='S' || gravar=='s') {
            FILE * file=fopen(filename,"wb");

            if (file==NULL) {
                printf("Erro: Nao foi possivel criar o arquivo.");
                getchar();
                break;
            }
            fwrite(&num,sizeof(double),1,file);
            fwrite(bits,1,1,file);
            fclose(file);

            printf("Arquivo %s gravado com sucesso.\n",filename);
        }
        /*
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
        }*/
        printf("\n\n");
        printf("Voce quer representar outro numero (S/N)? ");
        run=getchar();
        while ((c=getchar())!=EOF && c!='\n');
    }

    
    return 0;
}