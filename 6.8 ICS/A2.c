#include <stdio.h>

int main() {

    int roll_number;
    scanf("%d",&roll_number);
    int no_of_digits = 0;
    int sum_of_digits = 0;

    while(roll_number >= 1) {
        int digit = roll_number % 10;
        no_of_digits+=1;
        sum_of_digits+=digit;
        roll_number = roll_number / 10;
    }

    if((sum_of_digits % 2 == 0) && (no_of_digits % 2 == 0)) {
        printf("Ravenclaw");
    }
    else if(sum_of_digits % 2 == 0) {
        printf("Hufflepuff");
    }
    else if(no_of_digits % 2 == 0){
        printf("Slytherin");
    } else {
        printf("Gryffindor");
    }
    return 0;
}