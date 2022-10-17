# import all libraries , classes and variables
import pygame
import copy
from board import Board
from colours import *
from constants import *


#initialise pygame, instantiate board objects and create screen
pygame.init()
runGame = True
screen = pygame.display.set_mode((WIDTH, HEIGHT))
myBoard = Board(5,6)

#create 5*6 board with empty cells
myBoard.create_board()

#minimax algorithm; recursive
def minimax(board,depth,player):
    if depth == 0:
        return board.evaluate(), board.board

    if player == 'B': #max player
        maxEval = float('-inf')
        bestmove = None
        for move in getMoves(board, player):
            evaluation = minimax(move, depth-1, 'R')[0]
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                bestmove = move

        return maxEval,bestmove


    else: #min player
        minEval = float('+inf')
        bestmove = None
        for move in getMoves(board, player):
            evaluation = minimax(move, depth-1, 'B')[0]
            minEval = min(minEval, evaluation)
            print(minEval)
            if minEval == evaluation:
                bestmove = move

        return minEval, bestmove

def getMoves(board): #return a new board for scoring based off each possible move
    moves = []

    for move in range(COLS):
        temp_board = copy.deepcopy(board) #ensures not working off a reference
        new_board = temp_board
        new_board.move_made(move)
        moves.append(new_board)

    return moves




def whatColClicked(pos): #returns col integer based of mouse x co-ord
    if 100 < pos < 700:
        return (pos // 100) - 1


def main():
    #draw all elements initially
    screen.fill(WHITE)  # background
    pygame.draw.rect(screen, BLACK, (100, 200, 600, 500))  # grid base
    myBoard.draw_board(screen)  # board
    while runGame: #main game loop

        #Delete this if statement to make a two player game.
        if myBoard.playerturn == 'B' and not myBoard.win:
            score, new_board = minimax(myBoard, 4,'B') #call minimax , tree depth of 4
            myBoard.board = new_board.board
            myBoard.draw_board(screen)
            myBoard.switch_player()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN and not myBoard.win: #if player input
                pos = pygame.mouse.get_pos()
                myBoard.move_made(whatColClicked(pos[0])) #update board to the new one returned by move_made()
                myBoard.switch_player()
                myBoard.draw_board(screen)  # redraw board with new changes
            if event.type == pygame.MOUSEBUTTONDOWN and myBoard.win:
                print('GAME OVER')

            pygame.display.flip() #update display

main() #start game