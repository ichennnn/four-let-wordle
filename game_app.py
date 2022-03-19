#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 21:58:39 2022

@author: ichennnn
"""

# scrap the four letter words
import pandas as pd
import pygame
import random
import nltk
nltk.download('words')
from nltk.corpus import words
import os

pygame.init()

# screen display
color_bg=(160,160,160)
color_green=(0,153,0)
color_orange=(255,128,0)
color_white=(255,255,255)
color_grey=(224,224, 224)
color_dgrey=(128,128,128)

w_font = pygame.font.SysFont('helveticaneue', 56, True)
w_font2 = pygame.font.SysFont('helveticaneue', 24, True)

width = 500
height = 700
screen = pygame.display.set_mode([width, height])
pygame.display.set_caption('four letter w_rdle')

# board where we have 5 tries for the 4 letter ans
board=[[" " for i in range(4)] for j in range(5)]

# speed controls
fps=60
timer = pygame.time.Clock()
turn=0 
curr=0 # current position
can_enter=True # can enter letters into game
game_over=False
streak=0

# random word
path= os.getcwd()
df=pd.read_csv("fourletterwords.csv")
allwords=df.Word
ans = allwords[random.randint(0, len(allwords)-1)]

flag_word= True #yes the guess is a word
menu=True

def start_menu():
    msg1=w_font.render(('Four Letter'), True, color_white)
    screen.blit(msg1, (20, 250))
    msg11=w_font.render('W__rdle', True, color_white)
    screen.blit(msg11, (20, 330))
    img=pygame.image.load('startimg.ico')
    screen.blit(img,(20,490))
    msg2=w_font2.render('built by Irene Chen',True, color_white)
    screen.blit(msg2, (20, 570))
    msg3=w_font2.render('PRESS TAB TO START',True, color_white)
    screen.blit(msg3, (20, 600))
    
def make_board():   
    global turn
    global board
    for row in range(5):
         for col in range(4):
            pygame.draw.rect(screen, color_grey, [ col*125 +17,
                                                  row*125 + 15.5, 90, 90],3, 5)
            letter=w_font.render(board[row][col], True, color_white)
            screen.blit(letter, (col*125+40,row*125+25))

# find_many() finds the positions of letter let in string focus
def find_many(let, focus):
    pos=[i for i in range(len(focus)) if focus[i]==let]
    return pos
        
#check_ans() checks the guess according to Wordle rules
def check_ans():
    global turn
    global board
    global ans
   
    for row in range(5):
         for col in range(4):
            if ans[col] == board[row][col] and turn > row:
                # match 
                pygame.draw.rect(screen, color_green, [ col*125 +17,
                                                       row*125 + 15.5,90, 90],0, 5)
            elif str(board[row][col]) in ans and turn>row:
                if ans.count(board[row][col])==1:
                    if ''.join(board[row]).count(board[row][col])==1:
                        #case: ans=wolf guess=brow
                        pygame.draw.rect(screen, color_orange, [ col*125 + 17,
                                                                  row*125 +15.5, 90, 90],0, 5)
                    else:
                        #case: ans=wolf, guess=pool
                        pos=find_many(ans[col],''.join(board[row]))
                        try:
                            if pos.index(col)<ans.count(board[row][col]):
                                pygame.draw.rect(screen, color_orange, [ col*125 + 17,
                                                                  row*125 +15.5, 90, 90],0, 5)
                        except ValueError:
                            pygame.draw.rect(screen, color_dgrey, [ col*125 + 17,
                                                                  row*125 +15.5, 90, 90],0, 5)
                else:
                    if ''.join(board[row]).count(board[row][col])==1:
                        # case: ans=poll, guess=lays
                        pygame.draw.rect(screen, color_orange, [ col*125 + 17,
                                                                  row*125 +15.5, 90, 90],0, 5)
                    else:
                        #case: ans=pool, guess = odor
                        pos=find_many(ans[col],''.join(board[row]))
                        try:
                            if pos.index(col)<ans.count(board[row][col]):
                                pygame.draw.rect(screen, color_orange, [ col*125 + 17,
                                                                  row*125 +15.5, 90, 90],0, 5)
                        except ValueError:
                            pygame.draw.rect(screen, color_dgrey, [ col*125 + 17,
                                                                  row*125 +15.5, 90, 90],0, 5)
                    
            elif turn > row:
                  pygame.draw.rect(screen, color_dgrey, [ col*125 +17,
                                                         row*125 + 15.5, 90, 90],0, 5)

# win_lose() controls the end game screen and sets gameover  
def win_lose():
    global turn
    global game_over
    global streak
    if game_over:
        streak=+1
        screen.fill(color_bg)
        win1='You won!'
        win1_text=w_font.render(win1, True, color_white)
        screen.blit(win1_text, (50,250))
        win=f"The word was {ans}." 
        win_text=w_font2.render(win, True, color_white)
        screen.blit(win_text, (50, 350))
        new_line_txt="Hit TAB to play again"
        new_line=w_font2.render(new_line_txt, True, color_white)
        new_line_txt2="or SPACE BAR to exit"
        new_line2=w_font2.render(new_line_txt2, True, color_white)
        screen.blit(new_line, (20,630))
        screen.blit(new_line2, (20,650))
    elif turn>=5:
        screen.fill(color_bg)
        lose1='You lost!'
        lose1_text=w_font.render(lose1, True, color_white)
        screen.blit(lose1_text, (50,250))
        lose=f"The word was {ans}." 
        lose_text=w_font2.render(lose, True, color_white)
        screen.blit(lose_text, (50, 350))
        new_line_txt="Hit TAB to play again"
        new_line=w_font2.render(new_line_txt, True, color_white)
        new_line_txt2="or SPACE BAR to exit"
        new_line2=w_font2.render(new_line_txt2, True, color_white)
        screen.blit(new_line, (20,630))
        screen.blit(new_line2, (20,650))
        game_over=True
    

# main loop
running=True
while running:
    timer.tick(fps)
    screen.fill(color_bg)
    if menu:
        start_menu()
    else:
        if flag_word:
            bot_text=w_font2.render('Hit enter after each guess', True, color_white)
            screen.blit(bot_text, (20,620))
        else:
            not_w_text='This is not a word; hit BACKSPACE'
            bot_text=w_font2.render(not_w_text, True, color_orange)
            screen.blit(bot_text, (20,620))
        check_ans()
        make_board()
    
    #event handling
    for event in pygame.event.get():
        #exit
        if event.type == pygame.QUIT:
            running=False
        if event.type == pygame.TEXTINPUT and can_enter and (not game_over):
            entry=event.__getattribute__('text')
            board[turn][curr]=entry
            curr += 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE and curr>0:
                #hit back space and is not at starting curr
                curr-= 1
                board[turn][curr]=' '
            if event.key == pygame.K_TAB and game_over:
                # hit tab  to restart game
                turn = 0
                curr = 0
                game_over=False
                board=[[" " for i in range(4)] for j in range(5)]
                ans = allwords[random.randint(0, len(allwords)-1)]
            if event.key == pygame.K_TAB and menu:
                #exit from start menu and start the game
                screen.fill(color_bg)
                make_board()
                menu=False
                
            if event.key == pygame.K_RETURN and curr >= 4 and (not game_over):
                entry_guess=''.join(board[turn])
                # hit enter after guess 4 letters
                if entry_guess in words.words() or entry_guess in allwords:
                    #is this a word? Yes
                    turn += 1
                    curr = 0
                    flag_word=True
                elif str(entry_guess[-1]) == 's':
                    if entry_guess[0:3] in words.words():
                        turn += 1
                        curr = 0
                        flag_word=True
                    else:
                        flag_word=False
                else:
                    #not a word
                    flag_word=False
            if event.key == pygame.K_SPACE:
                running= False 
                # player wants to exit game
                    
                    
   
    for row in range(5):
        guess = ''.join(board[row])
        if guess ==  ans and row < turn:
            game_over=True
        else:
            game_over= False
            
      
    if curr >= 4:
        can_enter=False
    elif curr < 4:
        can_enter=True
    
    win_lose()
    
    pygame.display.flip()

pygame.quit()

