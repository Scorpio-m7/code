import pygame
class Bullet1(pygame.sprite.Sprite):
    def __init__(self,position):
        pygame.sprite.Sprite.__init__(self)#初始化
        self.image=pygame.image.load("images/bullet1.png").convert_alpha()#载入图片
        self.rect=self.image.get_rect()
        self.rect.left,self.rect.top=position
        self.speed=12#速度
        self.active=False
        self.mask=pygame.mask.from_surface(self.image)#非透明部分标记为mask
    def move(self):
        self.rect.top-=self.speed
        if self.rect.top<0:
            self.active=False
    def reset(self,position):
        self.rect.left,self.rect.top=position
        self.active=True
class Bullet2(pygame.sprite.Sprite):
    def __init__(self,position):
        pygame.sprite.Sprite.__init__(self)#初始化
        self.image=pygame.image.load("images/bullet2.png").convert_alpha()#载入图片
        self.rect=self.image.get_rect()
        self.rect.left,self.rect.top=position
        self.speed=15#速度
        self.active=False
        self.mask=pygame.mask.from_surface(self.image)#非透明部分标记为mask
    def move(self):
        self.rect.top-=self.speed
        if self.rect.top<0:
            self.active=False
    def reset(self,position):
        self.rect.left,self.rect.top=position
        self.active=True