import tkinter.messagebox
import keyboard
import pygame as pg
import random
import sys
   
def goFirst():
    if random.randint(0,1)==0:
        return "player1"
    else:
        return "player2"

def goPos(board,symbol,pos):
    board[pos] = pos
    
def isWin(board, symbol):
    return((board[1] == symbol and board[2] == symbol and board[3] == symbol) or
    (board[4] == symbol and board[5] == symbol and board[6] == symbol) or
    (board[7] == symbol and board[8] == symbol and board[9] == symbol) or
    (board[1] == symbol and board[4] == symbol and board[7] == symbol) or
    (board[2] == symbol and board[5] == symbol and board[8] == symbol) or
    (board[3] == symbol and board[6] == symbol and board[9] == symbol) or
    (board[1] == symbol and board[5] == symbol and board[9] == symbol) or
    (board[3] == symbol and board[5] == symbol and board[7] == symbol))

def freeSpace(board, pos):
    return board[pos] == ''
    
def isFull(board):
    for i in range(1,10):
        if freeSpace(board, i):
            return True
    return False
root = tkinter.Tk()
root.withdraw()
pg.init()

width, height = 800,800                    
screen = pg.display.set_mode((width, height))   
pg.display.set_caption("Sean's game")         

bg = pg.Surface(screen.get_size())
bg = bg.convert()
bg.fill((255,255,255))

rect = [0]*9
rect[0] = pg.draw.rect(bg, ('blue'),[0, 0, 266, 266], 2)
rect[1] = pg.draw.rect(bg, ('blue'),[266, 0, 266, 266], 2)
rect[2] = pg.draw.rect(bg, ('blue'),[533, 0, 266, 266], 2)
rect[3] = pg.draw.rect(bg, ('blue'),[0, 266, 266, 266], 2)
rect[4] = pg.draw.rect(bg, ('blue'),[266, 266, 266, 266], 2)
rect[5] = pg.draw.rect(bg, ('blue'),[533, 266, 266, 266], 2)
rect[6] = pg.draw.rect(bg, ('blue'),[0, 533, 266, 0], 2)
rect[7] = pg.draw.rect(bg, ('blue'),[266, 533, 266, 266], 2)
rect[8] = pg.draw.rect(bg, ('blue'),[533, 266, 266, 266], 2)
screen.blit(bg, (0,0))
pg.display.update()

myboard = [' ']*9
player1Symbol, player2Symbol= ['O','X']
turn = goFirst()
running= True
while running:
    if turn =="player1" :
        for event in pg.event.get():   
            if event.type == pg.QUIT:
                running = False
            else:
                if keyboard.is_pressed('1'):
                    pg.draw.circle(screen,('black'),(130,670),100,10)#1
                    pg.display.update()
                    pos = int(1)
                    goPos(board,player1Symbol,pos)
                    if isWin(board,player1Symbol):
                        tkinter.messagebox.showinfo(title = "GAMEOVER", message = "O WIN!")
                        running = False
                    else:
                        if isFull(myboard):
                            tkinter.messagebox.showinfo(title = "GAMEOVER", message = "TIE!")
                            break
                        else:
                            turn = "player2"
                            
                elif keyboard.is_pressed('2'):
                    pg.draw.circle(screen,('black'),(400,670),100,10)#2
                    pg.display.update()
                    pos = int(2)
                    goPos(board,player1Symbol,pos)
                    if isWin(board,player1Symbol):
                        tkinter.messagebox.showinfo(title = "GAMEOVER", message = "O WIN!")
                        running = False
                    else:
                        if isFull(myboard):
                            tkinter.messagebox.showinfo(title = "GAMEOVER", message = "TIE!")
                            break
                        else:
                            turn = "player2"
                            
                elif keyboard.is_pressed('3'):
                    pg.draw.circle(screen,('black'),(670,670),100,10)#3
                    pg.display.update()
                    pos = int(3)
                    goPos(board,player1Symbol,pos)
                    if isWin(board,player1Symbol):
                        tkinter.messagebox.showinfo(title = "GAMEOVER", message = "O WIN!")
                        running = False
                    else:
                        if isFull(myboard):
                            tkinter.messagebox.showinfo(title = "GAMEOVER", message = "TIE!")
                            break
                        else:
                            turn = "player2"
                            
                elif keyboard.is_pressed('4'):
                    pg.draw.circle(screen,('black'),(130,400),100,10)#4
                    pg.display.update()
                    pos = int(4)
                    goPos(board,player1Symbol,pos)
                    if isWin(board,player1Symbol):
                        tkinter.messagebox.showinfo(title = "GAMEOVER", message = "O WIN!")
                        running = False
                    else:
                        if isFull(myboard):
                            tkinter.messagebox.showinfo(title = "GAMEOVER", message = "TIE!")
                            break
                        else:
                            turn = "player2"
                            
                elif keyboard.is_pressed('5'):
                    pg.draw.circle(screen,('black'),(400,400),100,10)#5
                    pg.display.update()
                    pos = int(5)
                    goPos(board,player1Symbol,pos)
                    if isWin(board,player1Symbol):
                        tkinter.messagebox.showinfo(title = "GAMEOVER", message = "O WIN!")
                        running = False
                    else:
                        if isFull(myboard):
                            tkinter.messagebox.showinfo(title = "GAMEOVER", message = "TIE!")
                            break
                        else:
                            turn = "player2"
                            
                elif keyboard.is_pressed('6'):
                    pg.draw.circle(screen,('black'),(670,400),100,10)#6
                    pg.display.update()
                    pos = int(6)
                    goPos(board,player1Symbol,pos)
                    if isWin(board,player1Symbol):
                        tkinter.messagebox.showinfo(title = "GAMEOVER", message = "O WIN!")
                        running = False
                    else:
                        if isFull(myboard):
                            tkinter.messagebox.showinfo(title = "GAMEOVER", message = "TIE!")
                            break
                        else:
                            turn = "player2"
                            
                elif keyboard.is_pressed('7'):
                    pg.draw.circle(screen,('black'),(130,130),100,10)#7
                    pg.display.update()
                    pos = int(7)
                    goPos(board,player1Symbol,pos)
                    if isWin(board,player1Symbol):
                        tkinter.messagebox.showinfo(title = "GAMEOVER", message = "O WIN!")
                        running = False
                    else:
                        if isFull(myboard):
                            tkinter.messagebox.showinfo(title = "GAMEOVER", message = "TIE!")
                            break
                        else:
                            turn = "player2"
                            
                elif keyboard.is_pressed('8'):
                    pg.draw.circle(screen,('black'),(400,130),100,10)#8
                    pg.display.update()
                    pos = int(8)
                    goPos(board,player1Symbol,pos)
                    if isWin(board,player1Symbol):
                        tkinter.messagebox.showinfo(title = "GAMEOVER", message = "O WIN!")
                        running = False
                    else:
                        if isFull(myboard):
                            tkinter.messagebox.showinfo(title = "GAMEOVER", message = "TIE!")
                            break
                        else:
                            turn = "player2"
                        
                elif keyboard.is_pressed('9'):
                    pg.draw.circle(screen,('black'),(670,130),100,10)#9
                    pg.display.update()
                    pos = int(9)
                    goPos(board,player1Symbol,pos)
                    if isWin(board,player1Symbol):
                        tkinter.messagebox.showinfo(title = "GAMEOVER", message = "O WIN!")
                        running = False
                    else:
                        if isFull(myboard):
                            tkinter.messagebox.showinfo(title = "GAMEOVER", message = "TIE!")
                            break
                        else:
                            turn = "player2"           

    else:
        
        for event in pg.event.get():   
            if event.type == pg.QUIT:
                running = False
            else:
                if keyboard.is_pressed('1'):
                    pg.draw.line(screen,('black'),(50,600),(200,750),10)
                    pg.draw.line(screen,('black'),(200,600),(50,750),10)#1
                    pg.display.update()
                    pos = int(1)
                    goPos(board,player2Symbol,pos)
                    if isWin(board,player2Symbol):
                        tkinter.messagebox.showinfo(title = "GAMEOVER", message = "X WIN!")
                        running = False
                    else:
                        if isFull(myboard):
                            tkinter.messagebox.showinfo(title = "GAMEOVER", message = "TIE!")
                            break
                        else:
                            turn = "player1"
                            
                elif keyboard.is_pressed('2'):
                    pg.draw.line(screen,('black'),(320,600),(470,750),10)
                    pg.draw.line(screen,('black'),(320,750),(470,600),10)#2
                    pg.display.update()
                    pos = int(2)
                    goPos(board,player2Symbol,pos)
                    if isWin(board,player2Symbol):
                        tkinter.messagebox.showinfo(title = "GAMEOVER", message = "X WIN!")
                        running = False
                    else:
                        if isFull(myboard):
                            tkinter.messagebox.showinfo(title = "GAMEOVER", message = "TIE!")
                            break
                        else:
                            turn = "player1"
                            
                elif keyboard.is_pressed('3'):
                    pg.draw.line(screen,('black'),(600,600),(750,750),10)
                    pg.draw.line(screen,('black'),(750,600),(600,750),10)#3
                    pg.display.update()
                    pos = int(3)
                    goPos(board,player2Symbol,pos)
                    if isWin(board,player2Symbol):
                        tkinter.messagebox.showinfo(title = "GAMEOVER", message = "X WIN!")
                        running = False
                    else:
                        if isFull(myboard):
                            tkinter.messagebox.showinfo(title = "GAMEOVER", message = "TIE!")
                            break
                        else:
                            turn = "player1"
                
                elif keyboard.is_pressed('4'):
                    pg.draw.line(screen,('black'),(50,320),(200,470),10)
                    pg.draw.line(screen,('black'),(200,320),(50,470),10)#4
                    pg.display.update()
                    pos = int(4)
                    goPos(board,player2Symbol,pos)
                    if isWin(board,player2Symbol):
                        tkinter.messagebox.showinfo(title = "GAMEOVER", message = "X WIN!")
                        running = False
                    else:
                        if isFull(myboard):
                            tkinter.messagebox.showinfo(title = "GAMEOVER", message = "TIE!")
                            break
                        else:
                            turn = "player1"
                
                elif keyboard.is_pressed('5'):
                    pg.draw.line(screen,('black'),(320,320),(470,470),10)
                    pg.draw.line(screen,('black'),(470,320),(320,470),10)#5
                    pg.display.update()
                    pos = int(5)
                    goPos(board,player2Symbol,pos)
                    if isWin(board,player2Symbol):
                        tkinter.messagebox.showinfo(title = "GAMEOVER", message = "X WIN!")
                        running = False
                    else:
                        if isFull(myboard):
                            tkinter.messagebox.showinfo(title = "GAMEOVER", message = "TIE!")
                            break
                        else:
                            turn = "player1"
                            
                elif keyboard.is_pressed('6'):
                    pg.draw.line(screen,('black'),(600,320),(750,470),10)
                    pg.draw.line(screen,('black'),(750,320),(600,470),10)#6
                    pg.display.update()
                    pos = int(6)
                    goPos(board,player2Symbol,pos)
                    if isWin(board,player2Symbol):
                        tkinter.messagebox.showinfo(title = "GAMEOVER", message = "X WIN!")
                        running = False
                    else:
                        if isFull(myboard):
                            tkinter.messagebox.showinfo(title = "GAMEOVER", message = "TIE!")
                            break
                        else:
                            turn = "player1"
                            
                elif keyboard.is_pressed('7'):
                    pg.draw.line(screen,('black'),(50,50),(200,200),10)
                    pg.draw.line(screen,('black'),(200,50),(50,200),10)#7
                    pg.display.update()
                    pos = int(7)
                    goPos(board,player2Symbol,pos)
                    if isWin(board,player2Symbol):
                        tkinter.messagebox.showinfo(title = "GAMEOVER", message = "X WIN!")
                        running = False
                    else:
                        if isFull(myboard):
                            tkinter.messagebox.showinfo(title = "GAMEOVER", message = "TIE!")
                            break
                        else:
                            turn = "player1"
                            
                elif keyboard.is_pressed('8'):
                    pg.draw.line(screen,('black'),(320,50),(470,200),10)
                    pg.draw.line(screen,('black'),(320,200),(470,50),10)#8
                    pg.display.update()
                    pos = int(8)
                    goPos(board,player2Symbol,pos)
                    if isWin(board,player2Symbol):
                        tkinter.messagebox.showinfo(title = "GAMEOVER", message = "X WIN!")
                        running = False
                    else:
                        if isFull(myboard):
                            tkinter.messagebox.showinfo(title = "GAMEOVER", message = "TIE!")
                            break
                        else:
                            turn = "player1"
                            
                elif keyboard.is_pressed('9'):
                    pg.draw.line(screen,('black'),(600,50),(750,200),10)
                    pg.draw.line(screen,('black'),(600,200),(750,50),10)#9
                    pg.display.update()
                    pos = int(9)
                    goPos(board,player2Symbol,pos)
                    if isWin(board,player2Symbol):
                        tkinter.messagebox.showinfo(title = "GAMEOVER", message = "X WIN!")
                        running = False
                    else:
                        if isFull(myboard):
                            tkinter.messagebox.showinfo(title = "GAMEOVER", message = "TIE!")
                            break
                        else:
                            turn = "player1"
                
pg.quit()
sys.exit();