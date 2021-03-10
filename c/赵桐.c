#include <stdio.h>
#include <process.h>
#include <windows.h>
#include <conio.h>
#include <time.h>
#include <stdlib.h>

#define WIDTH 100
#define HEIGH 80

enum direction{

    LEFT,
    RIGHT,
    UP,
    DOWN

};

struct Food{

    int x;
    int y;

};

struct Node{

    int x;
    int y;
    struct Node *next;

};

struct Snake{

    int lenth;
    enum direction dir;

};

struct Food *food; 
struct Snake *snake;
struct Node *snode,*tail;
int SPEECH=200;
int score=2017;
int smark=0;
int times=0;
int STOP=0;

void Initfood();
void Initsnake();
void Eatfood();
void Addnode(int x, int y);
void display(struct Node *shead);
void move();
void draw();
void Homepage();
void keybordhit();
void Addtail();

void gotoxy(int x, int y)
{
    COORD pos;
    pos.X = x - 1;
    pos.Y = y - 1;
    SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE),pos);
}

void Initsnake()
{
    int i;

    snake=(struct Snake*)malloc(sizeof(struct Snake));
    tail=(struct Node*)malloc(sizeof(struct Node));
    food = (struct Food*)malloc(sizeof(struct Food));
    snake->lenth=1;
    snake->dir=RIGHT;

    for(i=2;i<=snake->lenth+2;i++)
    {
        Addnode(i,2);
    }
}

void Initfood()
{
    struct Node *p=snode;
    int mark=2;
    srand((unsigned)time(NULL));

    while(1)
    {
        food->x=rand()%(WIDTH-2)+2;
        food->y=rand()%(HEIGH-2)+2;

        while(p!=NULL)
        {
            if((food->x==p->x)&&(food->y==p->y))
            {
                mark=0;
                break;
            }

        p=p->next;

        }

        if(mark==1)
        {
            gotoxy(food->x,food->y);
            printf("%c",3);
            break;
        }

        mark=1;
        p=snode;

        }
    }

void move()
{
    struct Node *q, *p=snode;

    if(snake->dir==RIGHT)
    {
        Addnode(p->x+1,p->y);
        if(smark==0)
        {
            while(p->next!=NULL)
            {
                q=p;
                p=p->next;
            }

            q->next=NULL;
            free(p);

        }
    }

    if(snake->dir==LEFT)
    {
        Addnode(p->x-1,p->y);
        if(smark==0)
        {
            while(p->next!=NULL)
            {
                q=p;
                p=p->next;
            }

            q->next=NULL;
            free(p);
        }
    }

    if(snake->dir==UP)
    {
        Addnode(p->x,p->y-1);

        if(smark==0)
        {
            while(p->next!=NULL)
            {
                q=p;
                p=p->next;
            }

            q->next=NULL;
            free(p);

        }
    }

    if(snake->dir==DOWN)
    {
        Addnode(p->x,p->y+1);
        if(smark==0)
        {
            while(p->next!=NULL)
            {
                q=p;
                p=p->next;
            }

            q->next=NULL;
            free(p);
        }
    }
}

void Addnode(int x, int y)
{
    struct Node *newnode=(struct Node *)malloc(sizeof(struct Node));
    struct Node *p=snode;

    newnode->next=snode;
    newnode->x=x;
    newnode->y=y;
    snode=newnode;

    if(x<2||x>=WIDTH||y<2||y>=HEIGH)
    {
        STOP=1;
        gotoxy(10,19);
        printf("GameOver! Press any button quit\n");
        _getch();
        free(snode);
        free(snake);
        exit(0);
    }

    while(p!=NULL)
    {
        if(p->next!=NULL)
        if((p->x==x)&&(p->y==y))
        {
            STOP=1;
            gotoxy(10,19);
            printf("撞到自身,游戏结束,任意键退出!\n");
            _getch();
            free(snode);
            free(snake);
            exit(0);
        }

        p=p->next;
    }
}

void Eatfood()
{
    Addtail();
    score++;
}

void Addtail()
{
    struct Node *newnode=(struct Node *)malloc(sizeof(struct Node));
    struct Node *p=snode;

    tail->next=newnode;
    newnode->x=50;
    newnode->y=20;
    newnode->next=NULL;
    tail=newnode;
}

void draw()
{
    struct Node *p=snode;
    int i,j;

    while(p!=NULL)
    {
        gotoxy(p->x,p->y);
        printf("%c",2);
        tail=p;
        p=p->next;
    }

    if(snode->x==food->x&&snode->y==food->y)
    {
        smark=1;
        Eatfood();
        Initfood();
    }

    if(smark==0)
    {
        gotoxy(tail->x,tail->y);
        printf("%c",' ');
    }

    else
    {
        times=1;
    }

    if((smark==1)&&(times==1))
    {
        gotoxy(tail->x,tail->y);
        printf("%c",' ');
        smark=0;
    }

    gotoxy(50,12);
    printf("Food: %d,%d",food->x,food->y);

    gotoxy(50,5);
    printf("Scores: %d",score);

    gotoxy(50,7);
    printf("Speed: %d",SPEECH);

    gotoxy(15,14);
    printf("Press 'y' speed up");

    gotoxy(15,15);
    printf("Press 'n' speed down");

    gotoxy(15,16);
    printf("Press 'blank bar' pass");
}

void HideCursor()
{
    CONSOLE_CURSOR_INFO cursor_info = {1, 0};
    SetConsoleCursorInfo(GetStdHandle(STD_OUTPUT_HANDLE), &cursor_info);
}

void Homepage()
{
    int x,y;
    HideCursor();
    printf("----------------------------------------\n");
    printf("|\t\t\t\t       |\n");
    printf("|\t\t\t\t       |\n");
    printf("|\t\t\t\t       |\n");
    printf("|\t\t\t\t       |\n");
    printf("|\t\t\t\t       |\n");
    printf("|\t\t\t\t       |\n");
    printf("|\t\t\t\t       |\n");
    printf("|\t\t\t\t       |\n");
    printf("|\t\t\t\t       |\n");
    printf("|\t\t\t\t       |\n");
    printf("----------------------------------------\n");
    gotoxy(5,30);
    printf("Press any key to start, W.A.S.D to control forward");

    _getch();
    Initsnake();
    Initfood();

    gotoxy(5,13);
    printf("                                ");
}

void keybordhit()
{
    char ch;
    if(_kbhit())
    {
        ch=getch();
        switch(ch)
        {
            case 'W':
            case 'w':if(snake->dir==DOWN)
                    {
                        break;
                    }
                    else
                    snake->dir=UP;break;

            case 'A':
            case 'a':if(snake->dir==RIGHT)
                    {
                        break;
                    }
                    else
                    snake->dir=LEFT;break;

            case 'S':
            case 's':if(snake->dir==UP)
                    {
                        break;
                    }
                    else
                    snake->dir=DOWN;break;

            case 'D':
            case 'd':if(snake->dir==LEFT)
                    {
                        break;
                    }
                    else
                    snake->dir=RIGHT;break;

            case 'Y':
            case 'y':
                    if(SPEECH>=150)
                    {
                        SPEECH=SPEECH-50;
                    }
                        break;
            case 'N':
            case 'n':
                    if(SPEECH<=400)
                    {
                        SPEECH=SPEECH+50;
                    }
                        break;

            case ' ':
                    gotoxy(15,18);
                    printf("Game passed,press any key to continue");
                    system("pause>nul");
                    gotoxy(15,18);
                    printf("                           ");
                        break;

            default:break;
        }
    }
}

int main(void)
{
    Homepage();
    while(!STOP)
    {
        keybordhit();
        move();
        draw();
        Sleep(SPEECH);
    }

    return 0;
}