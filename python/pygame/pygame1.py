import pygame#不要和文件名相同
import sys
from pygame.locals import *
pygame.init()#初始化pygame
size=width,height=800,800#元组size
speed=[-2,1]
bg=(255,255,255)#RGB
fullscreen=False#设置不全屏
clock=pygame.time.Clock()#刷新的帧率
screen=pygame.display.set_mode(size,RESIZABLE)#创建size大小的窗口，surface图像对象
pygame.display.set_caption("神龙")#设置窗口标题
ratio=1.0#放大比例
oturtle=pygame.image.load("1.png")#加载图片,jpg,gif,格式都可以
turtle=oturtle
oturtle_rect=oturtle.get_rect()
position=turtle_rect=oturtle_rect#确定矩形
l_head=turtle
r_head=pygame.transform.flip(turtle,True,False)#水平翻转
while True:
	for event in pygame.event.get():#获取事件
		if event.type==pygame.QUIT:#退出事件,点×退出
			sys.exit()
		if event.type==pygame.KEYDOWN:#键盘按下事件
			if event.key==pygame.K_LEFT:#小键盘左键
				turtle=l_head
				speed=[-1,0]#向左移动
			if event.key==pygame.K_RIGHT:#小键盘右键
				turtle=r_head#水平翻转
				speed=[1,0]#向右移动
			if event.key==pygame.K_UP:#小键盘上键
				speed=[0,-1]#向上移动
			if event.key==pygame.K_DOWN:#小键盘下键
				speed=[0,1]#向下移动
			if event.key==K_F11:#按下f11时
				fullscreen= not fullscreen#全屏
				if fullscreen:
					screen=pygame.display.set_mode((1920,1080),FULLSCREEN|HWSURFACE)#全屏显示,硬件加速
					width,height=1920,1080
				else:
					screen=pygame.display.set_mode(size)
			if event.key==K_EQUALS and ratio<2:#按下等于号
				ratio+=0.1#放大10%
			if event.key==K_MINUS and ratio>0.5:#按下减号
				ratio-=0.1#缩小10%
			if event.key==K_SPACE:#按下空格
				ratio=1.0#还原
			turtle=pygame.transform.smoothscale(oturtle,(int(oturtle_rect.width*ratio),int(oturtle_rect.height*ratio)))#平滑缩放图像
			l_head=turtle
			r_head=pygame.transform.flip(turtle,True,False)#水平翻转
		if event.type==VIDEORESIZE:#检测拖拽窗口事件
			size=event.size
			width,height=size
			print(size)
			screen=pygame.display.set_mode(size,RESIZABLE)#重新打印图像
	position=position.move(speed)#移动图像
	if position.left<0 or position.right>width:#超出左右边界	
		turtle=pygame.transform.flip(turtle,True,False)#水平翻转图像,垂直方向不变
		speed[0]=-speed[0]#反向移动
	if position.top<0 or position.bottom>height:#超出上下边界
		speed[1]=-speed[1]
	screen.fill(bg)#填充屏幕背景
	screen.blit(turtle,position)#更新图像
	pygame.display.flip()#刷新屏幕
	#pygame.time.delay(5)#延时5毫秒来控制速度
	clock.tick(200)#设置帧率200