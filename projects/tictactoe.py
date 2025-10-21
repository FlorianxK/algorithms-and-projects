from typing import *

def setField(arr:List[List[str]], field:tuple, player:str) -> List[List[str]]:
    j,i = field
    arr[i][j] = player
    return arr

def checkWin(arr:List[List[str]], player:str) -> bool:
    n = len(arr)
    for i in range(n):
        #row check
        count = 0
        for j in range(n):
            if arr[i][j] == player:
                count += 1
        if count == 3:
            return True
        
        #column check
        count = 0
        for j in range(n):
            if arr[j][i] == player:
                count += 1
        if count == 3:
            return True
    
    #cross check
    c1,c2 = 0,0
    f,s = 0,n-1
    for i in range(n):
        if arr[i][f] == player:
            c1 += 1
        if arr[i][s] == player:
            c2 += 1
        f += 1
        s -= 1

    if c1 == 3 or c2 == 3:
        return True
    
    return False

def printArr(arr:List[List[str]]) -> None:
    for a in arr:
        print(' '.join(a))

def main() -> None:
    print("Hello")
    arr = [['.']*3 for _ in range(3)]
    moves = 1
    filled = set()
    h = {'1': (0,0), '2': (1,0), '3': (2,0), '4': (0,1), '5': (1,1), '6': (2,1), '7': (0,2), '8': (1,2), '9': (2,2)}
    print("Type which player starts: X or O: ", end='')
    player = input()
    while player != 'X' and player != 'O':
        print("Wrong input - type X or O: ", end='')
        player = input()

    while True:
        printArr(arr)
        print(f"Choose 1-9 from left to right to set {player}: ", end='')
        move = input()
        correctMove = True
        if move in h:
                if h[move] not in filled:
                    arr = setField(arr, h[move], player)
                    filled.add(h[move])
                else:
                    print("Field already filled! Choose a free one!")
                    correctMove = False
        else:
            print("Incorrect move!")
            correctMove = False

        if correctMove:
            if checkWin(arr,player):
                printArr(arr)
                print(f"Player {player} won the game!")
                break

            if moves == 9:
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