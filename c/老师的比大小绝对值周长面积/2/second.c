#include "second.h"


//	second.c --> second.h ---> stdio.h

//float pi = 3.141592;	声明一个float类型的变量 
#define PI 3.141592	//宏定义 PI 
void circle(float r)
{
	float c;
	c = 2*r*PI;
	printf("圆的周长为%f",c); 
}

void area(float r)
{
	float a;
	a = r*r*PI;
	printf("圆的面积为%f",a);
}

