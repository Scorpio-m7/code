#include <stdio.h>
#include "second.c"
int main()
{
    float a,b,c;
    scanf("%f",&a);
	b=circle( a); 
	c=area(a);
	printf("%f\n%f\n",b,c);	
}
