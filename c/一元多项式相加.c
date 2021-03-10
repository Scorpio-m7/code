#include <stdio.h>
#include <malloc.h>
#include <stdlib.h>
#define LEN sizeof (node)
typedef struct polynode
{
    int a;
    int b;
    struct polynode *next;
}node;
node *create(viod)
{
    node *h,*r,*s;
    int c,e;
    h=(node *)malloc(LEN);
    r=h;
    scanf("%d",&c);
    scanf("%d",&e);
    while (c!=0)
    {
        s=(node *)malloc(LEN);
        s->a=c;
        s->b=e;
        r->next=s;
        r=s;
        scanf("%d",&c);
        scanf("%d",&e);
    }
    r->next=NULL;
    return(h);
}
void polyadd(node *polya,node *polyb)
{
    node *q,*p,*pre,*temp;
    int sum;
    p=polya->next;
    q=polyb->next;
    pre=polya;
    while (p!=NULL&&q!=NULL)
    {
        if(p->b<q->b)
        {
            pre->next=p;
            pre=pre->next;
            p=p->next;
        }
        else if(p->b==q->b)
        {
            sum=p->a+q->a;
            if(sum!=0)
            {
                p->a=sum;
                pre->next=p;
                pre=pre->next;
                p=p->next;
                temp=q;
                q=q->next;
                free(temp);
            }
            else
            {
                temp=p->next;
                free(p);
                p=temp;
                temp=q->next;
                free(q);
                q=temp;
            }
        }
        else
        {
            pre->next=q;
            pre=pre->next;
            q=q->next;
        }
    }
    if(p!=NULL)
        pre->next=p;
    else
        pre->next=q;
}
void print(node *p)
{
    while(p->next!=NULL)
    {
        p=p->next;
        printf("  %d*^x%d",p->a,p->b);
    }
}
main()
{
    node *polya,*polyb;
    polya=create();
    print(polya);
    polyb=create();
    polyadd(polya,polyb);
    print(polya);
}
