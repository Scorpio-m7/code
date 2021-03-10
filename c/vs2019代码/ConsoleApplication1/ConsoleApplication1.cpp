// ConsoleApplication1.cpp : 此文件包含 "main" 函数。程序执行将在此处开始并结束。
//
#include <string.h>
#include <windows.h>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	/*unsigned short a = 0x8003;
	char ch1[40] = { 0 };
	a >>= 2;
	_itoa(a, ch1, 2);
	printf("%X\n", a);
	printf("%s\n", ch1);
	int b = 10;
	printf("%d\n", b >> 2);
	int choice = 0;
	printf("pick a number vetween 1 and 10 and you may win a prize!");
	scanf("%d", &choice);
	if ((choice > 10) || (choice < 1))
		choice = 11;
	switch (choice)
	{
	case 7:
		printf("book");
		break;
	case 2:
		printf("you win the pen!");
		break;
	case 8:
		printf("tables");
		break;
	case 11:
		printf("try again");
	default:
		printf("sorry");
		break;
	}*/
	char str[0x30] = "欢迎学习逆向工程";
	DWORD key = 0;
	printf("加密的字符串是：\n\t%s\n\n，输入1-255之间的一个整数作为加密密钥", str);
	while (true)
	{
		scanf_s("%d", &key);
		if (key<0||key>255)
		{
			printf("输入有误");
		}
		else {
			break;
		}
	}
	DWORD len = strnlen_s(str, sizeof(str));
	for (int i = 0; i < len; ++i)
	{
		str[i] ^= (key & 0xff);
	}
	char path[16] = ".\\1.txt";
	HANDLE hfile = CreateFileA(path, GENERIC_READ | GENERIC_WRITE, FILE_SHARE_READ, NULL, CREATE_NEW, FILE_ATTRIBUTE_NORMAL, NULL);
	if (hfile==INVALID_HANDLE_VALUE)
	{
		printf("文件创建失败\n");
		system("pause");
		CloseHandle(hfile);
		return 0;
	}
	WriteFile(hfile, str, len + 1, &len, NULL);
	printf("加密完成");
	CloseHandle(hfile);
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
//   6. 将来，若要再次打开此项目，请转到“文件”>“打开”>“项目”并选择 .sln 文
