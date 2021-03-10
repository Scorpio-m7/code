
// C与C陷阱  C语言编程自身含有的缺陷
//怎么把账户存储下来
//内存里面的链表数据 存储到硬盘 以文件的形式存储
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

struct student *head = NULL;	//存储链表表头的数据
struct student *p1 = NULL;		//当前节点的地址
struct student *p2 = NULL;		//上一个节点的地址  node

void node_create(void);	
void node_show(void);
void node_check(void);	//查询节点
void node_change(void);	//修改指定节点数据
void node_delete(void);
void node_write(void);	//将链表写入到文本中
struct student * node_read(void);	//将文本中的数据加载到内存中

int main()
{
	char i=0;
    head = node_read();
    for(;;)	//无限循环
    {
		printf("1:创建学生账户信息	2：查询所有学生信息	3:查询指定学生信息  4: 修改指定节点数据  5:删除指定节点		6：保存退出\n");
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
void node_create(void)	//每执行一次就创建一个节点
{
	p1 = (struct student *)malloc(sizeof(struct student));		//申请内存空间
    if(p1 ==NULL)//内存申请失败
    {
		printf("内存申请失败\n");
    }
    else	//内存申请成功
    {
		if(head ==NULL)	//申请第一个节点
        {
			head = p1;
            p2 = p1;	//为下次做准备
            p1->next = NULL;
        }
        else	//申请第二个以上的节点
        {
			p2->next =p1;	//将 当前节点的地址存储在上一个节点里面的next
            p1->next =NULL;	//最新节点后面没有节点，所以用NULL 填充
            p2 = p1;		//形成迭代，为下次做准备
        }
        memset(p1->name , 0 ,20);	//内存初始化  初始化为0
        printf("请输入学生的名字\n");
        scanf("%s",p1->name);
        printf("请输入学生的年龄\n");
        scanf("%d",&p1->age);
        memset(p1->tel , 0 ,12);	//内存初始化  初始化为0
        printf("请输入学生的电话号\n");
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
		printf("%d学生名字为:%s\n",i,lp->name);
        printf(" 学生的年龄为:%d\n",lp->age);
        printf(" 学生的电话号为:%s\n",lp->tel);
        i++;
        lp = lp->next;
    }
}

void node_check(void)
{
	struct student *lp=NULL;
    char name[20];
    lp = head;
	printf("请输入需要查询的学生名字\n");
    memset(name , 0 ,20);	//内存初始化
    scanf("%s",name);
    
    while(lp !=NULL)
    {
		if(strcmp(name , lp->name) == 0)	//成立的话 表示相同
        {
			printf("学生名字为:%s\n",lp->name);
            printf("学生年龄为:%d\n",lp->age);
            printf("学生电话号为:%s\n",lp->tel);
        }
        lp = lp->next;
    } 
}

void node_delete(void)
{
	struct student *lp1 = NULL;		//存储当前节点地址
    struct student *lp = NULL;		//存储下一个节点地址
    struct student *lp2 = NULL;		//存储上一个节点地址
    char name[20];
    memset(name ,0 ,20);
    lp = head;
    printf("请输入需要删除的学生名字\n");
    scanf("%s",name);
    
    while(lp !=NULL)
    {
		lp1 = lp;	//当前节点
        lp = lp->next;	//下一个节点
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
    printf("请输入需要修改的名字\n");
    scanf("%s",name);
    
    while(lp !=NULL)
    {
		if(strcmp(name , lp->name) ==0)
        {
			printf("请输入需要修改的年龄\n");
            scanf("%d",&lp->age);	//写入4个字节数据 unsigned char
        }
        lp = lp->next;
    }
}

void node_write(void)
{
	FILE *fp;	//文件类型的指针
    struct student *lp;
    lp = head;
    
	if((fp = fopen("SYSTEM" , "w+")) ==NULL)	//以写的方式打开文件
    {
		printf("滚,不给你看\n");
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
		printf("去你大爷的\n");
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
