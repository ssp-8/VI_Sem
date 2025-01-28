#include <stdio.h>
#include <string.h>

#define N 26

int main(){
    char m [] = "OVDTHUFWVZZPISLRLFZHYLAOLYL";

    for(int i = 0;i <N;i++){
        char d [strlen(m)];
        int j;
        for(j = 0;m[j]!= '\0';j++){
            char c = m[j]-65;
            if(c-i <0){
                c = (26-c-i)%N;
            }
            else {
            c = (c-i)%N;}
            d[j] = c+65;
        }
        d[j] = '\0';
        printf("For i = %d m = %s\n",i,d);
    }

}