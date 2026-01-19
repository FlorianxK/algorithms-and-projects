from typing import *

def printArr(arr:List[List[str]]) -> None:
    print("-------------------------")
    for i in range(9):
        for j in range(9):
            if arr[i][j] is not None:
                if j == 0:
                    print("|", end=" ")
                print(f"{arr[i][j]} ", end="")
            if (j + 1) % 3 == 0:
                print("|", end=" ")
        if (i + 1) % 3 == 0:
            print("\n-------------------------", end=" ")
        print()

#If soduku is solved add flag True
def isValidSudoku(board: List[List[str]],solved=False) -> bool:
    res = []
    for i in range(9):
        for j in range(9):
            element = board[i][j]
            if element != '.':
                res += [(i, element), (element, j), (i // 3, j // 3, element)]
            elif solved:
                return False
    return len(res) == len(set(res))

def solveSudoku(board: list[list[str]]) -> None:
    cell, n = 3, 9
    rows = [[0] * (n + 1) for _ in range(n)]
    cols = [[0] * (n + 1) for _ in range(n)]
    boxes = [[0] * (n + 1) for _ in range(n)]
    sudokuSolved = False

    def couldPlace(d, row, col):
        idx = (row // cell) * cell + col // cell
        return rows[row][d] + cols[col][d] + boxes[idx][d] == 0

    def placeNumber(d, row, col):
        idx = (row // cell) * cell + col // cell
        rows[row][d] += 1
        cols[col][d] += 1
        boxes[idx][d] += 1
        board[row][col] = str(d)

    def removeNumber(d, row, col):
        idx = (row // cell) * cell + col // cell
        rows[row][d] -= 1
        cols[col][d] -= 1
        boxes[idx][d] -= 1
        board[row][col] = '.'

    def placeNextNumbers(row, col):
        nonlocal sudokuSolved
        if row == n - 1 and col == n - 1:
            sudokuSolved = True
        elif col == n - 1:
            backtrack(row + 1, 0)
        else:
            backtrack(row, col + 1)

    def backtrack(row, col):
        nonlocal sudokuSolved
        if board[row][col] == '.':
            for d in range(1, 10):
                if couldPlace(d, row, col):
                    placeNumber(d, row, col)
                    placeNextNumbers(row, col)
                    if not sudokuSolved:
                        removeNumber(d, row, col)
        else:
            placeNextNumbers(row, col)

    for i in range(n):
        for j in range(n):
            if board[i][j] != '.':
                placeNumber(int(board[i][j]), i, j)
    backtrack(0, 0)

def generateEasyBoard():
    board = [['9','.','.','5','.','8','.','.','7'],
             ['.','8','.','3','.','7','9','.','5'],
             ['.','5','4','.','.','.','.','8','.'],
             ['.','7','.','6','8','.','.','3','2'],
             ['1','.','.','.','.','4','.','.','8'],
             ['5','.','.','2','1','9','.','6','.'],
             ['.','.','.','9','.','6','.','.','1'],
             ['7','2','6','.','.','1','.','4','.'],
             ['.','.','1','4','7','.','.','5','6']]
    return board

def generateHardBoard():
    board = [['5','3','.','.','7','.','.','.','.'],
             ['6','.','.','1','9','5','.','.','.'],
             ['.','9','8','.','.','.','.','6','.'],
             ['8','.','.','.','6','.','.','.','3'],
             ['4','.','.','8','.','3','.','.','1'],
             ['7','.','.','.','2','.','.','.','6'],
             ['.','6','.','.','.','.','2','8','.'],
             ['.','.','.','4','1','9','.','.','5'],
             ['.','.','.','.','8','.','.','7','9']]
    return board

def main() -> None:
    print("Hello")
    
    hard = generateHardBoard()
    printArr(hard)
    print(isValidSudoku(hard,True))
    solveSudoku(hard)
    printArr(hard)
    print(isValidSudoku(hard,True))

if __name__=="__main__":
    main()