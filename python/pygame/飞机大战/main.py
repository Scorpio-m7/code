import pygame
import sys
import traceback
import myplane
import enemy
import bullet
import supply
from random import *
from pygame.locals import *
pygame.init()#初始化
pygame.mixer.init()#混音器初始化
bg_size=width,height=480,700#根据background.png设置
screen=pygame.display.set_mode(bg_size)
pygame.display.set_caption("飞机大战")
background=pygame.image.load("images/background.png").convert()
BLACK=(0,0,0)
GREEN=(0,255,0)
RED=(255,0,0)
WHITE=(255,255,255)
pygame.mixer.music.load("sound/game_music.ogg")#载入游戏音乐
pygame.mixer.music.set_volume(0.2)
bullet_sound = pygame.mixer.Sound("sound/bullet.wav")
bullet_sound.set_volume(0.2)
bomb_sound = pygame.mixer.Sound("sound/use_bomb.wav")
bomb_sound.set_volume(0.2)
supply_sound = pygame.mixer.Sound("sound/supply.wav")
supply_sound.set_volume(0.2)
get_bomb_sound = pygame.mixer.Sound("sound/get_bomb.wav")
get_bomb_sound.set_volume(0.2)
get_bullet_sound = pygame.mixer.Sound("sound/get_bullet.wav")
get_bullet_sound.set_volume(0.2)
upgrade_sound = pygame.mixer.Sound("sound/upgrade.wav")
upgrade_sound.set_volume(0.2)
enemy3_fly_sound = pygame.mixer.Sound("sound/enemy3_flying.wav")
enemy3_fly_sound.set_volume(0.2)
enemy1_down_sound = pygame.mixer.Sound("sound/enemy1_down.wav")
enemy1_down_sound.set_volume(0.2)
enemy2_down_sound = pygame.mixer.Sound("sound/enemy2_down.wav")
enemy2_down_sound.set_volume(0.2)
enemy3_down_sound = pygame.mixer.Sound("sound/enemy3_down.wav")
enemy3_down_sound.set_volume(0.5)
me_down_sound = pygame.mixer.Sound("sound/me_down.wav")
me_down_sound.set_volume(0.2)
def add_small_enemies(group1,group2,num):
    for i in range(num):
        e1=enemy.SmallEnemy(bg_size)
        group1.add(e1)
        group2.add(e1)
def add_mid_enemies(group1,group2,num):
    for i in range(num):
        e2=enemy.MidEnemy(bg_size)
        group1.add(e2)
        group2.add(e2)
def add_big_enemies(group1,group2,num):
    for i in range(num):
        e3=enemy.BigEnemy(bg_size)
        group1.add(e3)
        group2.add(e3)
def inc_speed(target,inc):
    for each in target:
        each.speed+=inc
def main():
    pygame.mixer.music.play(-1)#播放背景音乐
    me=myplane.MyPlane(bg_size)#生成我方飞机
    enemies=pygame.sprite.Group()#生成敌方飞机
    small_enemies=pygame.sprite.Group()#生成小型飞机
    add_small_enemies(small_enemies,enemies,15)
    mid_enemies = pygame.sprite.Group()  # 生成中型飞机
    add_mid_enemies(mid_enemies, enemies, 4)
    big_enemies = pygame.sprite.Group()  # 生成大型飞机
    add_big_enemies(big_enemies, enemies, 4)
    bullet1=[]#生成普通子弹
    bullet1_index=0
    bullet1_NUM=4#四颗子弹
    for i in range(bullet1_NUM):
        bullet1.append(bullet.Bullet1(me.rect.midtop))#顶部中央生成子弹
    bullet2 = []  # 生成超级子弹
    bullet2_index = 0
    bullet2_NUM = 8  # 8颗子弹
    for i in range(bullet2_NUM//2):
        bullet2.append(bullet.Bullet2((me.rect.centerx-33,me.rect.centery)))
        bullet2.append(bullet.Bullet2((me.rect.centerx+30,me.rect.centery)))#从炮筒射击
    clock=pygame.time.Clock()
    e1_destroy_index=0#中弹图片索引
    e2_destroy_index = 0
    e3_destroy_index = 0
    me_destroy_index = 0
    score=0#统计得分
    score_font=pygame.font.Font("font/font.ttf",36)#加载36号字体
    paused=False#暂停标志
    paused_nor_image=pygame.image.load("images/pause_nor.png").convert_alpha()
    paused_pressed_image=pygame.image.load("images/pause_pressed.png").convert_alpha()
    resume_nor_image=pygame.image.load("images/resume_nor.png").convert_alpha()
    resume_pressed_image = pygame.image.load("images/resume_pressed.png").convert_alpha()
    paused_rect=paused_nor_image.get_rect()
    paused_rect.left,paused_rect.top=width-paused_rect.width-10,10#右上角显示
    paused_image=paused_nor_image
    level=1
    bomb_image=pygame.image.load("images/bomb.png").convert_alpha()#全屏炸弹
    bomb_rect=bomb_image.get_rect()
    bomb_font=pygame.font.Font("font/font.ttf",48)#48号字体
    bomb_num=3
    bullet_supply=supply.Bullet_Supply(bg_size)#每30秒发放一个补给包
    bomb_supply=supply.Bomb_Supply(bg_size)#实例化
    SUPPLY_TIME=USEREVENT#自定义事件
    pygame.time.set_timer(SUPPLY_TIME,30*1000)#30秒
    DOUBLE_BULLET_TIEM=USEREVENT+1#超级子弹定时器
    is_double_bullet=False#标志是否使用超级子弹
    INVINCIBLE_TIME=USEREVENT+2#解除我方无敌状态计时器
    life_image=pygame.image.load("images/life.png").convert_alpha()
    life_rect=life_image.get_rect()
    life_num=3#生命数量
    recorded=False#防止重复打开文件
    gameover_font=pygame.font.Font("font/font.ttf",48)#游戏结束画面
    again_image=pygame.image.load("images/again.png").convert_alpha()
    again_rect=again_image.get_rect()
    gameover_image=pygame.image.load("images/gameover.png").convert_alpha()
    gameover_rect=gameover_image.get_rect()
    switch_image=True#用于切换me1.png和me2.png
    delay=100#用于延迟
    running=True
    while running:
        for event in pygame.event.get():
            if event.type==QUIT:#退出
                pygame.quit()
                sys.exit()
            elif event.type==MOUSEBUTTONDOWN:
                if event.button==1 and paused_rect.collidepoint(event.pos):#检测点是否在矩形中
                    paused=not paused
                    if paused:
                        pygame.time.set_timer(SUPPLY_TIME,0)#取消自定义事件(补给)
                        pygame.mixer.music.pause()#暂停音乐
                        pygame.mixer.pause()#暂停音效
                    else:
                        pygame.time.set_timer(SUPPLY_TIME,30*1000)#自定义事件
                        pygame.mixer.music.unpause()#恢复音乐
                        pygame.mixer.unpause()#恢复音效
            elif event.type==MOUSEMOTION:
                if paused_rect.collidepoint(event.pos):
                    if paused:
                        paused_image=resume_pressed_image
                    else:
                        paused_image=paused_pressed_image
                else:
                    if paused:
                        paused_image=resume_nor_image
                    else:
                        paused_image=paused_nor_image
            elif event.type==KEYDOWN:
                if event.key==K_SPACE:#按下空格用炸弹
                    if bomb_num:
                        bomb_num-=1
                        bomb_sound.play()
                        for each in enemies:
                            if each.rect.bottom>0:
                                each.active=False
            elif event.type==SUPPLY_TIME:#响应事件
                supply_sound.play()
                if choice([True,False]):#在true和false中选择一个
                    bomb_supply.reset()
                else:
                    bullet_supply.reset()
            elif event.type==DOUBLE_BULLET_TIEM:
                is_double_bullet=False
                pygame.time.set_timer(DOUBLE_BULLET_TIEM,0)#取消定时器
            elif event.type==INVINCIBLE_TIME:
                me.invincible=False
                pygame.time.set_timer(INVINCIBLE_TIME,0)#解除无敌
        if level==1 and score>30:
            level=2#根据得分增加难度
            upgrade_sound.play()
            add_small_enemies(small_enemies,enemies,4)#增加4架小敌机
            add_mid_enemies(mid_enemies,enemies,3)#增加3架中敌机
            add_big_enemies(big_enemies,enemies,1)#增加一架大敌机
            inc_speed(small_enemies,2)#提升小敌机的速度
        elif level==2 and score>100:
            level=3#根据得分增加难度
            upgrade_sound.play()
            add_small_enemies(small_enemies,enemies,5)#增加5架小敌机
            add_mid_enemies(mid_enemies,enemies,4)#增加4架中敌机
            add_big_enemies(big_enemies,enemies,2)#增加2架大敌机
            inc_speed(small_enemies,2)#提升小敌机的速度
            inc_speed(mid_enemies, 2)  # 提升中敌机的速度
        elif level==3 and score>300:
            level=4#根据得分增加难度
            upgrade_sound.play()
            add_small_enemies(small_enemies,enemies,6)#增加6架小敌机
            add_mid_enemies(mid_enemies,enemies,5)#增加5架中敌机
            add_big_enemies(big_enemies,enemies,3)#增加3架大敌机
            inc_speed(small_enemies,2)#提升小敌机的速度
            inc_speed(mid_enemies, 2)  # 提升中敌机的速度
            inc_speed(big_enemies, 2)  # 提升大敌机的速度
        screen.blit(background, (0, 0))
        if life_num and not paused:
            key_pressed=pygame.key.get_pressed()#检测键盘按下操作
            if key_pressed[K_w] or key_pressed[K_UP]:
                me.moveUp()
            if key_pressed[K_s] or key_pressed[K_DOWN]:
                me.moveDown()
            if key_pressed[K_a] or key_pressed[K_LEFT]:
                me.moveLeft()
            if key_pressed[K_d] or key_pressed[K_RIGHT]:
                me.moveRight()
            if bomb_supply.active:#绘制全屏炸弹并检测是否获得
                bomb_supply.move()
                screen.blit(bomb_supply.image,bomb_supply.rect)
                if pygame.sprite.collide_mask(bomb_supply,me):#检测碰撞
                    get_bomb_sound.play()
                    if bomb_num<3:
                        bomb_num+=1
                    bomb_supply.active=False
            if bullet_supply.active:#绘制超级子弹并检测是否获得
                bullet_supply.move()
                screen.blit(bullet_supply.image,bullet_supply.rect)
                if pygame.sprite.collide_mask(bullet_supply,me):#检测碰撞
                    get_bullet_sound.play()
                    is_double_bullet=True#发射超级子弹
                    pygame.time.set_timer(DOUBLE_BULLET_TIEM,18*1000)#18秒的使用时间
                    bullet_supply.active=False
            if not (delay%10):
                bullet_sound.play()
                if is_double_bullet:
                    bullets=bullet2
                    bullets[bullet2_index].reset((me.rect.centerx-33,me.rect.centery))#发射子弹
                    bullets[bullet2_index+1].reset((me.rect.centerx+30,me.rect.centery))
                    bullet2_index = (bullet2_index + 2) % bullet2_NUM  # 指向下一个索引,不能超过8
                else:
                    bullets=bullet1
                    bullets[bullet1_index].reset(me.rect.midtop)#发射子弹
                    bullet1_index=(bullet1_index+1)%bullet1_NUM#指向下一个索引,不能超过4
            for b in bullets:#检测子弹是否击中
                if b.active:
                    b.move()
                    screen.blit(b.image,b.rect)
                    enemy_hit=pygame.sprite.spritecollide(b,enemies,False,pygame.sprite.collide_mask)#被子弹打中的敌机
                    if enemy_hit:
                        b.active=False
                        for e in enemy_hit:
                            if e in mid_enemies or e in big_enemies:
                                e.hit=True
                                e.energy-=1#每次击中减1点血
                                if e.energy==0:
                                    e.active=False
                            else:
                                e.active=False
            for each in big_enemies:
                if each.active:
                    each.move()
                    if each.hit:#绘制被打到的特效
                        screen.blit(each.image_hit,each.rect)
                        each.hit=False
                    else:
                        if switch_image:#绘制大型敌机
                            screen.blit(each.image1,each.rect)
                        else:
                            screen.blit(each.image2,each.rect)
                    pygame.draw.line(screen,BLACK,(each.rect.left,each.rect.top-5),(each.rect.right,each.rect.top-5),2)#绘制血槽
                    energy_remain=each.energy/enemy.BigEnemy.energy
                    if energy_remain>0.2:#如果生命大于20%显示绿色,否则显示红色
                        enemies_color=GREEN
                    else:
                        enemies_color=RED
                    pygame.draw.line(screen,enemies_color,(each.rect.left,each.rect.top-5),(each.rect.left+each.rect.width*energy_remain,each.rect.top-5),2)
                    if each.rect.bottom==-50:#即将出现播放音乐
                        enemy3_fly_sound.play(-1)
                else:
                    if not(delay%3):
                        if e3_destroy_index == 0:
                            enemy3_down_sound.play()#播放毁灭音效
                        screen.blit(each.destroy_images[e3_destroy_index],each.rect)
                        e3_destroy_index=(e3_destroy_index+1)%6#依次播放毁灭画面
                        if e3_destroy_index==0:
                            enemy3_fly_sound.stop()
                            score+=100
                            each.reset()
            for each in mid_enemies:
                if each.active:
                    each.move()#绘制中型敌机
                    if each.hit:
                        screen.blit(each.image_hit,each.rect)
                        each.hit=False
                    else:
                        screen.blit(each.image,each.rect)
                    pygame.draw.line(screen, BLACK, (each.rect.left, each.rect.top - 5),
                                     (each.rect.right, each.rect.top - 5), 2)  # 绘制血槽
                    energy_remain = each.energy / enemy.MidEnemy.energy
                    if energy_remain > 0.2:  # 如果生命大于20%显示绿色,否则显示红色
                        enemies_color = GREEN
                    else:
                        enemies_color = RED
                    pygame.draw.line(screen, enemies_color, (each.rect.left, each.rect.top - 5),
                                     (each.rect.left + each.rect.width * energy_remain, each.rect.top - 5), 2)
                else:
                    if not(delay%3):
                        if e2_destroy_index == 0:
                            enemy2_down_sound.play()#播放毁灭音效
                        screen.blit(each.destroy_images[e2_destroy_index],each.rect)
                        e2_destroy_index=(e2_destroy_index+1)%4#依次播放毁灭画面
                        if e2_destroy_index==0:
                            score+=10
                            each.reset()
            for each in small_enemies:
                if each.active:
                    each.move()#绘制小型敌机
                    screen.blit(each.image,each.rect)
                else:
                    if not(delay%3):
                        if e1_destroy_index == 0:
                            enemy1_down_sound.play()#播放毁灭音效
                        screen.blit(each.destroy_images[e1_destroy_index],each.rect)
                        e1_destroy_index=(e1_destroy_index+1)%4#依次播放毁灭画面
                        if e1_destroy_index==0:
                            score+=1
                            each.reset()
            enemies_down=pygame.sprite.spritecollide(me,enemies,False,pygame.sprite.collide_mask)#检测碰撞
            if enemies_down and not me.invincible:
                me.active=False#飞机毁灭
                for e in enemies_down:
                    e.active=False
            if me.active:
                if switch_image:
                     screen.blit(me.image1,me.rect)#绘制我方飞机
                else:
                    screen.blit(me.image2,me.rect)
            else:
                if not (delay % 3):
                    if me_destroy_index == 0:
                        me_down_sound.play()  # 播放毁灭音效
                    screen.blit(me.destroy_images[me_destroy_index], me.rect)
                    me_destroy_index = (me_destroy_index + 1) % 4 # 依次播放毁灭画面
                    if me_destroy_index == 0:
                        life_num-=1
                        me.reset()
                        pygame.time.set_timer(INVINCIBLE_TIME,3*1000)#3秒无敌
            bomb_text=bomb_font.render("*%d"%bomb_num,True,WHITE)#绘制炸弹数量
            text_rect=bomb_text.get_rect()
            screen.blit(bomb_image,(10,height-10-bomb_rect.height))
            screen.blit(bomb_text,(20+bomb_rect.width,height-5-text_rect.height))
            if life_num:#绘制剩余生命数量
                for i in range(life_num):
                    screen.blit(life_image,(width-10-(i+1)*life_rect.width,height-10-life_rect.height))
            score_text = score_font.render("Score:%s" % str(score), True, WHITE)  # 白色分数，无抗锯齿
            screen.blit(score_text, (10, 5))  # 绘制得分
        elif life_num==0:#绘制游戏结束画面
            pygame.mixer.music.stop()#背景音乐停止
            pygame.mixer.stop()#停止全部音效
            pygame.time.set_timer(SUPPLY_TIME,0)#停止发放补给
            if not recorded:
                recorded=True
                with open("record.txt","r") as f:
                    record_score=int(f.read())#读取历史最高分
                if score>record_score:
                    with open("record.txt","w") as f:
                        f.write(str(score))#如果高于历史最高分,则存档
            record_score_text = score_font.render("Best: %d" % record_score, True, WHITE)# 绘制结束画面
            screen.blit(record_score_text, (10, 5))
            gameover_text1 = gameover_font.render("Your Score: ", True, WHITE)
            gameover_text1_rect = gameover_text1.get_rect()
            gameover_text1_rect.left, gameover_text1_rect.top = (width - gameover_text1_rect.width) // 2, height // 2
            screen.blit(gameover_text1, gameover_text1_rect)
            gameover_text2 = gameover_font.render(str(score), True, WHITE)
            gameover_text2_rect = gameover_text2.get_rect()
            gameover_text2_rect.left, gameover_text2_rect.top = (width - gameover_text2_rect.width) // 2,gameover_text1_rect.bottom + 10
            screen.blit(gameover_text2, gameover_text2_rect)
            again_rect.left, again_rect.top = (width - again_rect.width) // 2, gameover_text2_rect.bottom + 50
            screen.blit(again_image, again_rect)
            gameover_rect.left, gameover_rect.top = (width - again_rect.width) // 2,again_rect.bottom + 10
            screen.blit(gameover_image, gameover_rect)
            if pygame.mouse.get_pressed()[0]:# 检测用户的鼠标操作
                pos = pygame.mouse.get_pos()# 如果用户按下鼠标左键
                if again_rect.left < pos[0] < again_rect.right and again_rect.top < pos[1] < again_rect.bottom:
                    main()
                elif gameover_rect.left < pos[0] < gameover_rect.right and gameover_rect.top < pos[1] < gameover_rect.bottom:
                    pygame.quit()
                    sys.exit()
        screen.blit(paused_image,paused_rect)#绘制暂停图片
        if not (delay%5):#切换图片
            switch_image=not switch_image
        delay-=1
        if not delay:
            delay=100
        pygame.display.flip()
        clock.tick(60)#60帧
if __name__=="__main__":
    try:
        main()
    except SystemExit:
        pass#正常退出
    except:
        traceback.print_exc()
        pygame.quit()
        input()