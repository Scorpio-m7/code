#include <stdio.h>
#include "first.h"
#include "second.h"


int main()
{
	int a,b,c;
	float r;
	printf("请输入两个需要比较的值, a,b\n");
	scanf("%d,%d",&a,&b);		//20,18
	c = my_max(a,b);
	printf("其中较大值为%d\n",c);

	printf("请输入求绝对值,\n");
	scanf("%d",&c);
	c = my_abs(c);
	printf("绝对值为%d\n",c);

	printf("请输入所求圆的半径\n");
	scanf("%f",&r);
	circle(r); 
	area(r);

	return 0;
} 



