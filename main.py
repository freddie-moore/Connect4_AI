import pygame
from consts import *
from board import Board
from copy import deepcopy
from minimax import minimax
import time
from statistics import mean

pygame.init()
board = Board()

# initialise key variables for the game
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(LBLUE)
board = Board()


# draws the initial empty board on screen
def draw_board():
    for row in range(0, 5):
        y = SIZE + SPACING + (row * SPACING) + (row * SIZE * 2)
        for col in range(0, 7):
            x = SIZE + SPACING + (col * SPACING) + (col * SIZE * 2)
            pygame.draw.circle(screen, DBLUE, (x, y), SIZE)
    pygame.display.flip()


# function draws each new entry in the board, onto the screen
def updateBoard(row, col):
    y = SIZE + SPACING + (row * SPACING) + (row * SIZE * 2)
    x = SIZE + SPACING + (col * SPACING) + (col * SIZE * 2)

    if board.board[row][col] == "R":
        colour = RED
    else:
        colour = YELLOW
    pygame.draw.circle(screen, colour, (x, y), SIZE)


def main():
    run = True
    draw_board()

    while run:
        for event in pygame.event.get():
            # check for quit
            if event.type == pygame.QUIT:
                pygame.quit()

            # takes player input
            if event.type == pygame.MOUSEBUTTONDOWN and board.win == False and board.draw == False:  # and not board.draw and not board.win:
                pos = pygame.mouse.get_pos()
                col = pos[0] // (SPACING + SIZE * 2)
                res = board.moveMade(col)
                #only progress to AI move if player move was a success
                if res[0]:
                    #draw player move on screen
                    updateBoard(res[1], col)
                    pygame.display.flip()
                    # AI MOVE
                    # TIMING LOOP TO INVESTIGATE EFFICIENCY

                bestmove = deepcopy(minimax(board, 5, float('-inf'), float('+inf'), True)[1])
                res = board.moveMade(bestmove.bestCol)
                if res[0]:
                    updateBoard(res[1], bestmove.bestCol)
                    pygame.display.flip()

            #checking game state
            elif board.win:
                print("WINNER")
            elif board.draw:
                print("DRAW")



main()