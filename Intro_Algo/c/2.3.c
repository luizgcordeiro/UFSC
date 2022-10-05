#include <stdio.h>
#include <stdlib.h>
#include <time.h>
//#include <stdarg.h> // function arguments
//#include <math.h> // math
#include <string.h>

void print_int_vector(int * v , int n) {
  //Prints an an-sized integer vector v

  printf( "[" );
  int i;
  for (i=0;i<n-1;i++) {
    printf(" %d ,",v[i]);
  }
  printf(" %d ]",v[i]);
  return;
}

void create_int_vector ( int * v , int n ) {
  //Randomly creates an n-sized integer vector v

  srand(time(NULL));

  for ( int i=0;i<n;i++) {
    v[i]=rand()%100;
  }
  return;
}

void merge (int * A , int p , int q , int r) {
    //Merges A[p,q] and A[q+1,r], where p<=q<r
    int n1=q-p+1;
    int n2=r-q;
    int L[n1] , R[n2];
    for (int i=0;i<n1;i++) {
        L[i]=A[p+i];
    }
    for (int j=0;j<n2;j++) {
        R[j]=A[q+1+j];
    }
    int i=0,j=0,k=p;
    while (i<n1 && j<n2) {
        if (L[i]<=R[j]) {
            A[k++]=L[i++];
        } else {
            A[k++]=R[j++];
        }
    }

    while (i<n1) {
        A[k++]=L[i++];
    }

    while (j<n2) {
        A[k++]=R[j++];
    }
}

void merge_sort ( int * A , int p , int r ) {
    if (p==r) {
        return;
    }
    int q=(p+r)/2;
    merge_sort(A,p,q);
    merge_sort(A,q+1,r);
    merge(A,p,q,r);
}

/*int main( int argc , char ** argv ) { // Test for merge-sort
    srand(time(NULL));

    int n=100000000;
    int number=10;

    int * v[number];
    for (int i=0;i<number;i++) {
        v[i]=malloc(n*sizeof(int));
        create_int_vector(v[i],n);
        merge_sort(v[i],0,n-1);
    }


    return 0;
}*/

/*
    2.3-1
    Using Figure 2.4 as a model, illustrate the operation of merge sort on
    the array A=[3,41,52,26,38,57,9,49].

    SOLUTION:
    Upside down for simplicity in writing:
    [3] [41]   [52] [26]   [38] [57]   [9] [49]
    --------   ---------   ---------   --------
     merge       merge       merge      merge
    --------   ---------   ---------   --------
     [3 41]     [26 52]     [38 57]     [9 49]
     ------------------     ------------------
           merge                  merge
     ------------------     ------------------
        [3 26 41 52]           [9 38 49 57]
        -----------------------------------
                       merge
        -----------------------------------
              [3 9 26 38 41 49 52 57]
*/

/*
    2.3-2
    Rewrite the MERGE procedure so that it does not use sentinels, instead
    stopping once either array L of R has had all its elements copied back
    to A and the copying the remainder of the other array back into A.

    SOLUTION:

    Lines 1-7 are basically the same (except L and R have one entry less).
    Lines 8 and 9 of the original algorithm were removed, and the "for" loop
    starting in line 12 of the original algorithm is where the changes start
    MERGE(A,p,q,r)
    1.  n1 = q-p+1
    2.  n2 = r-q
    3.  let L[1..n1] and R[1..n2] be new arrays
    4.  for i=1 to n1
    5.      L[i]=A[p+i-1]
    6.  for j=1 to n2
    7.  R[j]=A[q+j]
    8.  i=1
    9.  j=1
    10. k=1
    11. while i<=n1 and j<=n2    
    12.     if L[i]<=R[j]
    13.         A[k]=L[i]
    14.         i=i+1
    15.     else
    16.         A[k]=R[j]
    17.         j=j+1
    18.     k=k+1
        //Just need to copy the remainders. One of them will be empty.
    19. while i<=n1
    20.     A[k]=L[i]
    21.     i=i+1
    22.     k=k+1
    23. while j<=n2
    24.     A[k]=R[j]
    25.     j=j+1
    26.     k=k+1
*/

/*
    2.3-3
    Use mathematical induction to show that when n is an exact power of 2, the solution of the recurrence
        T(2)=2
        T(n)=2T(n/2)+n if n=2^k, for k>1
    is T(n)= n lg(n)

    SOLUTION:
    Assuming n=2^k. For k=1:
    T(n)    =   T(2^k)
            =   T(2^1)
            =   T(2)
            =   2
            =   2*1
            =   2 * lg(2)
            =   2^1 * lg(2^1)
            =   2^k * lg(2^k)
            =   n * lg(n)
    
    If the result holds for a certain k, and n=2^(k+1), then
    T(n)    =   T(2^(k+1))
            = 2 T(2^k)+2^(k+1)
            = 2*(2^k lg(2^k)) + 2^(k+1)
            = 2^(k+1) * (lg(2^k) + 1)
            = 2^(k+1) * (k+1)
            = n * lg(2^(k+1))
            = n * lg(n)
    so the result also holds for k+1.
*/

/*
    2.3-4
    We can express insertion sort as a recursive procedure as follows. In
    order to sort A[1..n], we recursively sort A[1..n-1] and then insert
    A[n] into the sorted array A[1..n-1]. Write a recurrence for the running
    time of this recursive version of insertion sort.

    SOLUTION:

    The recursive version of insertion sort and its running time (collapsing
    the Theta notation) is given by
    
        INSERTION-SORT(A)           times   cost
        if n==1                     1       1
            break                   1       1
        INSERTION-SORT(A[1..n-1])   1       T(n-1)
        key = A[n]
        i=n-1                       1       1
        while i>0 and A[i]>key      t       1
            A[i+1] = A[i]           t-1     1
            i=i-1                   t-1     1
        A[i+1]=key                  1       1

    where t = n in the worst case. So T(n) = T(n-1) + Theta(n).

    Remark: 2.3-6 deals with what is usually called BINARY-INSERTION-SORT,
    which looks like it would be an improvement on binary search but is not.
*/

/*
    2.3-5
    Referring back to the searching problem (see Exercise 2.1-3), observe
    that if the sequence A is sorted, we can check the midpoint of the
    sequence against v and eliminate half of the sequence from further
    consideration. The BINARY SEARCH algorithm repeats this procedure,
    halving the size of the remaining portion of the sequence each time.
    Write pseudocode, either iterative or recursive, for binary search.
    Argue that the worst-case running time of binary search if Theta(lg n)

    SOLUTION

    BINARY-SEARCH(v,A), iterative version
    L=1
    R=A.length
    while L<=R
        m = floor((L+R)/2)
        if A[m]=v
            return m
        else if A[m]<v
            L=m+1
        else
            R=m-1
    return NIL

    BINARY-SEARCH(v,A,p,q), recursive version 1
    // Searches for v in A[p..q]
    m = floor((p+q)/2)
    if p>q
        return NIL
    if A[m]=v
        return m
    if A[m]<v
        return BINARY-SEARCH(v,A,m+1,q)
    return BINARY-SEARCH(v,A,p,m-1)

    To find the index index at which A[m]=v, call
        BINARY-SEACH(v,A,1,A.length)

    BINARY-SEARCH(v,A) recursive version 2
    // We assume sum with NIL returns NIL
    n=A.length // Could also be a parameter
    if n=0
        return NIL
    m=floor((1+n)/2)
    if A[m]=v
        return m
    if A[m]<v
        return m + BINARY-SEARCH(v,A[m+1..n]) 
    return BINARY-SEARCH(v,A[1..(m-1)])

    
    Let us analyse the worst-case running time for the iterative version. In
    the first iteration of the "while" loop, the difference R-L starts as
    being n-1. At each other time, the new value of R-L is strictly smaller
    than half of what it was in the previous iteration. In the worst case,
    the loop exists when R<L. If the loop is run through k=lg(n) times, then
    at the end we have
        R-L <= (n-1)/2^k < n/2^k = n/n = 1,
    so R-L<=0. The loop will run at most one more time, after which it will
    necessarily terminate. Each other line in the code has constant time,
    so the final cost will be Theta(lg(n)) + Theta(1) = Theta(lg(n)).

    Alternatively, looking at any of the recursive versions, we see that
    the cost satisfies the recursion
        T(n)=T(n/2)+c, T(1)=c
    for some cost c, in a manner similar to the the book's analysis of merge
    sort. If n=2^k, then by induction we obtain
        T(n)=T(2^k)=(k+1)c = clg(n) + c = Theta(lg(n)).
*/

/*
    2.3-6
    Observe that the while loop of lines 5-7 of the INSERTION-SORT procedure
    in Section 2.1 uses a linear seach to scan (backward) through the sorted
    subarray A[1..j-1]. Can we use a binary search (see Exercise 2.3-5)
    instead to improve the overall worst-case running time of insertion sort
    to Theta(n lg(n))?

    SOLUTION:
    We can use a variation of binary search to find the position on which to
    place the key. However, we will still need to shift elements linearly,
    which takes up to Theta(n) time for arrays contiguously stored in
    memory (which is the model specified in the fourth edition of the book).

    So, looking at the recursive version of insertion sort in Exercise
    2.3-4 (properly modified so as to include a binary search), the running
    time would satisfy the equation
        T(n)=T(n-1)+Theta(lg(n))+Theta(n),
    which still is T(n)=Theta(n^2)
    
    One could even try to use linked lists to make shifting cheaper, but
    then binary search would become inefficient.
*/

/*
    2.3-7*
    Describe a Theta(n lg(n))-time algorithm that, given a set S of n
    integers and another integer x, determines whether or not there exist
    two elements in S whose sum is exactly x.

    SOLUTION:
    
    1.  MERGE-SORT(S)
    2.  a=1
    3.  b=n
    4.  while a<b
    5.      if S[a]+S[b]=x
    6.          return TRUE
    7.      if S[a]+S[b]<x
    8.          a=a+1
    9.      else
    10.         b=b-1
    11. return FALSE

    Line 1 takes time Theta(n lg(n)) and all others are constant, with
    the while loop running at most n times, so we have cost
        Theta(n lg(n)) + Theta(n) = Theta(n lg(n))

    This algorithm can be modified to an algorithm which solves an equation
    of the form f(S[a],S[b])=x, with f entrywise monotonic. The condition in
    line 4 should then be changed to "a<=n and b>=0", and the sum in lines 5
    and 7 should be changed to f. We could probably also do a binary search
    entrywise instead of linearly adding/subtracting 1, but the overall
    running time would still be Theta(n lg(n)) (although smaller).
*/

/*
    2-1 Insertion sort on small arrays in merge sort
    Although merge sort runs in Theta(n lg(n))) worst-case time and
    insertion sort runs in Theta(n^2) worst-case time, the constant factors
    of insertion sort can make it faster in practice for small problem sizes
    on many machines. Thus, it makes sense to coarsen the leaves of the
    recursion by using insertion sort within merge sort when subproblems
    become sufficiently small. Consider a modification to merge sort in
    which n/k sublists of length k are sorted using insertion sort and then
    merged using the standard mergin mechanism, where k is a value to be
    determined.

    a. Show that insertion sort can sort the n/k sublists, each of length k,
    in Theta(nk) worst-case time.
    b. Show how to merge the sublists in Theta(n lg(n/k)) worst-case time
    c. Given that the modified algorithm runs in Theta(nk + n lg(n/k))
    worst-case time, what is the largest value of k as a function of n for
    which the modified algorithm has the sas running time as standard
    merge sort, in terms of Theta-notation?
    


    
