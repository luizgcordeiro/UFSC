/*
    1-1 Comparison of running times
    For each function f(n) and time t in the following table,determine the largest
    size n of a problem that can besolvedin time t, assuming that the algorithm to
    solve the problem takes f(n) microseconds.

    We assume 30 days in a month, 365 days in a year
             
            | 1 sec    | 1 min      | 1 hour      | 1 day        | 1 month       | 1 year         | 1 century       |
    --------|----------|------------|-------------|--------------|---------------|----------------|-----------------|
    lg(n)   | 2^(10^6) | 2^(6*10^7) | 2^(36*10^8) | 2^(864*10^8) | 2^(2592*10^9) | 2^(31536*10^9) | 2^(31536*10^11) |
    sqrt(n) | 10^12    | (6*10^7)^2 | (36*10^8)^2 | (864*10^8)^2 | (2592*10^9)^2 | (31536*10^9)^2 | (31536*10^11)^2 |
    n       | 10^6     | (6*10^7)   | (36*10^8)   | (864*10^8)   | (2592*10^9)   | (31536*10^9)   | (31536*10^11)   |
    n lg(n) | 62746*   |
    n^2     | 10^3     |
    n^3     | 10^2     |
    2^n     | 19       |
    n!      | 9        |
    -------- ---------- 

    Note that 1 sec=10^6 microseconds.
    *Vide programa abaixo
*/

#include <stdio.h>
#include <math.h>

int main () {
    /*Find n such that nlg(n)=10^6
    
    I.e., n=10^6/lg(n)
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
    */

    double n=100000;
    double n_new=1000000/log2(n);

    while (n!=n_new) {
        n=n_new;
        n_new=1000000/log2(n_new);
    }

    printf("Aproximacao da solucao: %lf.16.\n",n_new);
    printf("Note que se n=%.0lf, entao n*lg(n)=%lf.\n",floor(n_new),floor(n_new)*log2(floor(n_new)));
    printf("Note que se n=%.0lf, entao n*lg(n)=%lf.\n",ceil(n_new),ceil(n_new)*log2(ceil(n_new)));
    printf("Portanto, %.0lf e a solucao.\n",floor(n_new));
    return 0;
}
