import pygame
pygame.init()


class Piece:

    def __init__(self, row, col, colour):
        self.row = row
        self.col = col
        self.colour = colour
        self.boardtopx = 150
        self.boardtopy = 250
        self.x = self.boardtopx + (row * 100)  #ensures centre positioning in each cell on board
        self.y = self.boardtopy + (col * 100)


    def draw(self, win):
        pygame.draw.circle(win, self.colour, (self.x, self.y), 40)