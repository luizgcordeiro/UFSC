#include <stdio.h>
#include <stdlib.h>
#include <time.h>
//#include <stdarg.h> // function arguments
//#include <math.h> // math
//#include <string.h>

/*
    2.2-1
    Express the function n^3/1000 - 100n^2 - 100n + 3 in terms of Theta-
    notation.

    SOLUTION:
    Theta(n^3)
*/

/*
    2.2-2
    Consider sorting n numbers stored in array A by first finding the
    smallest element of A and exchanging it with the element in A[1]. Then
    find the second smallest element of A, and exchange it with A[2].
    Continue in this manner for the first n-1 elements of A. Write
    pseudocode for this algorithm, which is known as selection sort. What
    loop invariant does this algorithm maintain? Why does it need to run for
    only the first n-1 elements, rhather than for all n elements? Give the
    best-case and worst-case running times of selection sort in Theta-
    notation.

    SOLUTION:

    (We ignore individual line cost)

    SELECTION-SORT(A)                               Times ran
    1.  for j=1 to n-1                              n
    2.      //Working with subarray A[j,...]
            //Need to find the smallest element
    3.      min_index=j                             n-1
    4.      for i=j+1 to n                          sum from j=1 to n-1 of
                                                    (n-j+1)
    5.          if A[i]<A[min_index]                sum from j=1 to n-1 of
                                                    (n-j)
    6.              min_index=i                     sum from j=1 to n-1 of
                                                    sum from i=j+1 to n of
                                                    0 or 1
    7.      <Swap A[j] and A[min_index]>            n-1

    The cost changes accordingly to how many times each line is ran. Since
    only line 6. has a variation in the number of times ran, it will be the
    determining factor for the cost.

    Best case for line 6: 0
    Worst case for line 6: sum from j=1 to n-1 of (n-j) = (n-1)n/2

    In both the best and worst case, the quadratic terms in lines 4. and 5.
    will control the order of growth, which in any case will be quadratic,
    that is, Theta(n^2).

    Loop invariant: At the start of the j-th iteration, the j-1 smallest
    elements of A appear sorted in the j-1 first entries of A.

    It needs only to run up to j=n-1 because, as the loop invariant states,
    at the end of it the n-1 smallest elements of A will appear sorted in
    the first n-1 first entries of A. The remaining element will appear in
    the n-th entry of A, and it will not be any of the n-1 smallest ones,
    so it will necessarily be the n-th smallest one, i.e., the largest
    element of A. This clearly makes it so that A is already sorted.
*/

/*
    2.2-3
    Consider linear seach again (see Exercise 2.1-3). How many elements of
    the input sequence need to be checked on the average, assuming that the
    element being searched for is equally likely to be any element in the
    array? How about in the worst case? What are the average-case and worst-
    case running times of linear search in Theta-notation? Justify your
    answers.

    SOLUTION:
    Recall the pseudocode:
    
        LINEAR SEARCH:
        for j=1 to n
            if v=A[j]
                return j
        return NIL

    No info was given for unsuccesful searches, so we assume an array of
    size n and a succesful search:
    
    The running time when the value is in the i-th position is i, and this
    happens in a fraction of 1/n of all cases. Thus, the average running
    time is
        sum from i=1 to n of (1/n)*i
            = (n+1)/2.

    The worst case which happens both for an unsuccesful search and when
    the value is in the last position, in which case the running time is n.

    In any case, the running times are Theta(n).
*/

/*
    2.2-4
    How can we modify any algorithm to have a good best-case running time?

    SOLUTION:
    There are two possibilities:

    1. If the algorithm modifies or does some sort of "improvement" on some
    piece of data (e.g. the sorting algorithms we have seen), we can first
    verify if this data already satisfies whatever the algorithm aims to do.
    This can usually be done in linear time, checking byte-by-byte or
    similarly.

    (Of course, we assume "almost any agorithm" to mean a sort of algorithm
    such as the ones presented in the book. An algorithm which takes a very
    large number and verifies whether it is prime or not would not fall in
    this category.)

    2. We choose an specific input I with a known output O. Then we add a
    check to our algorithm that, given another input, checks whether it is
    the specific input I we have chosen previously. If so, we simply ignore
    all computational steps and simply yield the known output O directly.
    This can most certainly be done in linear time (first a linear-cost
    check if the input is the specific one I, and in the positive case a
    linear-cost attribution of the output as O.)   
*/