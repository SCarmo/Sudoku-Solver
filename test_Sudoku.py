from Sudoku import Sudoku
board =[[3,0,6,5,0,8,4,0,0],
        [5,2,0,0,0,0,0,0,0],
        [0,8,7,0,0,0,0,3,1],
        [0,0,3,0,1,0,0,8,0],
        [9,0,0,8,6,3,0,0,5],
        [0,5,0,0,9,0,6,0,0],
        [1,3,0,0,0,0,2,5,0],
        [0,0,0,0,0,0,0,7,4],
        [0,0,5,2,0,6,3,0,0]]

def testSafeRow():
    b = Sudoku()
    b.board = board
    row = 0
    col = 1
    assert not b.safe(row,col,3), "Should not be safe to insert 3 in first row "
    assert b.safe(row,col,1), "Should be safe to insert 1 in first row "

def testSafeCol():
    b = Sudoku()
    b.board = board
    row = 0
    col = 1
    assert not b.safe(row,col,2), "Should not be safe to insert 2 in first column"
    assert b.safe(row,col,1), "Should be safe to insert 1 in first column"

def testSafeBox():
    b = Sudoku()
    b.board = board
    row = 0
    col = 1
    assert not b.safe(row,col,7), "Should not be safe to insert 7 in first box "
    assert b.safe(row,col,1), "Should be safe to insert 1 in first box "





