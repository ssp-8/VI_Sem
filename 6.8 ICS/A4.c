#include <stdio.h>
#include <string.h>

int main() {
    int num;

    scanf("%d", &num);

    char* roman_numerals[] = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
    int values[] = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
    char roman_number[20] = "";
    
    for (int i = 0; i < 13; i++) {
        while (num >= values[i]) {
            strcat(roman_number, roman_numerals[i]);  
            num -= values[i];  
        }
    }

    printf("%s\n", roman_number);
    
    return 0;
}
