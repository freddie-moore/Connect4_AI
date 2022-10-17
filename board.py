import pygame.draw
from colours import *

class Board:

    def __init__(self, rows, cols):
        self.board = []
        self.rows = rows
        self.cols = cols
        self.playerturn = 'R'
        self.win = False


    def create_board(self): #creates 6*5 grid, all empty slots represented with 'N'
        for row in range(self.rows):
            self.board.append([])
            for col in range(self.cols):
                self.board[row].append('N')

    def move_made(self, colClicked):  # returns a new board instead of updating existing one for easier implementation of MinMax algorithm
        for i in range(4, -1, -1):
            if self.board[i][colClicked] == 'N':
                self.board[i][colClicked] = self.playerturn  # inserts new piece into board array
                self.count_pieces(self.playerturn)
                break

    def draw_board(self, surface): #draw circles on screen correlating to board array
        for row in range(self.rows): #itereate through board array
            for col in range(self.cols):
                x = 150 + (col * 100) #set x,y pos. 150 = board dist from side, 100 = radius 40 + 60px padding
                y = 250 + (row * 100)
                if self.board[row][col] == 'N':
                    pygame.draw.circle(surface, WHITE, (x, y), 40)
                if self.board[row][col] == 'R':
                    pygame.draw.circle(surface, RED, (x, y), 40)
                if self.board[row][col] == 'B':
                    pygame.draw.circle(surface, BLUE, (x, y), 40)

    def switch_player(self):
        if self.playerturn == 'R':
            self.playerturn = 'B'
        else:
            self.playerturn = 'R'


    def count_pieces(self, colour): #versatile functoin , to determine whether a player has won , and to help AI evaluate the board
        masterList = []
        masterList.append(self.__checkhorizontal(colour))
        masterList.append(self.__checkvertical(colour))
        masterList.append(self.__checkdiagonalleft(colour))
        masterList.append(self.__checkdiagonalright(colour))
        score = 0
        #scoring board algorithm, prioritises highest possible move, then favours moves which build multiple pieces in a row
        for count in masterList:
            if count > score:
                score = (count * 10)
            score += count*count
            if count == 4:
                self.win = True
                score += 100000 #ensures a winning move is taken if possible

        return score

    def evaluate(self): #MINIMAX , blue max , red min
        score = self.count_pieces('B') - self.count_pieces('R')
        print(score)
        return score


    def __checkhorizontal(self, colour):
        highestcount = 0
        for row in self.board: #grab new row
            count = 0 #sets count to 0 for each new row; horizontal lines can't span multiple rows
            for piece in row:  # iterate through individual row
                if piece == colour:
                    count += 1
                    if count > highestcount:
                        highestcount = count
                else:
                    count = 0  # reset count if wrong colour piece encountered



        return highestcount

    def __checkvertical(self, colour):
        highestcount =  0
        for colnum in range(self.cols):  # grab individual column
            count = 0
            for rownum in range(self.rows):  # iterate through each piece in column
                if self.board[rownum][colnum] == colour:
                    count = count + 1
                    if count > highestcount:
                        highestcount = count
                else:
                    count = 0



        return highestcount

    def __checkdiagonalleft(self, colour):  # can also be done recursively ; but more memory intensive
        highestcount = 0
        for row in range(self.rows, 0, -1):  # iterating backwards more efficient + encountered sooner
            for col in range(self.cols, 0, -1):
                piece = self.board[row - 1][col - 1]  # grab initial piece
                if piece == colour:
                    checkleft = True
                    count = 1
                    newrow = row - 1
                    newcol = col - 1
                    while checkleft:  # iterative implementation
                        newrow = newrow - 1  # set row and col num to piece diagonally left
                        newcol = newcol - 1
                        if 0 <= newrow <= 5 and 0 <= newcol <= 5:  # prevents list index out of range
                            piece = self.board[newrow][newcol]
                            if piece == colour:
                                count = count + 1  # increment count if same colour piece found
                                if count > highestcount:
                                    highestcount = count
                            else:
                                count = 0
                                checkleft = False
                        else:  # stop searching , list index out of range
                            count = 0
                            checkleft = False

        return highestcount


    def __checkdiagonalright(self, colour):
        highestcount = 0
        for row in range(self.rows, 0, -1):
            for col in range(self.cols, 0, -1):
                piece = self.board[row - 1][col - 1]
                if piece == colour:
                    checkright = True
                    count = 1
                    newrow = row - 1
                    newcol = col - 1
                    while checkright:
                        newrow = newrow - 1
                        newcol = newcol + 1
                        if 0 <= newrow <= 5 and 0 <= newcol <= 5:
                            piece = self.board[newrow][newcol]
                            if piece == colour:
                                count = count + 1
                                if count > highestcount:
                                    highestcount = count
                            else:
                                count = 0
                                checkright = False
                        else:
                            count = 0
                            checkright = False

        return highestcount

    # recursive 2 function implementation , (PSEUDOCODE, NOT EXACT) , only implemented as a winCheck func, not a count func
    # def iterate_pieces(self):
    #    for row in range(self.rows,0,-1):
    #       for col in range(self.cols,0,-1):
    #          piece = self.board[row-1][col-1]
    #         self.checkdiagonalleft(piece,row-1,col-1,0)

    # def checkdiagonalleft(self,piece,row,col,count):
    #    if count == 4:
    #       return True
    #  else:
    #     if self.board[row-1][col-1] == piece:
    #        self.checkdiagonalleft(self.board[row-1][col-1],row-1,col-1,count + 1)