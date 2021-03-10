#include <stdio.h>
#define MAXSIZE 12500
typedef struct
{
    int i,j;
    int e;
}triple;
typedef struct
{
    triple data[MAXSIZE+1];
    int mu,nu,tu;
}tsmatrix;
createsmatrix(tsmatrix *m)
{
    int i,a,n,e,k;
    printf("行数，列数，非零个数，逗号分开");
    scanf("%d,%d,%d",&(*m).mu,&(*m).nu,&(*m).tu);
    (*m).data[0].i=0;
    printf("\n");
    for(i=1;i<=(*m).tu;i++)
    {
        do
        {
            printf("输入第%d个非零元素所在行(1~%d)列(1~%d)值以及该数值：",i,(*m).mu,(*m).nu);
            scanf("%d,%d,%d",&a,&n,&e);
            k=0;
            if(a<1||a>(*m).mu||n<1||n>(*m).nu)
                k=1;
            if(a<(*m).data[i-1].i||a==(*m).data[i-1].i&&n<(*m).data[i-1].j)
                k=1;
        }
        while(k);
        (*m).data[i].i=a;
        (*m).data[i].j=n;
        (*m).data[i].e=e;
    }
    printf("\n");
    return 1;
}
void printsmatrix(tsmatrix m)
{
    int i;
    printf("****************************\n");
    for(i=1;i<=m.tu;i++)
        printf("%2d%4d%8d\n",m.data[i].i,m.data[i].j,m.data[i].e);
    printf("****************************\n");
    printf("\n");
}
void transposesmatrix(tsmatrix m,tsmatrix *t)
{
    int q,p,col;
    (*t).mu=m.nu;
    (*t).nu=m.mu;
    (*t).tu=m.tu;
    if((*t).tu)
    {
        q=1;
        for(col=1;col<=m.nu;++col)
            for(p=1;p<=m.tu;++p)
            if(m.data[p].j==col)
            {
                (*t).data[q].i=m.data[p].j;
                (*t).data[q].j=m.data[p].i;
                (*t).data[q].e=m.data[p].e;
                ++q;
            }
    }
}
void print(tsmatrix a)
{
    int k=1,m,b;
    int M[MAXSIZE][MAXSIZE];
    printf("非零元素对应的位置：\n");
    printf("****************************\n");
    for(m=0;m<a.mu;m++)
    {
        for(b=0;b<a.nu;b++)
            M[m][b]=0;
    }
    while(k<=a.tu)
    {
        M[a.data[k].i-1][a.data[k].j-1]=a.data[k].e;
        k++;
    }
    for(m=0;m<a.mu;m++)
    {
        printf("|");
        for(b=0;b<a.nu;b++)
            printf("%d ",M[m][b]);
        printf("| \n");
    }
    printf("****************************\n");
    printf("\n");
}
int main()
{
    tsmatrix m,t;
    createsmatrix(&m);
    printf("三元组表为：\n");
    printsmatrix(m);
    print(m);
    transposesmatrix(m,&t);
    printf("转置矩阵三元组表为\n");
    printsmatrix(t);
    print(t);
    getchar();
}
