from Sudoku import Sudoku

if __name__ == "__main__":
    b = Sudoku()
    b.prettyPrint()
    print(b.solveBoard())
    b.prettyPrint()

