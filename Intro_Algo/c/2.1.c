#include <stdio.h>
//#include <math.h>

void insertion_sort(int * A, int n) {
    //Insertion sort on an integer array of length n

    int j;
    for (j=1;j<n;j++) {
        int key = A[j]
        int i=j-1;
        while (i>=0 && A[i]>key) {
            A[i+1]=A[i];
            i--;
        }

        A[i+1]=key;
    }
}

/*
    2.1-1
    Using Figure2.2 as a model, illustrate the operation of INSERTION-SORT on the
    array A=<31,41,59,26,41,58.

    (a)      __
        31  |41|  59  26  41  58
             ^^
    (b)          __
        31  41  |59|  26  41  58
                 ^^
    (c)              __
        31->41->59->|26|  41  58
        ^-------------^
    (d)                  __
        26  31  41  59->|41|  58
                    ^-----^
    (d)                      __
        26  31  41  41  59->|58|
                        ^-----^
*/

/*
    2.1-2
    Rewrite the INSERTION-SORT procedure to sort into nonincreasing instead of non-
    decreasing order.

    Change  "A[i]>key" by "A[i]<key" in line 5
*/

/*
    2.1-3
    Consider the searching problem:
    Input: A sequence of n numbers A=<a1,a2,...,an> and a value v
    Output: An index i such that v=A[i] or the special value NIL if v does not
      appear in  A.
    Write pseudocode for LINEAR SEARCH, which scans through the sequence, looking
    for v. Using a loop invariant, prove that your algorithm is correct. Make sure that
    your loop invariant fulfills the three necessary properties

    for j=1 to n
        if v=A[j]
            return j
    return NIL

    Loop invariant: At the start of the j-th iteration, v does not appear in  A[1..j-1]
    Initialization: Trivial (vacuous) for j=1
    Maintenance: Suppose the invariant was true before the j-th iteration, and that we
      are at the (j+1)-th iteration. This means that the procedure didn't return during
      the j-th iteration, i.e., that the condition "v=A[j]" was not true. Thus v is not
      A[j], nor does it appear in A[1..j-1] (by hypothesis), so it does not appear in
      A[1..j]=A[1..((j+1)-1)], as desired (the loop invariant at step j+1)
    Termination: The loop terminates under two possibilities:
      1st: It returns j, which only happens if "v=A[j]"" evaluates to True at some j.
        Moreover, "v=A[j']"" does not evaluate to True at any j'<j. So in this case
        the process actually returns the FIRST index j for which A[j]=v (and not just
        any such index).
      2nd: j gets to n+1. The loop invariant then tells us that v does not appear in
        A[1..n], and the process returns NIL, as desired.
*/

/*
    2.1-4
    Consider the problem of adding two n-bit binary integers, stored in two n-element
    arrays A and B. The sum of the two integers should be stored in binary form in
    an (n+1)-element array C. State the problem formally and write pseudocode for
    adding the two integers

    INPUT: n-element binary (0-1) arrays A and B, representing binary numbers between
      0 and 2^n-1
    OUTPUT: (n+1)-element binary (0-1) array C, representing A+B
    (remark: we use little endian: <x(0),x(1),x(2),...> represents the sum of 2^ix(i))

    We have two possibilities: First, do sum as usual. Store "along" as the number which
    goes through to the next digit along addition
    1.  along=0
    2.  for i=1 to n
    3.    //We have to sum A[i]+B[i]+along and update the result and the new along
    4.    //We do it without addition
    5.    if A[i]=B[i] //result will be 00 or 01 (little-endian); either way C[i]=along
    6.      C[i]=along
    7.      if A[i]=1  //result was 01
    8.        along=1
    9.      else
    10.       along=0
    11.   else        //A[i] and B[i]  are different: one is 0; other is 1
    12.     if along=1 //A[i]+B[i]+along=01
    13.       C[i]=0
    14.       //along=1, no need to update
    15.     else      //A[i]+B[i]+along=10
    16.       C[i]=1
    17.       //along=0, no need to update
    18. C[i]=along

    The second possibility is summing digit-of-B-by-digit-of-B to A (or vice-versa),
    from left to right.
    1.  C=<A,0>         //Make a copy of A to add digits of B
    2.  for i=1 to n    //Go digit-by-digit
    3.    if B[i]=1     //If B[i]=0, nothing to do
    5.      j=i
    6.      while C[j]=1//Go summing 1 along a sequence of 1s
    7.        C[j]=0
    8.        j+=1
    9.      C[j]=1
