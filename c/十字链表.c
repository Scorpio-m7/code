#include <stdio.h>
#include <stdlib.h>
#define MXASIZE 1000
typedef struct clist_node
{
    int row,col;
    int e;
    struct clist_node *right;
    struct clist_node *down;
}clistnode;
typedef struct clist
{
    int m,n,length;
    clistnode **row_head;
    clistnode **col_head;
}clist;
void creat_croosslist(clist *M)
{
    int i,j,len,e;
    clistnode *s;
    clistnode *temp;
    clistnode *pre;
    scanf("%d %d %d",&i,&j,&len);
    getchar();
    M->m=i;
    M->n=j;
    M->length=len;
    M->row_head=(clistnode **)malloc((MXASIZE+1) * sizeof(clistnode *));
    M->col_head=(clistnode **)malloc((MXASIZE+1) * sizeof(clistnode *));
    for(i=0;i<MXASIZE+1;i++)
    {
        M->row_head[i]=(clistnode *)malloc(sizeof(clistnode));
        M->col_head[i]=(clistnode *)malloc(sizeof(clistnode));
        M->col_head[i]->down=NULL;
        M->row_head[i]->right=NULL;
    }
    while(1)
    {
        scanf("%d %d %d",&i,&j,&e);
        getchar();
        if(i==0)
            break;
        else{
            s=(clistnode *)malloc(sizeof(clistnode));
            s->e=e;
            s->row=i;
            s->col=j;
            s->right=NULL;
            s->down=NULL;
            if(M->row_head[i]->right==NULL)
            {
                M->row_head[i]->right=s;
            }
            else{
                pre=M->row_head[i];
                temp=M->row_head[i]->right;
                while(temp->right!=NULL&&temp->col<j)
                {
                    pre=temp;
                    temp=temp->right;
                }
                if(temp->col<=j)
                    temp->right=s;
                else{
                    pre->right=s;
                    s->right=temp;
                }
            }
            if(M->col_head[i]->down==NULL){
                M->col_head[i]->down=s;
                }else{
                    pre=M->col_head[i];
                    temp=M->col_head[i]->down;
                    while(temp->down!=NULL&&temp->col<j){
                        pre=temp;
                        temp=temp->down;
                    }
                    if(temp->col<=j)
                        temp->down=s;
                    else{
                        pre->down=s;
                        s->down=temp;
                }
            }
        }
    }
}
mian()
{
}
