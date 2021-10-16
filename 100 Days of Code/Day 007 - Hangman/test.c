#include <stdio.h>

int main()
{
    char passwd[3] = "hi";
    char test = 'a';
    char test2 = ((int)test + (int)passwd) / 3;
    printf(test);
    printf(test2);
    return 0;
}
