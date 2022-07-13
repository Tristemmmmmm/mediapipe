import pygame
pygame.init()

LINE_WIDTH = 10
CROSS_WIDTH = 13
CIRCLE_WIDTH = 10
CIRCLE_RADIUS = 60

CROSS_COLOR = (255,114,86)
CIRCLE_COLOR = (139,137,137)
LINE_COLOR = (54,54,54)
BG_COLOR = (255,255,255)

font = pygame.font.SysFont("simhei", 50)
text_player1 = font.render("It's player1 turn", True, (255,255,255),(0,0,0))
text_player2 = font.render("It's player2 turn", True, (255,255,255),(0,0,0))
win_player1 = font.render("player1 win          ", True, (255,255,255),(0,0,0))
win_player2 = font.render("player2 win          ", True, (255,255,255),(0,0,0))
text_tie = font.render("tie                              ", True, (255,255,255),(0,0,0))

#設定視窗
screen = pygame.display.set_mode((600, 650))
pygame.display.set_caption("tic_tac_toe")

#建立畫布
bg = pygame.Surface((600,600))
bg.fill(BG_COLOR)

#畫棋盤
def drawlines():
    pygame.draw.line(bg, LINE_COLOR, (200,0), (200,600),LINE_WIDTH)
    pygame.draw.line(bg, LINE_COLOR, (400,0), (400,600),LINE_WIDTH)
    pygame.draw.line(bg, LINE_COLOR, (0,200), (600,200),LINE_WIDTH)
    pygame.draw.line(bg, LINE_COLOR, (0,400), (600,400),LINE_WIDTH)
drawlines()

#玩家1畫圈
def draw_circle():
    if pos[0] < 200 and pos[1] < 200:
        pygame.draw.circle(bg, CIRCLE_COLOR, (100,100), CIRCLE_RADIUS, CIRCLE_WIDTH)#1
        board_item[0] = "circle"
    elif pos[0] < 400 and pos[1] < 200:
        pygame.draw.circle(bg, CIRCLE_COLOR, (300,100), CIRCLE_RADIUS, CIRCLE_WIDTH)#2
        board_item[1] = "circle"
    elif pos[0] < 600 and pos[1] < 200:
        pygame.draw.circle(bg, CIRCLE_COLOR, (500,100), CIRCLE_RADIUS, CIRCLE_WIDTH)#3
        board_item[2] = "circle"
    elif pos[0] < 200 and pos[1] < 400:
        pygame.draw.circle(bg, CIRCLE_COLOR, (100,300), CIRCLE_RADIUS, CIRCLE_WIDTH)#4
        board_item[3] = "circle"
    elif pos[0] < 400 and pos[1] < 400:
        pygame.draw.circle(bg, CIRCLE_COLOR, (300,300), CIRCLE_RADIUS, CIRCLE_WIDTH)#5
        board_item[4] = "circle"
    elif pos[0] < 600 and pos[1] < 400:
        pygame.draw.circle(bg, CIRCLE_COLOR, (500,300), CIRCLE_RADIUS, CIRCLE_WIDTH)#6
        board_item[5] = "circle"
    elif pos[0] < 200 and pos[1] < 600:
        pygame.draw.circle(bg, CIRCLE_COLOR, (100,500), CIRCLE_RADIUS, CIRCLE_WIDTH)#7
        board_item[6] = "circle"
    elif pos[0] < 400 and pos[1] < 600:
        pygame.draw.circle(bg, CIRCLE_COLOR, (300,500), CIRCLE_RADIUS, CIRCLE_WIDTH)#8
        board_item[7] = "circle"
    elif pos[0] < 600 and pos[1] < 600:
        pygame.draw.circle(bg, CIRCLE_COLOR, (500,500), CIRCLE_RADIUS, CIRCLE_WIDTH)#9
        board_item[8] = "circle"
        
#玩家2畫叉
def draw_cross():
    if pos[0] < 200 and pos[1] < 200:
        pygame.draw.line(bg, CROSS_COLOR, (50,50), (150,150),CROSS_WIDTH)#1
        pygame.draw.line(bg, CROSS_COLOR, (150,50), (50,150),CROSS_WIDTH)#1
        board_item[0] = "cross"
    elif pos[0] < 400 and pos[1] < 200:
        pygame.draw.line(bg, CROSS_COLOR, (250,50), (350,150),CROSS_WIDTH)#2
        pygame.draw.line(bg, CROSS_COLOR, (350,50), (250,150),CROSS_WIDTH)#2
        board_item[1] = "cross"
    elif pos[0] < 600 and pos[1] < 200:
        pygame.draw.line(bg, CROSS_COLOR, (450,50), (550,150),CROSS_WIDTH)#3
        pygame.draw.line(bg, CROSS_COLOR, (550,50), (450,150),CROSS_WIDTH)#3
        board_item[2] = "cross"
    elif pos[0] < 200 and pos[1] < 400:
        pygame.draw.line(bg, CROSS_COLOR, (50,250), (150,350),CROSS_WIDTH)#4
        pygame.draw.line(bg, CROSS_COLOR, (150,250), (50,350),CROSS_WIDTH)#4
        board_item[3] = "cross"
    elif pos[0] < 400 and pos[1] < 400:
        pygame.draw.line(bg, CROSS_COLOR, (250,250), (350,350),CROSS_WIDTH)#5
        pygame.draw.line(bg, CROSS_COLOR, (350,250), (250,350),CROSS_WIDTH)#5
        board_item[4] = "cross"
    elif pos[0] < 600 and pos[1] < 400:
        pygame.draw.line(bg, CROSS_COLOR, (450,250), (550,350),CROSS_WIDTH)#6
        pygame.draw.line(bg, CROSS_COLOR, (550,250), (450,350),CROSS_WIDTH)#6
        board_item[5] = "cross"
    elif pos[0] < 200 and pos[1] < 600:
        pygame.draw.line(bg, CROSS_COLOR, (50,450), (150,550),CROSS_WIDTH)#7
        pygame.draw.line(bg, CROSS_COLOR, (150,450), (50,550),CROSS_WIDTH)#7
        board_item[6] = "cross"
    elif pos[0] < 400 and pos[1] < 600:
        pygame.draw.line(bg, CROSS_COLOR, (250,450), (350,550),CROSS_WIDTH)#8
        pygame.draw.line(bg, CROSS_COLOR, (350,450), (250,550),CROSS_WIDTH)#8
        board_item[7] = "cross"
    elif pos[0] < 600 and pos[1] < 600:
        pygame.draw.line(bg, CROSS_COLOR, (450,450), (550,550),CROSS_WIDTH)#9
        pygame.draw.line(bg, CROSS_COLOR, (550,450), (450,550),CROSS_WIDTH)#9
        board_item[8] = "cross"
        
def is_board_null(): 
    if pos[0] < 200 and pos[1] < 200:
         if board_null[0] == True:
             board_null[0] = False
             return True 
         else:
             return False
    elif pos[0] < 400 and pos[1] < 200:
         if board_null[1] == True:
             board_null[1] = False
             return True 
         else:
             return False
    elif pos[0] < 600 and pos[1] < 200:
        if board_null[2] == True:
             board_null[2] = False
             return True 
        else:
             return False
    elif pos[0] < 200 and pos[1] < 400:
        if board_null[3] == True:
             board_null[3] = False
             return True 
        else:
             return False
    elif pos[0] < 400 and pos[1] < 400:
        if board_null[4] == True:
             board_null[4] = False
             return True 
        else:
             return False
    elif pos[0] < 600 and pos[1] < 400:
        if board_null[5] == True:
             board_null[5] = False
             return True 
        else:
             return False
    elif pos[0] < 200 and pos[1] < 600:
        if board_null[6] == True:
             board_null[6] = False
             return True 
        else:
             return False
    elif pos[0] < 400 and pos[1] < 600:
        if board_null[7] == True:
             board_null[7] = False
             return True 
        else:
             return False
    elif pos[0] < 600 and pos[1] < 600:
        if board_null[8] == True:#如果是空的
             board_null[8] = False
             return True 
        else:
             return False
         
def win():
    return((board_item[0]  == board_item[1]  == board_item[2] ) or
    (board_item[3]  == board_item[4]  == board_item[5]) or
    (board_item[6]  == board_item[7]  == board_item[8] ) or
    (board_item[0]  == board_item[3]  == board_item[6] ) or
    (board_item[1]  == board_item[4]  == board_item[7] ) or
    (board_item[2]  == board_item[5]  == board_item[8] ) or
    (board_item[0]  == board_item[4]  == board_item[8] ) or
    (board_item[2]  == board_item[4]  == board_item[6] ))

def tie():
    for board in board_null:
        if board == True:
            return False
    return True

#main loop    
running = True
player = 0
board_null = [True,True,True,True,True,True,True,True,True]
board_item = ["0","1","2","3","4","5","6","7","8"]
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if win():
                    running = False
                elif tie():
                    running = False
                else:
                    pos = pygame.mouse.get_pos()
                    if is_board_null() == True:
                        if player == 0:
                            draw_circle()                       
                            player = 1
                            
                        elif player == 1:
                            draw_cross()
                            player = 0
    
    if win() == True:
        if player == 1:
            screen.blit(win_player1,(0,600))
            
        elif player == 0:
            screen.blit(win_player2,(0,600))
          
    elif tie():
        screen.blit(text_tie,(0,600))
    elif player == 0:
        screen.blit(text_player1,(0,600))
    elif player == 1:
        screen.blit(text_player2,(0,600))
        
    #顯示畫布
    screen.blit(bg,(0,0))
    pygame.display.update()
    
pygame.quit()

