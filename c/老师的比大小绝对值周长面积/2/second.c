#include "second.h"


//	second.c --> second.h ---> stdio.h

//float pi = 3.141592;	����һ��float���͵ı��� 
#define PI 3.141592	//�궨�� PI 
void circle(float r)
{
	float c;
	c = 2*r*PI;
	printf("Բ���ܳ�Ϊ%f",c); 
}

void area(float r)
{
	float a;
	a = r*r*PI;
	printf("Բ�����Ϊ%f",a);
}

