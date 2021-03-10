import pygame
import sys
from pygame.locals import *
pygame.init()
pygame.mixer.init()#初始化混音器
pygame.mixer.music.load("bg_music.ogg")#加载背景音乐
pygame.mixer.music.set_volume(0.2)#设置音量
pygame.mixer.music.play()#开始播放
cat_sound=pygame.mixer.Sound("cat.wav")#加载音效
cat_sound.set_volume(0.1)
dog_sound=pygame.mixer.Sound("dog.wav")#加载音效
dog_sound.set_volume(0.2)
bg_size=width,height=300,200
screen=pygame.display.set_mode(bg_size)#展示窗口
pygame.display.set_caption("music")#设置标题
pause=False
clock=pygame.time.Clock()
while True:
	for event in pygame.event.get():#获取事件
		if event.type==QUIT:#退出事件,点×退出
			sys.exit()
		if event.type==MOUSEBUTTONDOWN:
			if event.button==1:#左键猫叫
				cat_sound.play()
			if event.button==3:#右键狗叫
				dog_sound.play()
		if event.type==KEYDOWN:#空格背景
			if event.key==K_SPACE:
				pause=not pause
	screen.fill((255,255,255))
	if pause:#按下空格暂停背景音乐
		pygame.mixer.music.pause()
	else:
		pygame.mixer.music.unpause()
	pygame.display.flip()
	clock.tick(30)

