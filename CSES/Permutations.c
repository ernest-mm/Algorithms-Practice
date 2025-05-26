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
