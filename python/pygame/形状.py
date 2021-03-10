import pygame
import sys
from pygame.locals import *
import math
pygame.init()
WHITE=(255,255,255)#白色
BLACK=(0,0,0)#黑色
RED=(255,0,0)
BLUE=(0,0,255)
size=width,height=640,500
screen=pygame.display.set_mode(size)
pygame.display.set_caption("形状")
points=[(200,75),(300,25),(400,75),(450,25),(450,125),(400,75),(300,125)]#鱼形的坐标
position=size[0]//2,size[1]//2
moving=False
clock=pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            sys.exit()
        if event.type==MOUSEBUTTONDOWN:#按下鼠标
            if event.button==1:#左键
                moving=True
        if event.type==MOUSEBUTTONUP:#松开鼠标
            if event.button==1:
                moving=False
    if moving:
        position=pygame.mouse.get_pos()#追随鼠标移动
    screen.fill(WHITE)#白色背景
    pygame.draw.rect(screen,BLACK,(50,50,150,50),1)#绘制边框为1的黑色矩形在screen上
    pygame.draw.polygon(screen,BLACK,points,0)#绘制多边形
    pygame.draw.circle(screen,BLUE,position,50,1)#绘制边框为1的蓝色圆形
    pygame.draw.ellipse(screen,BLACK,(100,150,440,100),1)#绘制边框为1的椭圆
    pygame.draw.arc(screen,BLACK,(220,200,200,200),math.pi,math.pi*2,1)#绘制从180°到360°的的一部分椭圆
    pygame.draw.lines(screen,RED,1,points,1)#绘制多条线段
    pygame.draw.line(screen,BLACK,(100,350),(540,400),1)#从(100,350)到(540,400)的直线
    pygame.draw.aaline(screen,BLACK,(100,400),(540,450),1)#开启抗锯齿
    pygame.display.flip()
    clock.tick(120)