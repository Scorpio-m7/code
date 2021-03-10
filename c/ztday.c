#include <stdio.h>
int main(void)
{
	int yue [13]={0,31,28,31,30,31,30,31,31,30,31,30,31};
	int y,m,d,i=0,sum=0 ;
	for(;;)
	{
	scanf("%d%d%d",&y,&m,&d);
	if((y>1000)&&(y<9999)&&(m>=1)&&(m<=12)&&(d>=1)&&(d<=31))
	{
	if(y%4==0&&y%100!=0||y%400==0)
		yue [2]=29;
	else 
		yue [2]=28;
		if(d<=yue[m])
		break;
	}
	}
	do 
	{
		sum=sum+yue [i];
		i++;
	}while (i<m);
	printf("%d年%d月%d日时该年的第%d天",y,m,d,sum+d);

}