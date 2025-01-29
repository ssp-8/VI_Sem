#include <stdio.h>

int main() {
    int N,F,final_sum = 0;
    scanf("%d %d\n",&N,&F);

    int image [N];
    int locket [F];

    for(int i = 0;i < N;i++){
        scanf("%d",&image[i]);
    }
    for(int i = 0;i < F;i++){
        scanf("%d",&locket[i]);
    }

    for(int i = 0; i < N-F+1;i++){
        int sum = 0;
        for(int j = 0; j < F;j++){
            sum+=(image[i+j]*locket[j]);
        }
    final_sum+=sum;
    }
    if(final_sum > 1000){
        int sum_digits = 0;
        while(final_sum > 0){
            sum_digits+=(final_sum%10);
            final_sum/=10;
        }
        printf("%d\n",sum_digits);
    }
    else {
        printf("%d\n",final_sum%10);
    }
    return 0;
}