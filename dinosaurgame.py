import pygame
from pygame.locals import *
SCREENWIDTH=822   #高x寬(260x822)
SCREENHEIGHT=260
FPS=30


class MyMap():
    def __init__(self,x,y):  # 构造函数
        self.bg=pygame.image.load(r'background.jpg').convert_alpha()  # 进行图形判断,将背景与其相关的图片透明化
        self.x=x
        self.y=y
        

    def map_rolling(self):  # 滚动
        if self.x<-790:
            self.x=800
        else:
            self.x=-5  # 每帧以5个像素&#xff0c;表示像素移动的距离

    def map_update(self):
            SCREEN.blit(self.bg,(self.x,self.y))

# 恐龙类
from itertools import cycle  # 让我们读取反复不断的用
class Dinosaur():
    def __init__(self):
        # 初始化恐龙图片的矩阵
        self.rect=pygame.Rect(0,0,0,0)
        self.jumpState=False  # 状态
        self.jumpHeight=130  # 跳跃高度
        self.lowest_y=140  # 步行高度
        self.jumpValue=0  # 跳跃速度
        # 加载图片
        self.dinosaurIndex=0
        self.dinosaurIndexGen=cycle([0,1,2])
        self.dinosaur_img=(pygame.image.load(r'dinosaurj.jpg').convert_alpha(),
            pygame.image.load(r'dinosaurj.jpg').convert_alpha(),
            pygame.image.load(r'dinosaurj.jpg').convert_alpha(),
        )
        
        
        # 加载声音
        self.jump_audio=pygame.mixer.Sound('jump.wav')
        self.rect.size=self.dinosaur_img[0].get_size()
        self.x=50
        self.y=self.lowest_y
        self.rect.topleft=(self.x,self.y)

    def jump(self):
        self.jumpState = True

    def move(self):
        if self.jumpState:
            if self.rect.y >= self.lowest_y:
                self.jumpValue = -5  # 向上移动5个矩阵
            if self.rect.y <= self.lowest_y - self.jumpHeight:
                self.jumpValue = 5
            self.rect.y += self.jumpValue
            if self.rect.y >= self.lowest_y:
                self.jumpState = False  # 关闭跳跃状态


    def draw_dinosaur(self):
        # 匹配恐龙动图
        dinosaurIndex=next(self.dinosaurIndexGen)
        SCREEN.blit(self.dinosaur_img[dinosaurIndex],
                    (self.x,self.rect.y))


# 障碍物类
import random
class Obstacle():
    def __init__(self):
        self.rect=pygame.Rect(0,0,0,0)
        self.stone=pygame.image.load(r'stone.jpg').convert_alpha()
        self.cacti=pygame.image.load(r'cacti.jpg').convert_alpha()
        
        r=random.randint(0,1)
        if r==0:
            self.image=self.stone
        else:
            self.image=self.cacti
        self.rect.size=self.image.get_size()
        self.width,self.height=self.rect.size
        self.x=800
        self.y=200-(self.height/2)
        self.rect.center=(self.x,self.y)

    def obstacle_move(self):
        self.rect.x = -5

    def draw_obstacle(self):
        SCREEN.blit(self.image,(self.rect.x,self.rect.y))

# 游戏结束方法
def game_over():
    pass

def mainGame():
    over=False
    global SCREEN,FPSCLOCK  # 全局变量global
    pygame.init()  # 初始化
    FPSCLOCK=pygame.time.Clock()
    SCREEN=pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
    pygame.display.set_caption('dinosaur game')
    # 创建地图
    bg1=MyMap(0,0)
    bg2=MyMap(800,0)
    # 创建恐龙对象
    dinosaur = Dinosaur()
    # 创建一个障碍物集合
    addObasacletime = 0  # 计时器
    list=[]


    while True:
        # 事件监控
        for event in pygame.event.get():
            if event.type==QUIT:
                exit()
        # 单击空格&#xff0c;跳跃
        if event.type == KEYDOWN and event.key == K_SPACE:
            if dinosaur.rect.y >= dinosaur.lowest_y:
                dinosaur.jump()
                dinosaur.jump_audio.play()
            if over == True:
                mainGame()


        if over==False:
            bg1.map_update()  # 出现
            bg1.map_rolling()  # 滚动
            bg2.map_update()  # 出现
            bg2.map_rolling()  # 滚动
            dinosaur.move()  # 恐龙移动
            dinosaur.draw_dinosaur()  # 显示相应动画

            if addObasacletime>=1300:
                r=random.randint(0,100)
                if r > 40:
                    obstacle=Obstacle()
                    list.append(obstacle)
                addObasacletime=0


            for i in range(len(list)):
                list[i].obstacle_move()  # 出现的障碍物移动
                list[i].draw_obstacle()  # 显示出现的障碍物
                if pygame.sprite.collide_rect(dinosaur,list[i]):
                    over = True
                    game_over()



        addObasacletime+=40
        pygame.display.update()
        FPSCLOCK.tick(FPS)


if __name__ == '__main__':
    mainGame()