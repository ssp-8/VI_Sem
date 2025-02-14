#include <stdio.h>

int main() {
    int n,temp;

    printf("Enter the number of rings: ");
    scanf("%d",&n);

    if(n<=0){
        printf("Invalid input. Number of rings must be positive\n");
        return 1;
    }
    int a = 0,b = 1, sum = 0;
    for(int i = 1;i <= n;i++) {
        temp = a+b;
        a = b;
        b = temp;
        sum = sum + a;
    }
    printf("Total number of circles: %d\n",sum);
}