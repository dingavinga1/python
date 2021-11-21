import time


print("------------WELCOME TO TIC-TAC-TOE-------------")
time.sleep(1.5)
print("\n"*100)
print("----------------LETZ GOOOOOOOOOO-----------------")
time.sleep(1)
print("\n"*100)


boardarr=[]
for row in range(3):
    boardarr.append([])
    for column in range(3):
        boardarr[row].append(" ")


def board():
    print("\n"*100)
    print("  _TIC-TAC-TOE_")
    print("\n")
    print("\n", boardarr[0], "\n",boardarr[1], "\n",boardarr[2])
    print("\n")
    print("Player 1 is 'X' \nPlayer 2 is 'O'\n")
board()


def works(turnhaha):
    global posr, posc
    boardarr[posr][posc]=turnhaha


def game(player):
    global turn, posr, posc
    if player==True:
        turn="X"
        print("It's player 1's turn")
    else:
        turn="O"
        print("It's player 2's turn")
    correct=False
    while correct!=True:
        try:
            try:
                print("enter row you want to input to")
                posr=int(input())-1
                print("enter column you want to input to")
                posc=int(input())-1
            except ValueError:
                board()
                print("You didn't enter a number. Please enter again.\n")
                continue
            if boardarr[posr][posc] == " ":
                if (posc+1)<=0 or (posr+1)<=0:
                    board()
                    print("Position doesn't exist. Please enter again\n")
                    continue
                else:
                    correct=True
                    break
            else:
                board()
                print("Position already being used. Enter valid position.\n")
        except IndexError:
            board()
            print("Position doesn't exist. Please enter again\n")
    works(turn)
    board()
    
player1=True
win=False
draw=False


while win!=True:
    game(player1)
    countd = 0
    for r in range(3):
        countc, countr=0, 0
        for c in range(3):
            if boardarr[r][c] == turn:
                countc+=1
            if boardarr[c][r] == turn: 
                countr+=1
            if r==c:
               if boardarr[r][c] == turn:
                   countd+=1
            if countr==3 or countc==3:
                win=True
                break
        if win==True:
            break
    if countd==3:
        win=True
    if boardarr[2][0]==turn and boardarr[0][2]==turn and boardarr[1][1]==turn:
        win=True
    if win==True:
        if player1==True:
            print("THREE IN A ROW\nPLAYER 1 WINSSSSSSS")
            break
        else:
            print("THREE IN A ROW\nPLAYER 2 WINSSSSSSS")
            break
    countel=0
    for row in boardarr:
        countel+=row.count("X")
        countel+=row.count("O")
    if countel==9:
        draw=True
    if player1==True:
        player1=False
    else: 
        player1=True


if draw==True:
    print("ISSA DRAW. BETTER LUCK NEXT TIME ")