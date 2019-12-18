import os

#Function that prints board, uses global list 'board'
def printBoard():
    boardStrings = [f'{b[6]}|{b[7]}|{b[8]}', f'{b[3]}|{b[4]}|{b[5]}', f'{b[0]}|{b[1]}|{b[2]}', '-----']
    for i in [0, 3, 1, 3, 2]:
        print(boardStrings[i])

def readPlayerMove(pi):
    global b
    tile = int(input(f'Player {pi+1} choose a tile: '))
    b[tile-1] = player[pi]

def playerWon(board):
    return board[8] == 'X' or board[8]=='O'

# Game setup
b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
game = True

# Player setup
player = ['','']
while player[0] not in ['O', 'X']:
    player[0] = input('Does Player 1 want to be X or O? ')

if player[0] == 'O':
    player[1] = 'X'
else:
    player[1] = 'O'

os.system('clear')
print('Player 1 will start playing.')

pi = 0
while game:
    printBoard()
    readPlayerMove(pi)

    if playerWon(b):
        print(f'\nPlayer {pi+1} won the game!\n')
        replay = input('Play again? ')
        if replay == 'yes':
            b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        else:
            game = False

    pi += 1
    pi = pi%2
    os.system('clear')

print('\nGoodbye, have a nice day!')