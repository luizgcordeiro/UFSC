/*
    1-1 Comparison of running times
    For each function f(n) and time t in the following table,determine the largest
    size n of a problem that can besolvedin time t, assuming that the algorithm to
    solve the problem takes f(n) microseconds.

    We assume 30 days in a month, 365 days in a year. the tabl

                ---------- ------------ ------------- -------------- --------------- ---------------- -----------------   
               | 1 sec    | 1 min      | 1 hour      | 1 day        | 1 month       | 1 year         | 1 century       |
      ---------|----------|------------|-------------|--------------|---------------|----------------|-----------------|
    | lg(n)    | 2^(10^6) | 2^(6*10^7) | 2^(36*10^8) | 2^(864*10^8) | 2^(2592*10^9) | 2^(31536*10^9) | 2^(31536*10^11) |
    | sqrt(n)  | 10^12    | (6*10^7)^2 | (36*10^8)^2 | (864*10^8)^2 | (2592*10^9)^2 | (31536*10^9)^2 | (31536*10^11)^2 |
    | n        | 10^6     | (6*10^7)   | (36*10^8)   | (864*10^8)   | (2592*10^9)   | (31536*10^9)   | (31536*10^11)   |
    | n lg(n)* | 62746    | 2801417    | 133378058   | 2755147513   | 71870856404   | 797633893349   | 68610956750570  |
    | n^2*     | 10^3     | 7745       | 60000       | 293938       | 1609968       | 5615692        | 56156922        |
    | n^3*     | 10^2     | 391        | 1532        | 4420         | 13736         | 31593          | 146645          |
    | 2^n*     | 19       | 25         | 31          | 36           | 41            | 44             | 51              |
    | n!*      | 9        | 11         | 12          | 13           | 15            | 16             | 17              |
     ---------- ---------- ------------ ------------- -------------- --------------- ---------------- -----------------

    Note that 1 sec=10^6 microseconds.
    *Vide programa abaixo
*/

#include <stdio.h>
#include <math.h>

unsigned long long int pow2( int n ) {
    if (n==0) {
        return 1;
    }
    return 2*pow2(n-1);
}

unsigned long long int Pow10( int n ) {
    if (n==0) {
        return 1;
    }
    return 10*Pow10(n-1);
}

double log2fact( int n ) {
    if (n==1) {
        return 0;
    }
    return log2(n)+log2fact(n-1);
}

int main () {
    /*
    The following is not used anymore:

    ==================================
    Find largest n such that nlg(n)<=10^6
    
    Solving n=10^6/lg(n)
    This yields a fixed point iteration

    We can guess 10^4<n<10^5 elementary. The derivative satisfies
    (10^6/lg(n))'=10^6 lg'(n)/lg(n)^2
    Note that
    lg'(n)=1/(n log(2))=lg(10)/n,
    so (10^6/lg(n))'=10^6 * lg(10)/(n lg(n)^2)
    At the solution, we have
    (10^6/lg(n))'=10^6*lg(10)/(10^6 * lg(n))=log_n(10)
    Since the solution satisfies n>10^4, the derivative is <1/4.
    Moreover, the derivativeis decreasing after 10^4

    Therefore the fixed point iteration will converge for the initial guess n=10^5.

    This yields 62746
    ==================================

    Instead, we do a simple search by a variation of bisection.
    */

    unsigned long long int v[7] = {Pow10(6) , 6*Pow10(7) , 36*Pow10(8) , 864*Pow10(8) , 2592*Pow10(9) , 31536*Pow10(9) , 31536*Pow10(11)};
    unsigned long long int n_l,n_u,mi;//lower n, upper n, middle

    /*
        Find largest n such that n lg n<= 10^6
    */

    int i;

    printf("==========\n");

    for (i=0;i<7;i++) { 
        n_l=0;
        n_u=1;

        /*
            Let n_l be the largest power of 2 satisfying the inequality,
            and n_u be the next one.
        */
        while (n_u * log2((double)n_u)<=v[i]) {
            n_l=n_u;
            n_u*=2;
        }

        /*
            Apply bisection method
        */
        while (n_l+1!=n_u) {
            mi=(n_l+n_u)/2;

            if (mi * log2((double)mi)<=v[i]) {
                n_l=mi;
            } else {
                n_u=mi;
            }
        }

        printf("The largest integer n for which n*lg(n)<=%llu is n=%llu.\n",v[i],n_l);
    }
    
    printf("==========\n");

    /*
        Find largest n such that n^2<= ...
    */

    for (i=0;i<7;i++) { 
        n_l=0;
        n_u=1;

        /*
            Let n_l be the largest power of 2 satisfying the inequality,
            and n_u be the next one.
        */
        while (n_u*n_u<=v[i]) {
            n_l=n_u;
            n_u*=2;
        }

        /*
            Apply bisection method
        */
        while (n_l+1!=n_u) {
            mi=(n_l+n_u)/2;

            if (mi*mi<=v[i]) {
                n_l=mi;
            } else {
                n_u=mi;
            };
        }

        printf("The largest integer n for which n^2<=%llu is n=%llu.\n",v[i],n_l);
    }
    
    printf("==========\n");

    /*
        Find largest n such that n^3<= ...
    */

    for (i=0;i<7;i++) { 
        n_l=0;
        n_u=1;

        /*
            Let n_l be the largest power of 2 satisfying the inequality,
            and n_u be the next one.
        */
        while (n_u*n_u*n_u<=v[i]) {
            n_l=n_u;
            n_u*=2;
        }

        /*
            Apply bisection method
        */
        while (n_l+1!=n_u) {
            mi=(n_l+n_u)/2;

            if (mi*mi*mi<=v[i]) {
                n_l=mi;
            } else {
                n_u=mi;
            };
        }

        printf("The largest integer n for which n^3<=%llu is n=%llu.\n",v[i],n_l);
    }
    
    printf("==========\n");

    /*
        Find largest n such that 2^n<= ...
        To avoid overflow, take lg on both sides, i.e., find largest n such that n<=lg(...)
    */

    for (i=0;i<7;i++) { 
        n_l=0;
        n_u=1;

        /*
            Let n_l be the largest power of 2 satisfying the inequality,
            and n_u be the next one.
        */
        while (n_u<=log2(v[i])) {
            n_l=n_u;
            n_u*=2;
        }

        /*
            Apply bisection method
        */
        while (n_l+1!=n_u) {
            mi=(n_l+n_u)/2;

            if (mi<=log2(v[i])) {
                n_l=mi;
            } else {
                n_u=mi;
            };
        }

        printf("The largest integer n for which 2^n<=%llu is n=%llu.\n",v[i],n_l);
    }
    
    printf("==========\n");

    /*
        Find largest n such that n!<= ...

        Again, to avoid overflow, take lg on both sides
    */

    
    for (i=0;i<7;i++) { 
        n_l=0;
        n_u=1;

        /*
            Let n_l be the largest power of 2 satisfying the inequality,
            and n_u be the next one.
        */
        while (log2fact(n_u)<=log2(v[i])) {
            n_l=n_u;
            n_u*=2;
        }

        /*
            Apply bisection method
        */
        while (n_l+1!=n_u) {
            mi=(n_l+n_u)/2;

            if (log2fact(mi)<=log2(v[i])) {
                n_l=mi;
            } else {
                n_u=mi;
            };
        }

        printf("The largest integer n for which n!<=%llu is n=%llu.\n",v[i],n_l);
    }
    return 0;
}
