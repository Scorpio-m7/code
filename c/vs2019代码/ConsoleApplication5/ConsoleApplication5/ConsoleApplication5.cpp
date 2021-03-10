// ConsoleApplication5.cpp : 此文件包含 "main" 函数。程序执行将在此处开始并结束。
//

#include<stdio.h>
#include<windows.h>

EXCEPTION_DISPOSITION __cdecl _except_handler(struct _EXCEPTION_RECORD* _ExceptionRecord, void* _EstablisherFrame, struct _CONTEXT* _ContextRecord, void* _DispatcherContext)
{
	printf("Exception Handled\n");
	printf("%x %x\n", _ExceptionRecord->ExceptionAddress, _ContextRecord->Eip);
	_ContextRecord->Eip += 3;
	return ExceptionContinueExecution;
}
int main()
{
	__asm
	{
		push _except_handler
		push FS : [0] //SEH链表的表头
		mov FS : [0] , ESP
	}
	getchar();
	int a = 0;
	int b = 5;
	int c = b / a;
	__asm
	{
		MOV EAX, [ESP]
		MOV FS : [0] , EAX
		ADD ESP, 8
	}
	getchar();
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
