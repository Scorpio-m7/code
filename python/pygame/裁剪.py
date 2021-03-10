import pygame
import sys
from pygame.locals import *
pygame.init()
size=width,height=800,800
bg=(255,255,255)
clock=pygame.time.Clock()
screen=pygame.display.set_mode(size)
pygame.display.set_caption("标题")
turtle=pygame.image.load("1.png")
select=0#0表示未选择，1表示选择中，2表示选择完成
select_rect=pygame.Rect(0,0,0,0)#初始化矩形对象
drag=0#0表示未拖拽，1表示拖拽中，2表示完成拖拽
position=turtle.get_rect()
position.center=width//2,height//2
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            sys.exit()
        elif event.type==MOUSEBUTTONDOWN:
            if event.button==1:
                if select==0 and drag==0:#第一次点击，选择范围
                    pos_start=event.pos#开始位置
                    select=1
                elif select==2 and drag==0:#第二次点击，拖拽图像
                    capture=screen.subsurface(select_rect).copy()#拷贝子对象的矩形区域
                    cap_rect=capture.get_rect()
                    drag=1
                elif select==2 and drag==2:#第三次点击，初始化
                    select=0
                    drag=0
        elif event.type==MOUSEBUTTONUP:
            if event.button==1:
                if select==1 and drag==0:#第一次释放，结束选择
                    pos_stop=event.pos#停止位置
                    select=2
                if select==2 and drag==1:
                    drag=2
    screen.fill(bg)
    screen.blit(turtle,position)
    if select:#绘制选择框
        mouse_pos=pygame.mouse.get_pos()
        if select==1:
            pos_stop=mouse_pos
            select_rect.left,select_rect.top=pos_start#鼠标位置赋给矩形左上角
            select_rect.width,select_rect.height=pos_stop[0]-pos_start[0],pos_stop[1]-pos_start[1]#矩形宽高
            pygame.draw.rect(screen,(0,0,0),select_rect,1)#在屏幕上画黑色1像素的矩形
    if drag:#拖拽剪裁的图像
        if drag==1:
            cap_rect.center=mouse_pos#鼠标位置赋给矩形中心，随着鼠标移动
        screen.blit(capture,cap_rect)
    pygame.display.flip()
    clock.tick(30)
