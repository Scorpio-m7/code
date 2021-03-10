#include <iostream.h>
void main()
{
	int a[10],sum=0,ave=0,t,max,min;
	cout<<"请输入十个数组值：";
	for(int x=1;x<=10;x++)
	{
		cin>>a[x];
		sum+=a[x];
	}
	max=a[1];min=a[1];
		for(int i=2;i<=10;i++){
			if(a[i]>max)
			{
				max=a[i];
			}
			else if(a[i]<min){
				min=a[i];
			}
		}
	ave=(sum-max-min)/8;
	cout<<"最小值为："<<min<<endl;
	cout<<"最大值为："<<max<<endl;
	cout<<"平均值为："<<ave<<endl;
}