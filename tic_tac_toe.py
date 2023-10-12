def display_board(board):

    
    print('     |    | ')
    print('  ' +board[7]+'  |  '+board[8]+' | ' +' '+board[9])
    print('     |    | ')
    print('---------------')
    print('     |    | ')
    print('  '+board[4]+'  |  '+board[5]+' | ' +' '+board[6])
    print('     |    | ')
    print('---------------')
    print('     |    | ')
    print('  '+board[1]+ '  |  '+board[2]+' | ' +' '+board[3])
    print('     |    | ')

test_board=['0','X','O','X','O','X','O','X','O','X']
display_board(test_board)




def player_input():

    '''
    output=(player 1 marker , player 2 marker )
    '''

    marker=''

    while not marker =='X' or marker=='O':
        marker=input("player 1 : choose X or O:").upper()


    if marker=='X':
        return ('X',"O")
    else:
        return ('O','X')

player1 , player2=player_input()

print(player2)

def place_marker(board , marker , position):
    board[position]=marker

    

place_marker(test_board,'$',8)
display_board(test_board)

def win_check(board,mark):

    return ((board[7]==board[8]==board[9]==mark)or
    (board[4]==board[5]==board[6]==mark) or
    (board[1]==board[2]==board[3]==mark) or
    (board[7]==board[4]==board[1]==mark) or
    (board[8]==board[5]==board[2]==mark) or
    (board[9]==board[6]==board[3]==mark) or
    (board[7]==board[5]==board[3]==mark) or
    (board[9]==board[5]==board[1]==mark) )

display_board(test_board)

win_check(test_board,'X')

import random

def choose_first():
    flip=random.randint(0,1)

    if flip==0:
        return 'player 1 '
    else:
        return 'player 2 '

def space_check(board,position):
    return board[position] ==' '

def full_board_check(board):

    for i in range(1,10):
        if space_check(board,i):
            return False
    return True