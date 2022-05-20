#impot liberary 
import copy
import sys
import pygame as pygame 
import random
import numpy as np
#import const value from constant file 
from constant import *

# --- pygame SETUP ---
#initit pygame 
pygame.init()
screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption('Habiba Mohab Tamer AI project ')
screen.fill( BG_COLOR )

# --- CLASSES ---

class Board:

    def __init__(self):
        self.squares = np.zeros( (ROWS, COLS) )
       

    def mark_sqr(self, row, col, player):
        self.squares[row][col] = player

    def empty_sqr(self, row, col):
        return self.squares[row][col] == 0

class Game:

    def __init__(self):
        self.board = Board()
        self.player = 1   #1-cross  #2-circles
        self.show_lines()

    # --- DRAW METHODS ---

    def show_lines(self):
        # bg
        screen.fill( BG_COLOR )

        # vertical
        pygame.draw.line(screen, LINE_COLOR, (SQSIZE, 0), (SQSIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (WIDTH - SQSIZE, 0), (WIDTH - SQSIZE, HEIGHT), LINE_WIDTH)

        # horizontal
        pygame.draw.line(screen, LINE_COLOR, (0, SQSIZE), (WIDTH, SQSIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (0, HEIGHT - SQSIZE), (WIDTH, HEIGHT - SQSIZE), LINE_WIDTH)

    def draw_fig(self, row, col):
        if self.player == 1:
            # draw cross
            # desc line
            start_desc = (col * SQSIZE + OFFSET, row * SQSIZE + OFFSET)
            end_desc = (col * SQSIZE + SQSIZE - OFFSET, row * SQSIZE + SQSIZE - OFFSET)
            pygame.draw.line(screen, CROSS_COLOR, start_desc, end_desc, CROSS_WIDTH)
            # asc line
            start_asc = (col * SQSIZE + OFFSET, row * SQSIZE + SQSIZE - OFFSET)
            end_asc = (col * SQSIZE + SQSIZE - OFFSET, row * SQSIZE + OFFSET)
            pygame.draw.line(screen, CROSS_COLOR, start_asc, end_asc, CROSS_WIDTH)
        
        elif self.player == 2:
            # draw circle
            center = (col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2)
            pygame.draw.circle(screen, CIRC_COLOR, center, RADIUS, CIRC_WIDTH)

    # --- OTHER METHODS ---


    def next_turn(self):
        self.player = self.player % 2 + 1

def main():

    # --- OBJECTS ---

    game = Game()
    board = game.board

    # --- MAINLOOP ---

    while True:
        
        # pygame events
        for event in pygame.event.get():

            # quit event
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # click event
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                row = pos[1] // SQSIZE
                col = pos[0] // SQSIZE
                
                if board.empty_sqr(row,col):
                    board.mark_sqr(row , col , game.player)
                    game.draw_fig(row,col)
                    game.next_turn()

        # AI initial call

            # update the screen
            pygame.display.update()

            

main()