import pygame#不要和文件名相同
import sys
pygame.init()#初始化pygame
size=width,height=600,400#元组size
screen=pygame.display.set_mode(size)#创建size大小的窗口，surface图像对象
pygame.display.set_caption("hack")#设置窗口标题
bg=(0,0,0)#设置背景
font=pygame.font.Font(None,20)#设置字体
line_height=font.get_linesize()#获取行高
position=0#打印位置
screen.fill(bg)#填充屏幕背景
while True:
        for event in pygame.event.get():#获取事件
                if event.type==pygame.QUIT:#退出事件,点×退出
                        sys.exit()
                screen.blit(font.render(str(event),True,(0,255,0)),(0,position))#显示出获得事件文本,消除锯齿,绿色,从0到position的位置
                position+=line_height#打印位置向下移动
                if position>height:#如果超出窗口大小
                        position=0#位置回到最上面
                        screen.fill(bg)#黑色填充
        pygame.display.flip()#刷新屏幕
