#include <stdio.h>
int year,month,day,sum=0;
int month_day[13] = {0,31,28,31,30,31,30,31,31,30,31,30,31}; 
int main()
{
	int i=0;
	do
	{	
		printf("��������Ч��� 1000~9999\n");
		scanf("%d",&year);
	}while(!(year >=1000 && year<=9999));
	if((year %4==0 && year %100 !=0) || (year %400 == 0))
	{
		month_day[2] = 29;
//		printf("����");
	}
	else
	{
		month_day[2] = 28;
//		printf("ƽ��"); 
	}
	do
	{
		printf("��������Ч�·� 1~12\n");
		scanf("%d",&month);		
	}while(!(month>=1 && month<=12));
	do
	{
		printf("��������Ч���� (ע��ÿ�µ��������)\n");
		scanf("%d",&day);
	}while(!(day>=1 && day <=month_day[month]));
	for(i=1;i<month;i++)
	{
		sum  = sum + month_day[i];
	}
	sum = sum + day;
	printf("%d��%d��%d���Ǹ���ĵ�%d��\n",year,month,day,sum);
	return 0;		
} 
