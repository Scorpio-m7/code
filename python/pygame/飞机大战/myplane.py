import pygame
class MyPlane(pygame.sprite.Sprite):
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)#初始化
        self.image1=pygame.image.load("images/me1.png").convert_alpha()#载入图片
        self.image2 = pygame.image.load("images/me2.png").convert_alpha()#载入图片
        self.destroy_images=[]#插入毁坏图片
        self.destroy_images.extend([pygame.image.load("images/me_destroy_1.png").convert_alpha(),pygame.image.load("images/me_destroy_2.png").convert_alpha(),pygame.image.load("images/me_destroy_3.png").convert_alpha(),pygame.image.load("images/me_destroy_4.png").convert_alpha()])
        self.rect=self.image1.get_rect()
        self.width,self.height=bg_size[0],bg_size[1]
        self.rect.left,self.rect.top=(self.width-self.rect.width)//2,self.height-self.rect.height-60#初始位置在中间
        self.speed=10#速度
        self.active = True  # 活着的
        self.invincible=False
        self.mask=pygame.mask.from_surface(self.image1)#非透明部分标记为mask
    def moveUp(self):
        if self.rect.top>0:#没有超出边界
            self.rect.top-=self.speed#向上移动
        else:#超出边界
            self.rect.top=0#纠正到0位置
    def moveDown(self):
        if self.rect.bottom<self.height-60:
            self.rect.top+=self.speed#向下移动
        else:
            self.rect.bottom=self.height-60
    def moveLeft(self):
        if self.rect.left>0:
            self.rect.left-=self.speed#向左移动
        else:
            self.rect.left=0
    def moveRight(self):
        if self.rect.right<self.width:
            self.rect.left+=self.speed#向右移动
        else:
            self.rect.right=self.width
    def reset(self):
        self.rect.left, self.rect.top = (self.width - self.rect.width) // 2, self.height - self.rect.height - 60  # 初始位置在中间
        self.active=True
        self.invincible = True