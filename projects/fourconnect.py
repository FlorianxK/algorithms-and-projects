from typing import *

def dropInColumn(arr:List[List[str]], player:str, column:int) -> Tuple[List[List[str]], int]:
    for i in range(len(arr)-1,-1,-1):
        if arr[i][column] == '.':
            arr[i][column] = player
            break
    return arr,i

def checkWin(arr:List[List[str]], player:str, pos:tuple) -> bool:
    n,m = len(arr[0]),len(arr)
    dir = [ (0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1) ]
    x,y = pos
    for dx,dy in dir:
        count = 0
        nx,ny = x,y
        while arr[nx][ny] == player:
            count += 1
            nx,ny = nx+dx,ny+dy
            if count == 4:
                return True
            elif 0 > nx or nx >= m or 0 > ny or ny >= n:
                break
    return False

def printArr(arr:List[List[str]]) -> None:
    for a in arr:
        print(' '.join(a))

def main() -> None:
    print("Hello")
    row,column = 6,7
    arr = [['.']*column for _ in range(row)]
    filledColumn = [0]*column
    moves = 1
    print("Type which player starts: X or O: ", end='')
    player = input()
    while player != 'X' and player != 'O':
        print("Wrong input - type X or O: ", end='')
        player = input()

    while True:
        correctMove = True
        printArr(arr)
        print(f"Choose 1-7 from left to right to drop {player} into the column: ", end='')
        move = input()
        i = 0
        if move.isnumeric():
            val = int(move)
            if 1 <= val and val <= 7:
                if filledColumn[val-1] < 6:
                    arr,i = dropInColumn(arr,player,val-1)
                    filledColumn[val-1] += 1
                else:
                    print("Column is already full! Choose a free one!")
                    correctMove = False
            else:
                print("Number has to be between 1-7!")
                correctMove = False
        else:
            print("Input is not a number!")
            correctMove = False

        if correctMove:
            if checkWin(arr,player,(i,int(move)-1)):
                printArr(arr)
                print(f"Player {player} won the game!")
                break

            if moves == row*column:
                printArr(arr)
                print("DRAW - no winner!")
                break
            moves += 1

            if player == 'X':
                player = 'O'
            elif player == 'O':
                player = 'X'

if __name__=="__main__":
    main()