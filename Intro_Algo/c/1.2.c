/*
    1.2 Algorithms as a technology
*/

/*
    1.2-1
    Give an example of an application that requires algorithmic content at the
    application level, and discuss the function of the algorithms involved.

    GPS directions; Routing.
    Tax programs; computations.
*/

/*
    1.2-2
    Suppose that for inputs of size n on a particular computer, insertion sort runs in
    8n^2 steps and merge sort runs in 64 n lg n steps. For which values of n does
    insertion sort beat merge sort?
    
    SOLUTION:
    We need to solve
        8n^2 < 64n lg(n)
    Note that
        8n^2 < 64n lg(n)
            iff n < lg(n^8)
            iff 2^n < n^8
            iff 2^(n/8) < n
    Computationally (e.g. with the penultimate inequality), we find this holds if
    2<=n<=43. At n=44 the inequality reverses. For n>=44, the derivative of the LHS of
    the last inequality is
        2^(n/8)log(2)/8
            > 2^5 log (2)/8 (because n>=44)
            > 2^5/16    (because log(2)>1/2)
            = 2 
    so in particular it grows faster than n, which is the RHS. Thus, the inequality is
    reversed for all n>=44, and insertion sort beats merge sort precisely for n<=43.
*/

/*
    1.2-3
    What is the smallest value of n such that an algorithm whose running time is 100n^2
    runs faster than an algorithm whose running time is 2^n on the same machine?

    SOLUTION:
    We need to solve
        100n^2 < 2^n
    Note that
        100n^2 < 2^n
            iff lg(100)+2lg(n) < n (*)

    We can approximate lg(100)~7 to get an (over)estimate, and focus on powers of 2.

    For n=8 we have
        lg(100)+2lg(n)
            < 7+2lg(8)
            = 7+2*3=13,
    but this is greater than n=8. So the algorithm with running time 100n^2 is slower
    than the one with running time 2^n for n=8.

    For n=15, (actually, this calculation was first done for n=16)
        lg(100)+2lg(n)
        < 7+2lg(16)
        = 7+2*4
        = 15
        = n
    so n=15 is a good guess for the starting n for which 100n^2<2^n.

    Let us use the algorithm that computes lg in binary digit-by-digit (see Knuth's
    book) to get a better approximation of lg(100):
        lg(100)
            = lg(2^6 * 10^2/2^6)    (n=6 is the integer for which
                                        2^n <= 10^2 < 2^(n+1))
            = 6 + lg(10^2/2^6)      (properties of logarithms)
            = 6 + (1/2)lg(10^4/2^12)    (take square inside lg and divide by 2)
            = 6 + (1/2)lg (2* 10^4/2^13)    (divide and multiply by 2)
            = 6 + (1/2)+(1/2)lg(10^4/2^13)  (properties of lg)
            = 6.5+(1/4)lg(10^8/2^26)    (simplify)
    Note that
        10^8/2^26
            =(10^4/2^13)^2
            =(10000/8192)^2
            <(1.25)^2
            =1.5625
            <2,
    so lg(10^8/2^26)<1.

    Similarly,
    lg(14)
        = 3+lg(14/8)
        = 3+(1/2)lg(196/64)
        = 3+(1/2)+(1/2)lg(196/128)
        = 3.5+(1/4)lg(38416/16384)
        > 3.75,
    where the last inequality follows from 38416/16384>2.

    Therefore,
        lg(100) + 2lg(14)
            > 6.5+2*3.75
            = 6.5+7.5
            = 14,
    so for n=14, 2^n<100n^2 (in fact, it would be easy enough to just verify this
    directly: 2^14=16384, whereas 100*(14)^2=19600.)

    We just need to check that no n<14 satisfies the given inequality, which can also be
    done directly (but let us do it the hard way).
    
    Indeed, we do know that lg(100)>6, so 2^n<100^n only if n>=7. But in this case
    2lg(n)>4,so in fact we actually need
        n >= lg(100)+4
            >10.5,
    i.e., n>=11. But then again 2lg(n)>=6, so
        n >= lg(100)+2lg(6)
            > 6+6 = 12,
    thus n>=13.

    We may check that
        lg(13)>3.5
    with an argument similar to the ones above for lg(100) and lg(14), or alternatively
    we may simply use concavity of lg, as 13 belongs to the interval [8,16]:
        lg(13)
            > lg(8)+(13-8)*(lg(16)-log(8))/(16-8)
            = 3+5*1/8
            = 3.625.
    Thus, for n=13,
        lg(100) + 2lg(13) > 6+7 = 13,
    so the desired inequality is not satisfied.
    
    This proves that n=15 is the smalles number for which 100n^2<2^n.

    For n>=15, we may simply compare derivatives of lg(100) + 2lg(n) and n, which are
        (lg(100) + 2lg(n))' = 2/(log(2)*n)
            and
        n'=1

    Since log(2)>1/2, then for n>=15
        2/(log(2)*n)<4/15<1,
    so the inequality 100 n^2 <=2^n holds exactly for n>=15 (n an integer, obviously).
*/

