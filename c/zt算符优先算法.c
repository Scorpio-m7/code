#define STACK_INIT_SIZE 100
#define STACKINCREMENT 10
#include <stdio.h>
#include <malloc.h>
#include <stdlib.h>
#include <string.h>
typedef struct {
int *base;
int *top;
int stacksize;
}optr;
void initstack(optr *s){
s->base=(int *)malloc(STACK_INIT_SIZE *sizeof(int));
if(!s->base)
return 0;
s->top=s->base;
s->stacksize=STACK_INIT_SIZE ;
return 1;
}
char gettop(optr *s,char *e){
if(s->top==s->base)
return 0;
e=*(s->top-1);
return 1;
}
void pop(optr *s,char *e){
if(s->top==s->base)
return 0;
*e=*(--s->top);
return 1;
}
void push(optr *s,int e){
if(s->top-s->base>=s->stacksize)
{
s->base=(char *)realloc(s->base,(s->stacksize+STACKINCREMENT)*sizeof(char));
if(!s->base)
return 0;
s->top=s->base+s->stacksize;
s->stacksize+=STACKINCREMENT;
}
*s->top++=e;
return 1;
}
int evaluate(){
    initstack(optr);
    push(optr,'#');
    initstack(opnd);
    c=getchar();
    while (c!='#'||gettop(optr)!='#')
    {
        if(!in(c,op))
        {
            push((opnd,c);c=getchar();
        }
        else
            switch(precede(gettop(optr),c))
        {
        case'<':
            push(optr,c);c=getchar();
            break;
        case'=':
            pop(optr,x);c=getchar;
            break;
        case'>':
            pop(optr,theta);
            pop(opnd,b);
            pop(opnd,a);
            push( opnd,operate(a,theta,b));
            break;
        }
    }
    return gettop(opnd);
}
void main(){
    char a,b,c;
    scanf("%c",a);
    evaluate(a,b,c)
}
