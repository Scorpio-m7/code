
// C��C����  C���Ա�������е�ȱ��
//��ô���˻��洢����
//�ڴ�������������� �洢��Ӳ�� ���ļ�����ʽ�洢
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct student
{
	char name[20];
    int age;
    char tel[12];
    struct student *next;
};

struct student *head = NULL;	//�洢�����ͷ������
struct student *p1 = NULL;		//��ǰ�ڵ�ĵ�ַ
struct student *p2 = NULL;		//��һ���ڵ�ĵ�ַ  node

void node_create(void);	
void node_show(void);
void node_check(void);	//��ѯ�ڵ�
void node_change(void);	//�޸�ָ���ڵ�����
void node_delete(void);
void node_write(void);	//������д�뵽�ı���
struct student * node_read(void);	//���ı��е����ݼ��ص��ڴ���

int main()
{
	char i=0;
    head = node_read();
    for(;;)	//����ѭ��
    {
		printf("1:����ѧ���˻���Ϣ	2����ѯ����ѧ����Ϣ	3:��ѯָ��ѧ����Ϣ  4: �޸�ָ���ڵ�����  5:ɾ��ָ���ڵ�		6�������˳�\n");
		printf("----------------------------------------------------\n");
        scanf("%d",&i);
        switch(i)
        {
			case 1:node_create();	break;
            case 2:node_show();		break;
            case 3:node_check();	break;
            case 4:node_change();	break;
            case 5:node_delete();	break;
            case 6:node_write();	return 0;	break;
        }
    }
}
//	O-----------O----------O-----------O----------O---------O
//	head
//	   									         			p1
//	            								  			p2
void node_create(void)	//ÿִ��һ�ξʹ���һ���ڵ�
{
	p1 = (struct student *)malloc(sizeof(struct student));		//�����ڴ�ռ�
    if(p1 ==NULL)//�ڴ�����ʧ��
    {
		printf("�ڴ�����ʧ��\n");
    }
    else	//�ڴ�����ɹ�
    {
		if(head ==NULL)	//�����һ���ڵ�
        {
			head = p1;
            p2 = p1;	//Ϊ�´���׼��
            p1->next = NULL;
        }
        else	//����ڶ������ϵĽڵ�
        {
			p2->next =p1;	//�� ��ǰ�ڵ�ĵ�ַ�洢����һ���ڵ������next
            p1->next =NULL;	//���½ڵ����û�нڵ㣬������NULL ���
            p2 = p1;		//�γɵ�����Ϊ�´���׼��
        }
        memset(p1->name , 0 ,20);	//�ڴ��ʼ��  ��ʼ��Ϊ0
        printf("������ѧ��������\n");
        scanf("%s",p1->name);
        printf("������ѧ��������\n");
        scanf("%d",&p1->age);
        memset(p1->tel , 0 ,12);	//�ڴ��ʼ��  ��ʼ��Ϊ0
        printf("������ѧ���ĵ绰��\n");
        scanf("%s",p1->tel);
    }
}

void node_show(void)
{
	struct student *lp;
    int i=1;
    lp = head;
	while(lp != NULL)
    {
		printf("%dѧ������Ϊ:%s\n",i,lp->name);
        printf(" ѧ��������Ϊ:%d\n",lp->age);
        printf(" ѧ���ĵ绰��Ϊ:%s\n",lp->tel);
        i++;
        lp = lp->next;
    }
}

void node_check(void)
{
	struct student *lp=NULL;
    char name[20];
    lp = head;
	printf("��������Ҫ��ѯ��ѧ������\n");
    memset(name , 0 ,20);	//�ڴ��ʼ��
    scanf("%s",name);
    
    while(lp !=NULL)
    {
		if(strcmp(name , lp->name) == 0)	//�����Ļ� ��ʾ��ͬ
        {
			printf("ѧ������Ϊ:%s\n",lp->name);
            printf("ѧ������Ϊ:%d\n",lp->age);
            printf("ѧ���绰��Ϊ:%s\n",lp->tel);
        }
        lp = lp->next;
    } 
}

void node_delete(void)
{
	struct student *lp1 = NULL;		//�洢��ǰ�ڵ��ַ
    struct student *lp = NULL;		//�洢��һ���ڵ��ַ
    struct student *lp2 = NULL;		//�洢��һ���ڵ��ַ
    char name[20];
    memset(name ,0 ,20);
    lp = head;
    printf("��������Ҫɾ����ѧ������\n");
    scanf("%s",name);
    
    while(lp !=NULL)
    {
		lp1 = lp;	//��ǰ�ڵ�
        lp = lp->next;	//��һ���ڵ�
        if(strcmp(lp1->name ,name)==0)
        {
			if(lp1 == head)
            {
				head = lp1->next;
                free(lp1);
            }
            else if(lp1->next ==NULL)
            {
				lp2->next = NULL;
                p2 = lp2;
                free(lp1);
            }
            else
            {
				lp2->next = lp;
                free(lp1);
            }
        }
        lp2 = lp1;
    }
}

void node_change(void)
{
	struct student *lp;
    char name[20];
    memset(name ,0 ,20);
    lp = head;
    printf("��������Ҫ�޸ĵ�����\n");
    scanf("%s",name);
    
    while(lp !=NULL)
    {
		if(strcmp(name , lp->name) ==0)
        {
			printf("��������Ҫ�޸ĵ�����\n");
            scanf("%d",&lp->age);	//д��4���ֽ����� unsigned char
        }
        lp = lp->next;
    }
}

void node_write(void)
{
	FILE *fp;	//�ļ����͵�ָ��
    struct student *lp;
    lp = head;
    
	if((fp = fopen("SYSTEM" , "w+")) ==NULL)	//��д�ķ�ʽ���ļ�
    {
		printf("��,�����㿴\n");
    }
    else
    {
		while(lp!=NULL)
        {
			fwrite(lp->name , sizeof(lp->name) , 1 , fp);
            fwrite(&lp->age , sizeof(lp->age) , 1 ,fp);
            fwrite(lp->tel , sizeof(lp->tel) , 1 ,fp);
            lp=lp->next;
        }
        fclose(fp);
    }
}

struct student * node_read(void)
{
	FILE *fp;
    struct student *phead;
    int i=1;
    p1 = (struct student *)malloc(sizeof(struct student));
    if((fp = fopen("SYSTEM" , "r+"))==NULL)
    {
		printf("ȥ���ү��\n");
    }
    else
    {
		i=fread(p1->name , sizeof(p1->name) , 1 ,fp);
        i=fread(&p1->age , sizeof(p1->age) , 1 , fp);
        i=fread(p1->tel , sizeof(p1->tel) , 1 , fp);
        if(i==0)
        {
			free(p1);
            return NULL;
        }
        else
        {
			phead = p1;
            p1->next = NULL;
            p2 = p1;
        }
        while(1)
        {
			p1 = (struct student *)malloc(sizeof(struct student));
			i=fread(p1->name , sizeof(p1->name) , 1 ,fp);
			i=fread(&p1->age , sizeof(p1->age) , 1 , fp);
			i=fread(p1->tel , sizeof(p1->tel) , 1 , fp);           
            
            if(i==0)
            {
				fclose(fp);
                return phead;
            }
            else
            {
				p2->next = p1;
                p1->next = NULL;
                p2 = p1;
            }
        }
    }
}
