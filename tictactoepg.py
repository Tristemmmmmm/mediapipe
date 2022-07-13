import pygame
pygame.init()
                                                #1 2 3
                                                #4 5 6   
                                                #7 8 9 
#營
def Win(board, symbol):
    return((board[1] == symbol and board[2] == symbol and board[3] == symbol) or
    (board[4] == symbol and board[5] == symbol and board[6] == symbol) or
    (board[7] == symbol and board[8] == symbol and board[9] == symbol) or
    (board[1] == symbol and board[4] == symbol and board[7] == symbol) or
    (board[2] == symbol and board[5] == symbol and board[8] == symbol) or
    (board[3] == symbol and board[6] == symbol and board[9] == symbol) or
    (board[1] == symbol and board[5] == symbol and board[9] == symbol) or
    (board[3] == symbol and board[5] == symbol and board[7] == symbol))
"""def isWin(a, symbol):
    return((a1 == symbol and a2 == symbol and a3 == symbol) or
    (a4 == symbol and a5 == symbol and a6 == symbol) or
    (a7 == symbol and a8 == symbol and a9 == symbol) or
    (a1 == symbol and a4 == symbol and a7 == symbol) or
    (a2 == symbol and a5 == symbol and a8 == symbol) or
    (a3 == symbol and a6 == symbol and a9 == symbol) or
    (a1 == symbol and a5 == symbol and a9 == symbol) or
    (a3 == symbol and a5 == symbol and a7 == symbol))"""

def IsWin(pos, symbol):
    return((pos[0] < 170 and pos[1] < 170 == symbol and pos[0] < 330 and pos[1] < 170 == symbol and pos[0] < 490 and pos[1] < 170 == symbol) or
    (pos[0] < 170 and pos[1] < 330 == symbol and pos[0] < 330 and pos[1] < 330 == symbol and pos[0] < 490 and pos[1] < 330 == symbol) or
    (pos[0] < 170 and pos[1] < 490 == symbol and pos[0] < 330 and pos[1] < 490 == symbol and pos[0] < 490 and pos[1] < 490 == symbol) or
    (pos[0] < 170 and pos[1] < 170 == symbol and pos[0] < 170 and pos[1] < 330 == symbol and pos[0] < 170 and pos[1] < 490 == symbol) or
    (pos[0] < 330 and pos[1] < 170 == symbol and pos[0] < 330 and pos[1] < 330 == symbol and pos[0] < 330 and pos[1] < 490 == symbol) or
    (pos[0] < 490 and pos[1] < 170 == symbol and pos[0] < 490 and pos[1] < 330 == symbol and pos[0] < 490 and pos[1] < 490 == symbol) or
    (pos[0] < 170 and pos[1] < 170 == symbol and pos[0] < 330 and pos[1] < 330 == symbol and pos[0] < 490 and pos[1] < 490 == symbol) or
    (pos[0] < 490 and pos[1] < 170 == symbol and pos[0] < 330 and pos[1] < 330 == symbol and pos[0] < 170 and pos[1] < 490 == symbol))
        
#設定視窗
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("圈圈叉叉輸入版")

#建立畫布
bg = pygame.Surface((500,500))
bg.fill((255,255,255))

#畫棋盤
def drawlines():
    pygame.draw.line(bg, (0,0,0), (10,170), (490,170),15)
    pygame.draw.line(bg, (0,0,0), (10,330), (490,330),15)
    pygame.draw.line(bg, (0,0,0), (170,10), (170,490),15)
    pygame.draw.line(bg, (0,0,0), (330,10), (330,490),15)
drawlines()

"""
a1=pygame.draw.circle(bg, (0,0,255), (90,90), 60, 10)
a2=pygame.draw.circle(bg, (0,0,255), (250,90), 60, 10)
a3=pygame.draw.circle(bg, (0,0,255), (90,250), 60, 10)
a4=pygame.draw.circle(bg, (0,0,255), (90,250), 60, 10)
a5=pygame.draw.circle(bg, (0,0,255), (250,250), 60, 10)
a6=pygame.draw.circle(bg, (0,0,255), (410,250), 60, 10)
a7=pygame.draw.circle(bg, (0,0,255), (90,410), 60, 10)
a8=pygame.draw.circle(bg, (0,0,255), (250,410), 60, 10)
a9=pygame.draw.circle(bg, (0,0,255), (410,410), 60, 10)"""

#玩家1畫圈
def draw_circle():
    if pos[0] < 170 and pos[1] < 170:
        pygame.draw.circle(bg, (0,0,255), (90,90), 60, 10)#1            
    elif pos[0] < 330 and pos[1] < 170:
        pygame.draw.circle(bg, (0,0,255), (250,90), 60, 10)#2
    elif pos[0] < 490 and pos[1] < 170:
        pygame.draw.circle(bg, (0,0,255), (410,90), 60, 10)#3
    elif pos[0] < 170 and pos[1] < 330:
        pygame.draw.circle(bg, (0,0,255), (90,250), 60, 10)#4
    elif pos[0] < 330 and pos[1] < 330:
        pygame.draw.circle(bg, (0,0,255), (250,250), 60, 10)#5
    elif pos[0] < 490 and pos[1] < 330:
        pygame.draw.circle(bg, (0,0,255), (410,250), 60, 10)#6
    elif pos[0] < 170 and pos[1] < 490:
        pygame.draw.circle(bg, (0,0,255), (90,410), 60, 10)#7
    elif pos[0] < 330 and pos[1] < 490:
        pygame.draw.circle(bg, (0,0,255), (250,410), 60, 10)#8
    elif pos[0] < 490 and pos[1] < 490:
        pygame.draw.circle(bg, (0,0,255), (410,410), 60, 10)#9
        
#玩家2畫叉
def draw_prong():
    if pos[0] < 170 and pos[1] < 170:
        pygame.draw.line(bg, (255,0,0), (30,30), (150,150),10)#1
        pygame.draw.line(bg, (255,0,0), (150,30), (30,150),10)#1
    elif pos[0] < 330 and pos[1] < 170:
        pygame.draw.line(bg, (255,0,0), (190,30), (310,150),10)#2
        pygame.draw.line(bg, (255,0,0), (310,30), (190,150),10)#2
    elif pos[0] < 490 and pos[1] < 170:
        pygame.draw.line(bg, (255,0,0), (350,30), (470,150),10)#3
        pygame.draw.line(bg, (255,0,0), (470,30), (350,150),10)#3
    elif pos[0] < 170 and pos[1] < 330:
        pygame.draw.line(bg, (255,0,0), (30,190), (150,310),10)#4
        pygame.draw.line(bg, (255,0,0), (150,190), (30,310),10)#4
    elif pos[0] < 330 and pos[1] < 330:
        pygame.draw.line(bg, (255,0,0), (190,190), (310,310),10)#5
        pygame.draw.line(bg, (255,0,0), (310,190), (190,310),10)#5
    elif pos[0] < 490 and pos[1] < 330:
        pygame.draw.line(bg, (255,0,0), (350,190), (470,310),10)#6
        pygame.draw.line(bg, (255,0,0), (470,190), (350,310),10)#6
    elif pos[0] < 170 and pos[1] < 490:
        pygame.draw.line(bg, (255,0,0), (30,350), (150,470),10)#7
        pygame.draw.line(bg, (255,0,0), (150,350), (30,470),10)#7
    elif pos[0] < 330 and pos[1] < 490:
        pygame.draw.line(bg, (255,0,0), (190,350), (310,470),10)#8
        pygame.draw.line(bg, (255,0,0), (310,350), (190,470),10)#8
    elif pos[0] < 490 and pos[1] < 490:
        pygame.draw.line(bg, (255,0,0), (350,350), (470,470),10)#9
        pygame.draw.line(bg, (255,0,0), (470,350), (350,470),10)#9

#main loop    
running = True
player = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]: #0是左鍵1是中間滾輪2是柚見
                pos = pygame.mouse.get_pos()
                if player == 0:
                    draw_circle()
                    player = 1
                #ifwin
                else:
                    draw_prong()
                    player = 0
                        
    #顯示畫布
    screen.blit(bg,(0,0))
    pygame.display.update()

pygame.quit()

