#include <stdio.h>

int main() {

    float N,I,T,S,E,P,D;
    float O,X,Y;

    scanf("%f %f %f",&N,&T,&I);
    scanf("%f %f %f %f",&P,&S,&E,&D);

    float total_time_taken = (P - D) * (N * T) + D * (3 * (N / 2)) * T;
    float ideal_time_taken = I * N * P;

    X = E * P;
    O = ((S - E) * P) / (8 * 1024);
    Y = (ideal_time_taken / total_time_taken) * 100;

    printf("%.2f %.2f %.2f\n",X,O,Y);

}