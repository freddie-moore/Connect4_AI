class Board:
    def __init__(self):
        self.win = False
        self.draw = False
        self.board = [[" "] * 7 for _ in range(5)]
        self.playerturn = "R"
        self.turnCount = 0
        self.bestCol = 0

    #finds bottom-most available position in specified column, returns False if no move in column
    def moveMade(self, col):
            if 0 <= col <= 6:
                for row in range(1, 6):
                    if self.board[-row][col] == " ":
                        self.board[-row][col] = self.playerturn
                        self.turnCount += 1
                        self.__checkGameState()
                        self.evalBoard()
                        self.changeTurn()
                        return True, (-row + len(self.board))

            return False, None

    def changeTurn(self):
        if self.playerturn == "R":
            self.playerturn = "Y"
        else:
            self.playerturn = "R"

    def __checkGameState(self):
        if self.__checkWinVert() or self.__checkWinHoz() or self.__checkWinDiag():
            self.win = True
        if self.turnCount == 35:
            self.draw = True

    #check for 4 in a row diagonally
    def __checkWinDiag(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if self.board[row][col] == self.playerturn:
                    if row + 3 < len(self.board) and col + 3 < len(self.board[0]) and \
                            self.board[row + 1][col + 1] == self.playerturn and \
                            self.board[row + 2][col + 2] == self.playerturn and \
                            self.board[row + 3][col + 3] == self.playerturn:
                        return True
                    if row + 3 < len(self.board) and col - 3 >= 0 and \
                            self.board[row + 1][col - 1] == self.playerturn and \
                            self.board[row + 2][col - 2] == self.playerturn and \
                            self.board[row + 3][col - 3] == self.playerturn:
                        return True
        return False

    #check for 4 in a row in a straight or horizontal line
    def __countPiecesWin(self, start_row, start_col, rowInc, colInc):
        count = 0
        while 0 <= start_row < len(self.board) and 0 <= start_col < len(self.board[0]):
            if self.board[start_row][start_col] == self.playerturn:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0
            start_row += rowInc
            start_col += colInc
        return False

    def __checkWinVert(self):
        for col in range(len(self.board[0])):
            if self.__countPiecesWin(0, col, 1, 0):
                return True
        return False

    def __checkWinHoz(self):
        for row in range(len(self.board)):
            if self.__countPiecesWin(row, 0, 0, 1):
                return True
        return False

    #evaluate state of board
    def evalBoard(self):
        rScore = 0
        for score in self.__EvalDiag("R"):
            rScore += score**10
        for row in range(len(self.board)):
            for score in self.__EvalRows("R", 0, row, 1):
                rScore += score**10
        for row in range(len(self.board)):
            for score in self.__EvalRows("R", 6, row, -1):
                rScore += score**10
        for col in range(len(self.board[0])):
            for score in self.__EvalVert("R", col):
                rScore += score**10

        yScore = 0

        for score in self.__EvalDiag("Y"):
            yScore += score**10
        for row in range(len(self.board)):
            for score in self.__EvalRows("Y", 0, row, 1):
                yScore += score**10
        for row in range(len(self.board)):
            for score in self.__EvalRows("Y", 6, row, -1):
                yScore += score**10
        for col in range(len(self.board[0])):
            for score in self.__EvalVert("Y", col):
                yScore += score**10

        return yScore - rScore

#count every piece in some sort of horizontal line, that has the possibility to develop into a win
    def __EvalRows(self, player, startCol, startRow, step):
        counts = []
        curRow = startRow
        absCol = startCol

        #abs(StartCol-absCol) used to ensure we only consider the first 4 columns,\
        # as these are the only possible ones to build 4 in a row off
        while 0 <= startRow < (len(self.board)) and 0 <= startCol < len(self.board[0]) and abs(startCol-absCol) < 4:
            count = 0
            curCol = startCol
            if self.board[curRow][curCol] == player:
                while 0 <= curRow < len(self.board) and 0 <= curCol < len(self.board[0]) and abs(startCol-curCol) < 4:
                    if self.board[curRow][curCol] == player:
                        count += 1
                    elif self.board[curRow][curCol] == " " and (curRow == 4 or self.board[curRow+1][curCol] != " "):
                        pass
                    else:
                        count = 0
                        break

                    curCol += step

                counts.append(count)
            startCol += step

        return counts

    # count every piece in some sort of vertical line, that has the possibility to develop into a win
    def __EvalVert(self, player, col):
        counts = []
        for row in range(3,5):
            count = 0
            if self.board[row][col] == player:
                for piece in range(0,4):
                    if self.board[row-piece][col] == player:
                        count += 1
                        if count == 4:
                            break
                    else:
                        count = 0
                        break
                counts.append(count)

        return counts

    # count every piece in some sort of diagonal line, that has the possibility to develop into a win
    def __EvalDiag(self, player):
        counts = []
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if self.board[row][col] == player:
                    count = 0
                    if row - 3 >= 0 and col - 3 >= 0:
                        for p in range(4):
                            if self.board[row-p][col-p] == player:
                                count += 1
                            elif self.board[row-p][col-p] == " ":
                                pass
                            else:
                                count = 0
                                break
                        counts.append(count)

                    count = 0
                    if row - 3 >= 0 and col + 3 < len(self.board[0]):
                        for p in range(4):
                            if self.board[row - p][col + p] == player:
                                count += 1
                            elif self.board[row - p][col + p] == " ":
                                pass
                            else:
                                count = 0
                                break
                        counts.append(count)


        return counts

