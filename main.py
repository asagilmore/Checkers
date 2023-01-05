import time
import sys

from function import type

board = [[0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0],
         [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 2, 0, 2, 0, 2, 0, 2], [2, 0, 2, 0, 2, 0, 2, 0]]
21
screen = [[0, 2, 0, 2, 0, 2, 0, 2], [2, 0, 2, 0, 2, 0, 2, 0],
          [0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0],
          [0, 6, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0],
          [0, 4, 0, 4, 0, 4, 0, 4], [4, 0, 4, 0, 4, 0, 4, 0]]

#0=greyed out 1= empty 2=green 3=green selected 4= red 5= red selected


def draw():
    sys.stdout.write("\x1b[2J\x1b[H")
    num = 1
    for row in screen:
        sys.stdout.write("\033[0;37;39m" + str(num) + " ")
        for x in row:
            if x == 0:
                sys.stdout.write("\033[0;37;39m" + "▧")
            elif x == 1:
                sys.stdout.write("\033[0;37;39m" + "▢")
            elif x == 2:
                sys.stdout.write("\033[0;32;40m" + "▣")
            elif x == 3:
                sys.stdout.write("\033[0;32;42m" + "▣")
            elif x == 4:
                sys.stdout.write("\033[0;31;40m" + "▣")
            elif x == 5:
                sys.stdout.write("\033[0;31;41m" + "▣")
            elif x == 6:
                sys.stdout.write("\033[0;32;40m" + "▢")
            elif x == 7:
                sys.stdout.write("\033[0;31;40m" + "▢")
            sys.stdout.write(" ")
        num = num + 1
        sys.stdout.write("\n")
    sys.stdout.write("  1 2 3 4 5 6 7 8\n")


def setScreen():
    countRow = 0
    for row in board:
        countCollumn = 0
        for collumn in row:
            if int(board[countRow][countCollumn]) == 1:
                screen[countRow][countCollumn] = 2
            elif int(board[countRow][countCollumn]) == 2:
                screen[countRow][countCollumn] = 4
            else:
                if (countRow % 2) == 0 or countRow == 0:
                    if (countCollumn % 2) == 0 or countCollumn == 0:
                        screen[countRow][countCollumn] = 0
                    else:
                        screen[countRow][countCollumn] = 1
                else:
                    if (countCollumn % 2) == 0 or countCollumn == 0:
                        screen[countRow][countCollumn] = 1
                    else:
                        screen[countRow][countCollumn] = 0
            countCollumn += 1
        countRow += 1


def selectPiece(player):
    type("\nplayer:" + str(player) + " select piece (row,collumn Ie. '3 6')\n")
    selection = input("")  # set selection
    try:
        row = (int(selection[0]) - 1)
        collumn = (int(selection[-1]) - 1)
    except ValueError:
        type("that is not on the board")
        return (selectPiece(player))
    if row > 7 or collumn > 7 or row < 0 or collumn < 0:
        type("error, that selection is out of the range")
        selectPiece(player)
        return ()
    else:
        if board[row][collumn] == player:
            screen[row][collumn] += 1
            selection = [row, collumn]
            return (selection)
        else:
            type("error, that is not your peice, please try again")
            return (selectPiece(player))


def getMoves1(row, collumn):
    moves = []
    #check left
    if (row + 1) <= 7:
        if (collumn - 1) >= 0:
            if board[row + 1][collumn - 1] == 0:
                screen[row + 1][collumn - 1] = 6
                moves.append([(row + 1), (collumn - 1)])
            if (row + 2) <= 7:
                if board[row + 1][collumn -
                                  1] == 2 and board[row + 2][collumn - 2] == 0:
                    screen[row + 2][collumn - 2] = 6
                    moves.append([(row + 2), (collumn - 2)])

    #check right
        if (row + 1) <= 7:
            if (collumn + 1) <= 7:
                if board[row + 1][collumn + 1] == 0:
                    screen[row + 1][collumn + 1] = 6
                    moves.append([(row + 1), (collumn + 1)])
                if (row + 2) <= 7:
                    if board[row + 1][collumn + 1] == 2 and board[row +
                                                                  2][collumn -
                                                                     2] == 0:
                        screen[row + 2][collumn + 2] = 6
                        moves.append([(row + 2), (collumn + 2)])
    return (moves)


def getMoves2(row, collumn):
    moves = []
    #check left
    if (row - 1) >= 0:
        if (collumn - 1) >= 0:
            if board[row - 1][collumn - 1] == 0:
                screen[row - 1][collumn - 1] = 7
                moves.append([(row - 1), (collumn - 1)])
            if (row - 2) >= 0:
                if board[row - 1][collumn -
                                  1] == 1 and board[row - 2][collumn - 2] == 0:
                    screen[row - 2][collumn - 2] = 7
                    moves.append([(row - 2), (collumn - 2)])

    #check right
        if (row - 1) >= 0:
            if (collumn + 1) <= 7:
                if board[row - 1][collumn + 1] == 0:
                    screen[row - 1][collumn + 1] = 7
                    moves.append([(row - 1), (collumn + 1)])
                if (row - 2) >= 0:
                    if board[row - 1][collumn + 1] == 1 and board[row -
                                                                  2][collumn -
                                                                     2] == 0:
                        screen[row - 2][collumn + 2] = 7
                        moves.append([(row - 2), (collumn + 2)])
    return (moves)


def askmove(player, moves):
    i = 1
    type("select move player " + str(player))
    for move in moves:
        type(", " + str(i) + ":(" + str(int(move[0]) + 1) + "," +
             str(int(move[1]) + 1) + ")")
        i += 1
    return (int(input("\n")) - 1)


def turnP1():
    setScreen()
    draw()

    killed = False
    select1 = selectPiece(1)
    moves1 = getMoves1(select1[0], select1[1])

    draw()

    move1 = moves1[askmove(1, moves1)]

    if (abs(move1[0] - select1[0]) > 1):  #check if move jumps selectPiece
        #check if board spot = 2, set to 0
        if int(board[int((move1[0] + select1[0]) / 2)][int(
            (move1[1] + select1[1]) / 2)]) == 2:
            board[int((move1[0] + select1[0]) / 2)][int(
                (move1[1] + select1[1]) / 2)] = 0
            killed = True
    #double check move position, move there, remove old piece
    if int(board[move1[0]][move1[1]]) == 0:
        board[select1[0]][select1[1]] = 0
        board[move1[0]][move1[1]] = 1
        return (killed)


def turnP2():
    setScreen()
    draw()

    killed = False
    select1 = selectPiece(2)
    moves1 = getMoves2(select1[0], select1[-1])

    draw()

    move1 = moves1[askmove(2, moves1)]

    if (abs(move1[0] - select1[0]) > 1):  #check if move jumps selectPiece
        #check if board spot = 2, set to 0
        if int(board[int((move1[0] + select1[0]) / 2)][int(
            (move1[1] + select1[1]) / 2)]) == 1:
            board[int((move1[0] + select1[0]) / 2)][int(
                (move1[1] + select1[1]) / 2)] = 0
            killed = True
    #double check move position, move there, remove old piece
    if int(board[move1[0]][move1[1]]) == 0:
        board[select1[0]][select1[1]] = 0
        board[move1[0]][move1[1]] = 2
    return (killed)


while True:
    setScreen()
    draw()
    while True:
        if turnP1() != True:
            break
        setScreen()
        draw()
    while True:
        if turnP2() != True:
            break
        setScreen()
        draw()

    #if turn == 2:
