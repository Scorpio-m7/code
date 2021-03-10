#include <stdio.h>
int year,month,day,sum=0;
int month_day[13] = {0,31,28,31,30,31,30,31,31,30,31,30,31}; 
int main()
{
	int i=0;
	do
	{	
		printf("请输入有效年份 1000~9999\n");
		scanf("%d",&year);
	}while(!(year >=1000 && year<=9999));
	if((year %4==0 && year %100 !=0) || (year %400 == 0))
	{
		month_day[2] = 29;
//		printf("闰年");
	}
	else
	{
		month_day[2] = 28;
//		printf("平年"); 
	}
	do
	{
		printf("请输入有效月份 1~12\n");
		scanf("%d",&month);		
	}while(!(month>=1 && month<=12));
	do
	{
		printf("请输入有效日期 (注意每月的最大天数)\n");
		scanf("%d",&day);
	}while(!(day>=1 && day <=month_day[month]));
	for(i=1;i<month;i++)
	{
		sum  = sum + month_day[i];
	}
	sum = sum + day;
	printf("%d年%d月%d日是该年的第%d天\n",year,month,day,sum);
	return 0;		
} 
