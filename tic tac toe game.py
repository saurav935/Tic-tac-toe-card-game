
board=[' ',' ',' ',
       ' ',' ',' ',
       ' ',' ',' ']

game_on=True

# Greetings:
print('Welcome to Tic Tac Toe!')


# Sample board:
print('The game board is numbered in this way:')
board1=[[0,1,2],
        [3,4,5],
        [6,7,8]]
for r in board1:
    print(r)

# Winning vertically
def vertical():
    global game_on
    if board[0]==board[3]==board[6]==player:
        print(player,'has won the game')
        game_on=False
    elif board[1]==board[4]==board[7]==player:
        print(player,'has won the game')
        game_on=False
    elif board[2]==board[5]==board[8]==player:
        print(player,'has won the game')
        game_on=False
    return vertical

# Winning horizontal
def horizontal():
    global game_on
    if board[0] == board[1] == board[2] == player:
        print(player, 'has won the game')
        game_on = False
    elif board[3] == board[4] == board[5] == player:
        print(player, 'has won the game')
        game_on = False
    elif board[6] == board[7] == board[8] == player:
        print(player, 'has won the game')
        game_on = False
    return horizontal

# Winning diagonally
def diagonal():
    global game_on
    if board[0] == board[4] == board[8] == player:
        print(player, 'has won the game')
        game_on = False
    elif board[2] == board[4] == board[6] == player:
        print(player, 'has won the game')
        game_on = False
    return diagonal

# All winning categories
def all_win():
    vertical()
    horizontal()
    diagonal()
    return all_win

# Choice between X and O:
def player_status():
    choice = 'wrong'
    while choice not in ['X', 'O']:
        print('Please choose between X or O')
        choice = input('Player1 = Do you want to be X or O :').upper()
    if choice == 'X':
        print('Player1 will play first')
        print('Player 1 = X')
        print('Player 2 = O')
    elif choice == 'O':
        print('Player1 will play first')
        print('Player 1 = O')
        print('Player 2 = X')

    return choice

player=player_status()


# Displaying game board:
def display():
    print(board[0] + ' |' + board[1] + ' |' + board[2])
    print(board[3] + ' |' + board[4] + ' |' + board[5])
    print(board[6] + ' |' + board[7] + ' |' + board[8])

    return display

# Flip player
def flip_player():
    global player
    if  player=='X':
        player='O'
    else:
        player='X'
    return flip_player


# Confirmation on whether to start the game or not:
confirmation='wrong'
while confirmation not in ['Y','N']:
    print('Please choose between Y or N')
    confirmation = input('Are you ready to play? ( Y / N ):').upper()
    if confirmation=='Y':
        print('This is the initial board:')
        display()
    elif confirmation=='N':
        confirmation='wrong'
        while confirmation=='N':
             confirmation = input('Are you ready to play? ( Y / N ):').upper()


# Deciding the position of the value using index
def position():
    board[index]=current_player
    return display()



# Game on
while game_on:
    current_player=player
    index='wrong'
    while index not in (0,1,2,3,4,5,6,7,8):
        index=int(input('Choose any position between ( 0-8 ):'))
        if index not in (0,1,2,3,4,5,6,7,8):
            print('Your choice is beyond the range.\nPlease select the number within the specified range.')
        else:
            pass
    if board[index]==' ':
        position()
    else:
        print('The position is already occupied !! \n Please choose a valid position.')
    vertical()
    horizontal()
    diagonal()
    flip_player()


