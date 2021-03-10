#include <iostream.h>
int he(int x,int y){
	return x+y;
}
/*void mian(){
	int a,b,*sum;
	cin>>a>>b;
	sum=&he(a,b);
	cout<<*sum;
}*/
void mian(){
	int i,a[10],*p;
	for(i=1;i<=10;i++){
		cin>>a[i];
		p=&a[i];
		cout<<*p;
	}
}
