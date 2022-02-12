#include <stdio.h>

// int main()
// {
//     float a=132.4;
//     int b=(int)a;
//     printf("%d\n",b);
//     a=139.9;
//     int c=(int)a;
//     printf("%d\n",c);
// }
int f(int x)
{
    printf("x is %d\n",x);
    return x;
}

main()
{
    if(f(0) || f(1))
    {
        printf("got it");
    }
}