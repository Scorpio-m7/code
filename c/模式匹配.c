#include <stdio.h>
#include <string.h>
#include <malloc.h>

typedef struct Hstring
{
	char *ch;
	int length;
};

void Initstring(struct Hstring *s)
{
	s->ch = NULL;
	s->length = NULL;
}

void Assign(struct Hstring *s,char cstr[])
{
    int i;
	s->ch = (char *)malloc(sizeof(char));
	for(i = 0;cstr[i] != '\0';i++)
	{
		s->ch[i] = cstr[i];
	}
	s->length = i;
}

int Index(struct Hstring *s,struct Hstring *t,int pos)
{
	int i = pos;
	int j = 1;
	while(i < s->length&&j < t->length)
	{
		if(s->ch[i] == t->ch[j])
		{
			++i;
			++j;
		}
		else
		{
			i = i-j+1;
			j = 0;
		}
		if(j == t->length)
			return(i-j+1);
		else
			return 0;
	}
}

int main()
{
	struct Hstring s,t;
	int k = 0,pos = 3;
	printf("�������һ������\n");
	char str1[20];
	gets(str1);

	printf("������ڶ�������\n");
	char str2[20];
	gets(str2);

	Initstring(&s);
	Assign(&s,str1);

	Initstring(&t);
	Assign(&t,str2);

	k = Index(&s,&t,pos);
	printf("�Ӵ��������ϵ�λ�ã�\n");
	printf("%d\n",k);

	return 0;
}
