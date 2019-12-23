from random import randint
import pygame as pg

pg.init()

# Sets size of grid
WINDOWSIZE = 810 # needs to be multiple of 9
WINDOWWIDTH = WINDOWSIZE
WINDOWHEIGHT = WINDOWSIZE
SQUARESIZE = WINDOWSIZE // 3 # size of a 3x3 square
CELLSIZE = SQUARESIZE // 3 # Size of a cell
NUMBERSIZE = CELLSIZE // 3 # Position of unsolved number

size = (WINDOWWIDTH,WINDOWHEIGHT)
SCREEN = pg.display.set_mode(size)
pg.display.set_caption('Sudoku Solver')

# Set up the colours
BLACK   = (0,0,0)
WHITE   = (255,255,255)
GREY    = (200,200,200)

# fonts
FONT = pg.font.Font('freesansbold.ttf', 55)

class Sudoku:

    def __init__(self):
        # 0 value indicates blank space
        self.board = [[0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0]]

        self.generateBoard()

    def generateBoard(self):
        ## Make a valid sudoku board

        # 1. generate first row
        validRow = [1,2,3,4,5,6,7,8,9]
        for i in range(0,9):
            randPos = randint(1,9) - 1
            validRow[i], validRow[randPos] = validRow[randPos], validRow[i]

        # 2. further rows are simply a rotation of the first row
        for i in range(0,9,3):
            for j in range(i, i+3):
                self.board[j] = validRow
                validRow = validRow[3:] + validRow[:3]
            validRow = self.board[i]
            validRow = validRow[1:] + validRow[:1]

        # 3. insert blanks for the puzzle aspect
        self.insertBlanks()

    def prettyPrint(self):
        for row in self.board:
            print(row)

    def insertBlanks(self):
        # fill approx. half the board with blanks
        for _ in range(40):
            row = randint(0,8)
            col = randint(0,8)
            while self.board[row][col] == 0:
                row = randint(0,8)
                col = randint(0,8)
            self.board[row][col] = 0


    def safe(self, row, col, num):
        # check row
        for c in self.board[row]:
            if c == num:
                return False

        # check col
        for r in self.board:
            if r[col] == num:
                return False

        # check box
        firstRow = row - (row % 3)
        firstCol = col - (col % 3)

        for r in range(firstRow, firstRow+3):
            for c in range(firstCol, firstCol+3):
                if self.board[r][c] == num:
                    return False

        # if row col and box don't contain num then return true
        return True

    # Backtracking algorithm used to solve the sudoku board
    def solveBoard(self):
        # find row, col of unnassigned cell
        row = -1
        col = -1
        found = False

        for i in range(0,9):
            for j in range(0,9):
                if self.board[i][j] == 0:
                    row = i
                    col = j
                    found = True
                    break
            if found:
                break

        # if there is none return true
        if not found:
            return True

        # for digits from 1 to 9
        for i in range(1,10):
            # - if no conflict for digit at row, col then assign and recursively fill rest of board
            if self.safe(row, col, i):
                self.board[row][col] = i
                # - if recursion successful return true
                if self.solveBoard():
                    return True
                # - else remove digit and try another number
                else:
                    self.board[row][col] = 0

        # if all digits tried and no result, return false
        return False

    def setBoard(self, arr):
        self.board = arr

# draw the sudoku grid
def drawGrid():
    # draw minor line
    for x in range(0, WINDOWWIDTH, CELLSIZE): # vertical lines
        pg.draw.line(SCREEN, GREY, (x,0), (x,WINDOWHEIGHT))

    for y in range(0, WINDOWHEIGHT, CELLSIZE): # horizontal lines
        pg.draw.line(SCREEN, GREY, (0,y), (WINDOWWIDTH,y))

    # draw major lines
    for x in range(0, WINDOWWIDTH, SQUARESIZE): # vertical lines
        pg.draw.line(SCREEN, BLACK, (x,0), (x,WINDOWWIDTH))

    for y in range(0, WINDOWHEIGHT, SQUARESIZE): # horizontal lines
        pg.draw.line(SCREEN, BLACK, (0,y), (WINDOWHEIGHT,y))


def drawNumbers():
    text = FONT.render('*numbers*', True, BLACK)
    textRect = text.get_rect()
    textRect.center = (400,400)
    SCREEN.blit(text, textRect)

if __name__ == "__main__":
    b = Sudoku()
    b.prettyPrint()
    print(b.solveBoard())
    b.prettyPrint()

    run = True

    # Main game loop
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        SCREEN.fill(WHITE)

        drawGrid()
        drawNumbers()


        pg.display.update()


