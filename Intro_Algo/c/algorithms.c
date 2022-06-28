#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {

    char * dict[3];

    char * str1="banana";

    char * str2="babaca";

    char * str3="carambola";

    dict[0]=str1;
    dict[1]=str2;
    dict[2]=str3;
    
    printf("yeah");
    return 0;
}

/*
    Section 2.1
*/

void insertion_sort(int * v , int n) {
    /*
        Insertion sort algorithm.

        Takes an array v of length n and sorts it by InsertionSort.
    */

   int j;

   for (j=1;j<n;j++) {
    int key=v[j]; //This is the value which will be compared to the previous ones
    int i=j-1;

    while (i>=0 && v[i]>key) {
        v[i+1]=v[i];
        i--;
    }

    v[i+1]=key;
   }
}

int word_compare(char * str1,char * str2) {
    /*
        Compares two strings str1 and str2 lexicographically.

        Returns 1 if the second is greater; 0 otherwise.

        Equivalently, gives the Boolean value of "str2>str1"
    */

   int i=0;
   for (i=0; str1[i]==str2[i]; i++);
   
   //i is the first index at which str1 and str2 differ

   if (str1[i]<str2[i]) {
    return 1;
   }

   return 0;
}

void insertion_sort_dictionary (char ** dict, int n) {
    /*
        Sorts a dictionary with n words
    */

    int j;

   for (j=1;j<n;j++) {
    char * key=dict[j]; //This is the value which will be compared to the previous ones
    int i=j-1;

    while (i>=0 && word_compare(key,dict[i])) {
        strcpy(dict[i+1],dict[i]);
        i--;
    }

    strcpy(dict[i+1],key);
   }
}