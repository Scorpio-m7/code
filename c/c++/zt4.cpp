#include <iostream.h>
class weight{
public:
	float height;
	int sex;
	double Weight;
public:
	void w(double x,int y);
};
void weight::w(double x,int y){
		if(y==1)
			cout<<(x-80)*0.7;
		else if(y==0)
			cout<<(x-70)*0.6;	
}
void main(){
	weight T;
	cout<<"输入性别（男性输入1，女性输入0）,请输入身高，"<<endl;
	cin>>T.sex>>T.height;
	T.w(T.height,T.sex);
	cout<<"kg"<<endl;
}