/*
A permutation of integers 1,2,...,n is called beautiful 
if there are no adjacent elements whose difference is 1.

Given n, construct a beautiful permutation if such a permutation exists.

Input
The only input line contains an integer n.
Output
Print a beautiful permutation of integers 1,2,...,n. 
If there are several solutions, you may print any of them. 
If there are no solutions, print "NO SOLUTION".

Constraints

1 <= n <= 10^6

Example 1
Input:
5

Output:
4 2 5 3 1
Example 2
Input:
3

Output:
NO SOLUTION
*/
#include <stdio.h>

void beautiful_permutation(int n){
    int i;
    if (n == 1){
        printf("%d", 1);
    }
    else if (n <= 3){
        printf("NO SOLUTION");
    }
    else {
        printf("2");
        for (i=4; i<=n; i+=2) {
            printf(" %d", i);
        }
        for (i=1; i<=n; i+=2) {
            printf(" %d", i);
        }
    }
}

int main(void){
    int n;
    scanf("%d", &n);
    beautiful_permutation(n);
    return 0;
}
