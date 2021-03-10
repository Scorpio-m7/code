// ConsoleApplication4.cpp : 此文件包含 "main" 函数。程序执行将在此处开始并结束。
//
#include <stdlib.h>
#include <windows.h>
#include <stdio.h>
using namespace std;
int add(int x,int y){
    return x+y;
}
int hook(int x,int y){
    x+=500;
    y+=500;
	printf("Programe has been hooked!\n");
	return x+y;
}
int main(){
    printf("abcdefg");
    char* fn=(char*)&add;
    char* d1=(char*)&hook;
    char* d2=(char*)&add;
    DWORD distance=d1-d2;
    DWORD ignore;
    VirtualProtect(fn,128,PAGE_EXECUTE_READWRITE,&ignore);
    *fn=0xE9;
    fn++;
    *(int*)fn=distance-5;
    //jmp指令占5个字节，除去jmp头0xE9，后四个字节是相对jmp指令下一条指令的地址相对偏移。*int会写入4个字节，以将覆盖原高字节硬编码使其置0
    //或者前面*fn=0xEB,0xEB对应的短跳转只能有一个节字偏移，那这里就可以用*fn=distance-5;了
    int a=5,b=5;
    while(1){
    	int ans=add(a,b);
    	printf("%d+%d=%d\n",a,b,ans);
    	Sleep(500);
    }
    return 0;  
}

// 运行程序: Ctrl + F5 或调试 >“开始执行(不调试)”菜单
// 调试程序: F5 或调试 >“开始调试”菜单

// 入门使用技巧: 
//   1. 使用解决方案资源管理器窗口添加/管理文件
//   2. 使用团队资源管理器窗口连接到源代码管理
//   3. 使用输出窗口查看生成输出和其他消息
//   4. 使用错误列表窗口查看错误
//   5. 转到“项目”>“添加新项”以创建新的代码文件，或转到“项目”>“添加现有项”以将现有代码文件添加到项目
//   6. 将来，若要再次打开此项目，请转到“文件”>“打开”>“项目”并选择 .sln 文件
