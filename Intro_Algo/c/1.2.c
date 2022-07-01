/*
    1.2 Algorithms as a technology
*/

/*
    1.2-1
    Give an example of an application that requires algorithmic contentat the application
    level, and discuss the function of the algorithms involved.

    GPS directions; Routing. Tax programs; computations.
*/

/*
    1.2-2
    Suppose we are comparing implementations of insertion sort and merge sort on the
    same machine. For inputs ofsize n, insertion sort runs in 8n^2 stesps, while merge
    sort runs in 64n lg(n) steps.For which values of n does insertion sort beat merge sort?

    8n^2<64n lg(n) iff n<lg(n^8) iff 2^n<n^8 iff 2^(n/8) <n
    Computationally (e.g. with the penultimate inequality), we find this holds 2<=n<=43.
    At n>=43, the derivative of the LHS of the last inequality is 2^(n/8)log(2)/8>2^5/16=2,
    and in particular grows greater than n and  in fact the inequality reverses.
*/

/*
    1.2-3
    What is the smallest value of n such that analgorithm whose running time is 100n^2
    runs  faster than an algorithm whose running tmie is 2^n on the same machine?

    100n^2<2^n iff lg(100)+2lg(n)<n (*)
    We can approximate lg(100)~7 to get an estimate, and focus on powers of 2.
    For n=8 we have
    lg(100)+2lg(n)<7+2lg(8)=7+2*3=13, but this is greater than n=8
    For n=16,
    lg(100)+2lg(n)<7+2lg(16)=7+2*4=15<n
    so n=16 is a good guess. Actually, the strict inequality above shows n=15 also works.
    Note that
    lg(100)=6+lg(10^2/2^6)=6+(1/2)lg(10^4/2^12)=6+(1/2)+(1/2)lg(10^4/2^13)=6.5+(1/4)lg(10^8/2^26)
    We can verify that 10^8/2^26=(10^4/2^13)^2=(10000/8192)^2<(1.25)^2<2, so lg(10^8/2^26)<1
    Similarly,
    lg(14)=3+lg(14/8)=3+(1/2)lg(196/64)=3+(1/2)+(1/2)lg(196/128)=3.5+(1/4)lg(38416/16384)>3.75,
    where the last inequality follows from 38416/16384>2
    Therefore,
    lg(100)+2lg(14)>6.5+2*3.75=6.5+7.5=14,
    so n=14 does not work

    We just need to check that no n<14 satisfies the given inequality. In fact, from our approximation
    of lg(100) we need at least n>=7. But in this case 2lg(n)>4,so in fact we just check n>=lg(100)+4>10.5,
    i.e., n>=11. But then again 2lg(n)>=6

    Checking that lg(13)>3.5 with an argument similar to the one above (or alternatively with concavity of lg:
    lg(13)>lg(8)+(13-8)*(lg(16)-log(8))/(16-8)=3+5*1/8=3.625)
    shows that n=13 does not satisfy (*), so indeed n=15 is the number we are after.

