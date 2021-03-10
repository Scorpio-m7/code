import pygame
import sys
import traceback
from pygame.locals import *
from random import *
class Ball(pygame.sprite.Sprite):#继承精灵
    def __init__(self,grayball_image,greenball_image,position,speed,bg_size,target):
        pygame.sprite.Sprite.__init__(self)#初始化动画精灵
        self.grayball_image=pygame.image.load(grayball_image).convert_alpha()#通过阿尔法通道添加图片
        self.greenball_image=pygame.image.load(greenball_image).convert_alpha()
        self.rect=self.grayball_image.get_rect()#获得球的尺寸
        self.rect.left,self.rect.top=position#小球放在指定位置
        self.side=[choice([-1,1]),choice([-1,1])]#随机的方向
        self.speed=speed
        self.collide=False#碰撞标记
        self.target=target
        self.control=False#控制标记
        self.width,self.height=bg_size[0],bg_size[1]#获得宽高
        self.radius=self.rect.width/2#小球半径
    def move(self):
        if self.control:#如果玩家控制,小球速度带方向
            self.rect=self.rect.move(self.speed)
        else:#如果非玩家控制,小球速度与方向分离
            self.rect=self.rect.move(self.side[0]*self.speed[0],self.side[1]*self.speed[1])#方向*速度
        if self.rect.right<=0:#如果从左面移出去
            self.rect.left=self.width#从右边进入
        elif self.rect.left>=self.width:#右出左进
            self.rect.right=0
        elif self.rect.bottom<=0:#上出下进
            self.rect.top=self.height
        elif self.rect.top>=self.height:#下出上进
            self.rect.bottom=0
    def check(self,motion):
        if self.target<motion<self.target+5:
            return True
class Glass(pygame.sprite.Sprite):
    def __init__(self,glass_image,mouse_image,bg_size):
        pygame.sprite.Sprite.__init__(self)#初始化动画精灵
        self.glass_image=pygame.image.load(glass_image).convert_alpha()#加载图片
        self.glass_rect=self.glass_image.get_rect()#获得矩形位置
        self.glass_rect.left,self.glass_rect.top=(bg_size[0]-self.glass_rect.width)//2,bg_size[1]-self.glass_rect.height#背景宽-glass宽/2,背景高-glass高
        self.mouse_image=pygame.image.load(mouse_image).convert_alpha()#加载图片
        self.mouse_rect=self.mouse_image.get_rect()#获得矩形位置
        self.mouse_rect.left,self.mouse_rect.top=self.glass_rect.left,self.glass_rect.top#设置鼠标左上角
        pygame.mouse.set_visible(False)#设置鼠标不可见
def main():
    pygame.init()
    grayball_image="ball.png"#图片名称
    greenball_image="green_ball.png"
    glass_image="glass.png"
    mouse_image="hand.png"
    bg_image="background.png"
    running=True
    pygame.mixer.music.load("bg_music.ogg")#添加背景音乐
    pygame.mixer.music.play()#播放
    loser_sound=pygame.mixer.Sound("cat.wav")#添加音效
    GAMEOVER=USEREVENT#创建事件
    pygame.mixer.music.set_endevent(GAMEOVER)#背景音乐结束时
    bg_size=width,height=1024,511#画布大小
    screen=pygame.display.set_mode(bg_size)#显示画布
    pygame.display.set_caption("play the ball")
    background=pygame.image.load(bg_image).convert_alpha()#载入图片
    hole = [(150, 160, 220, 230), (360, 370, 90, 100), (460, 470, 330, 340),(770, 780, 340, 350), (830, 840, 140, 150)]#洞的位置
    balls=[]
    group=pygame.sprite.Group()#添加spritecollide的group
    BALL_NUM=5#设置5个小球
    for i in range(BALL_NUM):
        position=randint(0,width-100),randint(0,height-100)#随机位置
        speed=[randint(1,5),randint(1,5)]#随机速度
        ball=Ball(grayball_image,greenball_image,position,speed,bg_size,5*(i+1))
        while pygame.sprite.spritecollide(ball,group,False,pygame.sprite.collide_circle):#如果位置重叠，重新随机位置,增加圆形碰撞
            ball.rect.left,ball.rect.top=randint(0,width-100),randint(0,height-100)
        balls.append(ball)
        group.add(ball)#添加球
    glass=Glass(glass_image,mouse_image,bg_size)#实例化
    motion=0
    MYIMER=USEREVENT+1
    pygame.time.set_timer(MYIMER,1000)
    pygame.key.set_repeat(100,100)#100毫秒开始每100毫秒响应一次
    clock=pygame.time.Clock()#设置帧率
    while running:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==GAMEOVER:
                loser_sound.play()#音乐结束播放cat.wav
                pygame.time.delay(2000)#延时2秒
                running=False#游戏结束
            elif event.type==MYIMER:
                if motion:
                    for each in group:
                        if each.check(motion):
                            each.speed==[0,0]
                            each.control=True
                    motion=0
            elif event.type==MOUSEMOTION:
                motion+=1
            elif event.type==KEYDOWN:#ASDW控制小球
                if event.key==K_w:
                    for each in group:
                        if each.control:
                            each.speed[1]-=1
                if event.key==K_s:
                    for each in group:
                        if each.control:
                            each.speed[1]+=1
                if event.key==K_a:
                    for each in group:
                        if each.control:
                            each.speed[0]-=1
                if event.key==K_d:
                    for each in group:
                        if each.control:
                            each.speed[0]+=1
                if event.key==K_SPACE:
                    for each in group:
                        if each.control:
                            for i in hole:
                                if i[0]<=each.rect.centerx<=i[1] and i[2]<=each.rect.centerx<=i[3]:
                                    each.speed[0,0]#如果进洞，速度为0
                                    group.remove(each)#移出group，其他小球不会对它碰撞检测
                                    temp=balls.pop(balls.index(each))
                                    balls.insert(0,temp)#将此小球先绘制
                                    hole.remove(i)#移除坑位
                                if not hole:
                                    pygame.mixer.music.stop()#没有空洞，音乐停止
        screen.blit(background,(0,0))#画出背景
        screen.blit(glass.glass_image,glass.glass_rect)
        glass.mouse_rect.left,glass.mouse_rect.top=pygame.mouse.get_pos()#获取鼠标位置
        if glass.mouse_rect.left<glass.glass_rect.left:#从左面超出玻璃面板
            glass.mouse_rect.left=glass.glass_rect.left
        if glass.mouse_rect.left>glass.glass_rect.right-glass.mouse_rect.width:#从右边超出玻璃面板
            glass.mouse_rect.left = glass.glass_rect.right-glass.mouse_rect.width
        if glass.mouse_rect.top <glass.glass_rect.top:  # 从上边超出玻璃面板
            glass.mouse_rect.top = glass.glass_rect.top
        if glass.mouse_rect.top > glass.glass_rect.bottom - glass.mouse_rect.height:  # 从下边超出玻璃面板
            glass.mouse_rect.top =glass.glass_rect.bottom - glass.mouse_rect.height
        screen.blit(glass.mouse_image,glass.mouse_rect)
        for each in balls:
            each.move()#调用move方法
            if each.collide:
                each.speed = [randint(1, 5), randint(1, 5)]#重新获得速度
                each.collide=False#碰撞标记复位
            if each.control:
                screen.blit(each.greenball_image,each.rect)#画绿色的
            else:
                screen.blit(each.grayball_image,each.rect)
        for each in group:
            group.remove(each)#移除自身小球
            if pygame.sprite.spritecollide(each,group,False,pygame.sprite.collide_circle):#检测小球碰撞,被碰撞的小球不消失,增加圆形碰撞
                each.side[0]=-each.side[0]#方向取反
                each.side[1]=-each.side[1]
                each.collide=True#碰撞标志改变
                if each.control:
                    each.side[0]=-1
                    each.side[1]=-1#方向取反
                    each.control=False#控制标记改变
            group.add(each)#重新添加小球
        pygame.display.flip()#显示
        clock.tick(30)#每秒30帧
if __name__=="__main__":
    try:
        main()
    except SystemExit:
        pass
    except:#通过cmd打开，返回错误
        traceback.print_exc()
        pygame.quit()
        input()