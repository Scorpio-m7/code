#include <stdio.h>
#include "first.h"
#include "second.h"


int main()
{
	int a,b,c;
	float r;
	printf("������������Ҫ�Ƚϵ�ֵ, a,b\n");
	scanf("%d,%d",&a,&b);		//20,18
	c = my_max(a,b);
	printf("���нϴ�ֵΪ%d\n",c);

	printf("�����������ֵ,\n");
	scanf("%d",&c);
	c = my_abs(c);
	printf("����ֵΪ%d\n",c);

	printf("����������Բ�İ뾶\n");
	scanf("%f",&r);
	circle(r); 
	area(r);

	return 0;
} 



