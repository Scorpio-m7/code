struct Stack{
    char * base;
    char * top;
    int staticsize;
};
char yxj[7][7]={{'>','>','<','<','<','>','>'},
                {'>','>','<','<','<','>','>'},
                {'>','>','>','>','<','>','>'},
                {'>','>','>','>','<','>','>'},
                {'<','<','<','<','<','=',' '},
                {'>','>','>','>','=','>','>'},
                {'<','<','<','<','<',' ','='}};
char ysf[7]={'+','-','*','/','(',')','#'};
int Init_Static(struct Stack * L){

    L->base=(char *)malloc(100*sizeof(char));
    if(!L->base)
        return 0;
    L->top = L->base;
    staticsize = 100;
}
int GetTop(struct Stack * L,char * c){

    if(L->base == L->top)
        return 0;
    *c = *(L->top-1);
    return 1;
}
int Push(struct Stack * L,char e){
    if(L->top-L->base>=L->stacksize)
        return 0;
    *L->top++ = e;
    return 1;
}
int Pop(struct Stack * L,char * e){
    if(L->top == L->base)
        return 0;
    *e = *(--L->top);
    return 1;

}
int In(char c){
    if(c>=48&&c<=57)
        return 0;
    else
        return 1;

}
char Precede(char c1,char c2){

    int i,j;
    for(i=0;i<7;i++)
        if(c1==ysf[i])
            break;
     for(j=0;j<7;j++)
        if(c2==ysf[j])
            break;

    return yxj[i][j];
}

