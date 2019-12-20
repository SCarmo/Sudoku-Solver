from random import randint

class Sudoku:
    def generatePuzzle(self):
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

        # 3. Remove some numbers


    def __init__(self):
        self.board = [[0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0]]

        self.generatePuzzle()

    def prettyPrint(self):
        for row in self.board:
            print(row)

    def check_box(self, col, row):
        rowMin = (row // 3) * 3
        colMin = (col // 3) * 3




if __name__ == "__main__":
    b = Sudoku()
    b.prettyPrint()






