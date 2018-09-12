def display_board(board):
    print(board[7]+'|'+board[8]+"|"+board[9])
    print("-----")
    print(board[4]+'|'+board[5]+"|"+board[6])
    print("-----")
    print(board[1]+'|'+board[2]+"|"+board[3])

test_board = [' ']*10

def player_input():
    marker=''
    while marker!='x' and marker!='o':
        marker=input("\n\nplayer1,please choose a marker(x,o) ")
    player1=marker
    if player1=='x':
        player2='o'
    else:
        player2='x'
    print("\n\nso player1 is {} and player2 is {}".format(player1,player2))
    return player1

def place_marker(board, marker, position):
    if position==1:
        board[1]=marker
    elif position==2:
        board[2]=marker
    elif position==3:
        board[3]=marker
    elif position==4:
        board[4]=marker
    elif position==5:
        board[5]=marker
    elif position==6:
        board[6]=marker
    elif position==7:
        board[7]=marker
    elif position==8:
        board[8]=marker
    elif position==9:
        board[9]=marker

def win_check(board, mark):
    if board[1]==board[2] and board[2]==board[3] and board[1]==mark:
        return True
    elif board[4]==board[5] and board[5]==board[6]and board[4]==mark:
        return True
    elif board[7]==board[8] and board[8]==board[9]and board[7]==mark:
        return True
    elif board[1]==board[5] and board[5]==board[9] and board[9]==mark:
        return True
    elif board[3]==board[5] and board[5]==board[7]and board[7]==mark:
        return True
    elif board[1]==board[4] and board[4]==board[7] and board[7]==mark:
        return True
    elif board[2]==board[5] and board[5]==board[8]and board[8]==mark:
        return True
    elif board[3]==board[6] and board[6]==board[9]and board[6]==mark:
        return True

import random

def choose_first():
    chance=random.randint(1,2)
    if chance==1:
        print("\n\ncongratulations player1! You have the first turn ")
        return chance
    else:
        print("\n\ncongratulations player2! You have the first turn ")
        return chance

def space_check(board, position):
    if board[position]==' ':
        return True
    else:
        return False

def full_board_check(board):
    for symbol in board:
        if symbol==' ':
            return False
    return True

def player_choice(board):
    position=int(input("Enter your position!"))
    if space_check(test_board,position):
        return position
    else:
        return 0

def replay():
    choice=input("Do you want to play again?(Yes or No)")
    if choice=="Yes" or choice=="yes":
        return True
    else:
        return False

print('Welcome to Tic Tac Toe!\n\n')
test_board=[' ']*10
test_board[0]='$'
display_board(test_board)
play=True
while play==True:
    test_board=[' ']*10
    test_board[0]='$'#while True
    player1marker=player_input()
    if player1marker=='x':
        player2marker='o'
    else:
        player2marker='x'
    chance=choose_first()
        # Set the game up here
    #pass
    while True:
        if full_board_check(test_board)==True:
            print("The match is Tie!")
            break
        if chance==1:
            position=0
            while position==0:
                position=player_choice(test_board)#Player 1 Turn
            place_marker(test_board,player1marker,position)
            display_board(test_board)
            chance=2
            if win_check(test_board,player1marker):
                print("congratulation player1.You have won the game")
                break
            if full_board_check(test_board)==True:
                print("The match is Tie!")
                break
        if chance==2:
            position=0
            while position==0:
                position=player_choice(test_board)
            place_marker(test_board,player2marker,position)
            display_board(test_board)
            chance=1
            if win_check(test_board,player2marker):
                print("congratulation player2.You have won the game")
                break
            if full_board_check(test_board)==True:
                print("The match is Tie!")
                break# Player2's turn.
    play=replay()