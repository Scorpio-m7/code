#include <iostream.h>
 void main(){
	int a;
	cin>>a;
	if(a>=90&&a<100)
		cout<<"优秀";
	else if(a>=80&&a<90)
		cout<<"良好";
	else if(a>=70&&a<80)
		cout<<"中等";
	else if(a>=60&&a<70)
		cout<<"及格";
	else cout<<"不及格";


	int q,w,e;
	cin>>q>>w>>e;
	if(q>w)
	{
		if(q>e)
		{
			if(w>e)
				cout<<q<<endl<<w<<endl<<e;
			else if(e>w)
				cout<<q<<endl<<e<<endl<<w;
		}
		else if(e>q)
			cout<<e<<endl<<q<<endl<<w;
	}
	else if(w>q)
	{
		if(w>e)
		{
			if(q>e)
				cout<<w<<endl<<q<<endl<<e;
			else if(e>q)
				cout<<w<<endl<<e<<endl<<q;
		}
		else if(e>w)
			cout<<e<<endl<<w<<endl<<q;
	}

 
	int r;
	cin>>r;
	switch(r/10){
		case 9:	cout<<"优秀";break;
		case 8:	cout<<"良好";break;
		case 7:	cout<<"中等";break;
		case 6:	cout<<"及格";break;
		default:	cout<<"不及格";
	}


	int g,i;
	cin>>g;
	for(i=1;i<=g;i++)
	{
		sum=sum+i*i;
	}
	cout<<sum;
	
	int s;
	cin>>s;
	if(s%2==0)
	cout<<"偶数";
	else
	cout<<"奇数";
}