#include <stdio.h>
#include <malloc.h>
#include <stdlib.h>
#include <string.h>
#define STACK_INT_SIZE 100
#define STACKINCREMENT 10
typedef struct
{
	int *base;
	int *top;
	int stacksize;
}sqStack;

void InitStack(sqStack *s)
{
	s->base = (int *)malloc(STACK_INT_SIZE * sizeof(int));
	if(!s->base)
	{
		exit(1);
	}
	s->top = s->base;
	s->stacksize = STACK_INT_SIZE;
}

void Push(sqStack *s,int e)
{
	if(s->top - s->base >= s->stacksize)
	{
		s->base = (int *)realloc(s->base,(s->stacksize + STACKINCREMENT) * sizeof(int));
		if(!s->base)
		{
			exit(1);
		}
		s->top = s->base + s->stacksize;
		s->stacksize += STACKINCREMENT;
	}
	*(s->top) = e;
	s->top++;
}

void Pop(sqStack *s,char *e)
{
	if(s->top == s->base)
		exit(1);
	*e = *(--(s->top));
}

char GetTop(sqStack *s)
{
	if(s->top == s->base)
	{
		return -1;
	}
	return *(s->top - 1);
}

int In(char e)
{
	if(e == '+'||e == '*'||e == '-'||e == '/'||e == '('||e == ')'||e == '#')
		return 1;
	else
		return 0;
}

char Precede(char a,char b)
{
	char f;
	if(a == '+'||a == '-')
	{
		if(b == '+'||b == '-'||b == ')'||b == '#')
			f = '>';
		else if(b == '*'||b == '/'||b == '(')
			f = '<';
	}
	else if(a == '*'||a == '/')
	{
		if(b == '+'||b == '-'||b == '*'||b == '/'||b == ')'||b == '#')
			f = '>';
		else if(b == '(')
			f = '<';
	}
	else if(a == '(')
	{
		if(b == '+'||b == '-'||b == '*'||b == '/'||b == '(')
			f = '<';
		else if(b == ')')
			f = '=';
	}
	else if(a == ')')
	{
		if(b == '+'||b == '-'||b == '*'||b == '/'||b == ')'||b == '#')
			f = '>';
	}
	else if(a == '#')
	{
		if(b == '+'||b == '-'||b == '*'||b == '/'||b == '(')
			f = '<';
		else if(b == '#')
			f = '=';
	}
	return f;
}

char Operate(char a,char theta,char b)
{
	char c;
	a = a - '0';
	b = b - '0';
	if(theta == '+')
		c = a+b+'0';
	else if(theta == '-')
		c = a-b+'0';
	else if(theta == '*')
		c = a*b+'0';
	else if(theta == '/')
		c = a/b+'0';
	return c;
}

int EvaluateExpression()
{
	sqStack OPND,OPTR;
	char ch,a,b,theta,x;
	InitStack(&OPND);
	InitStack(&OPTR);
	Push(&OPTR,'#');
	ch = getchar();
	while(ch != '#'||GetTop(&OPTR)!= '#')
	{
		if(!In(ch))
		{
			Push(&OPND,ch);
			ch = getchar();
		}
		else
		{
			switch(Precede(GetTop(&OPTR),ch))
			{
			case '<':
				Push(&OPTR,ch);
				ch = getchar();
				break;
			case '>':
				Pop(&OPTR,&theta);
				Pop(&OPND,&b);
				Pop(&OPND,&a);
				Push(&OPND,Operate(a,theta,b));
				break;
			case '=':
				Pop(&OPTR,&x);
				ch = getchar();
				break;
			}
		}
	}
	return GetTop(&OPND)-'0';
}

void main()
{
	printf("请输入算术表达式，以#结束\n");
	printf("例如\t 1*(2-1)#\t\n");
	printf("结果是:%d\n",EvaluateExpression());
}
