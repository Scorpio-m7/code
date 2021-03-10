import pygame
from random import *
class Bullet_Supply(pygame.sprite.Sprite):#继承精灵
    def __init__(self,bg_size):#初始化
        pygame.sprite.Sprite.__init__(self)#调用sprite初始化
        self.image=pygame.image.load("images/bullet_supply.png").convert_alpha()
        self.rect=self.image.get_rect()#获得矩形
        self.width,self.height=bg_size[0],bg_size[1]#背景尺寸本地化
        self.rect.left,self.rect.bottom=randint(0,self.width-self.rect.width),-100
        self.speed=5
        self.active=False#默认不开启
        self.mask=pygame.mask.from_surface(self.image)
    def move(self):
        if self.rect.top<self.height:
            self.rect.top+=self.speed
        else:
            self.active=False#超出底部失效
    def reset(self):
        self.active=True
        self.rect.left, self.rect.bottom = randint(0, self.width - self.rect.width), -100#重新获得随机位置
class Bomb_Supply(pygame.sprite.Sprite):  # 继承精灵
    def __init__(self, bg_size):  # 初始化
        pygame.sprite.Sprite.__init__(self)  # 调用sprite初始化
        self.image = pygame.image.load("images/bomb_supply.png").convert_alpha()
        self.rect = self.image.get_rect()  # 获得矩形
        self.width, self.height = bg_size[0], bg_size[1]  # 背景尺寸本地化
        self.rect.left, self.rect.bottom = randint(0, self.width - self.rect.width), -100
        self.speed = 5
        self.active = False  # 默认不开启
        self.mask = pygame.mask.from_surface(self.image)
    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.active = False  # 超出底部失效
    def reset(self):
        self.active = True
        self.rect.left, self.rect.bottom = randint(0, self.width - self.rect.width), -100  # 重新获得随机位置
