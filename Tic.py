# Tic Tac Toe

# Global variables
board = [' ']*10
game_state = True
announce = ''

def reset_board():
    global board, game_state
    board = [' ']*10
    game_state = True

def display_board():
    print("  "+board[1]+" |"+board[2]+" |"+board[3]+" ")
    print("--------------")
    print("  "+board[4]+" |"+board[5]+" |"+board[6]+" ")
    print("--------------")
    print("  "+board[7]+" |"+board[8]+" |"+board[9]+" ")
    
def win_check(board, player):
    if ((board[7] == board[8] == board[9] == player) or
       (board[4] == board[5] == board[6] == player) or
       (board[1] == board[2] == board[3] == player) or
       (board[7] == board[5] == board[3] == player) or
       (board[1] == board[5] == board[9] == player) or
       (board[7] == board[4] == board[1] == player) or
       (board[8] == board[5] == board[2] == player) or
       (board[9] == board[6] == board[3] == player)):
        return True
    else:
        return False

def full_board_check(board):
    if ' ' in board[1:]:
        return False
    else:
        return True

def ask_player(mark):
    global board

    while True:
        try:
            choice = int(input('\nChoose where to place your '+mark+' :'))
        except ValueError:
            print('\nSorry, please choose a number between 1-9')
            continue
        if board[choice] == ' ':
            board[choice] = mark
            break
        else:
            print('\nThat spaace is not empty! Choose another.')

def player_choice(mark):
    global board,game_state,announce
    announce = ' '
    mark = str(mark)
    display_board()
    print('\n')

    ask_player(mark)
    if win_check(board,mark):
        print('\n'*100)
        display_board()
        announce = mark + " Won the game. Congratulations!!"
        game_state = False
    elif full_board_check(board):
        announce = "Game is Tie!!"
        game_state = False

    return game_state,announce

def play_game():
    reset_board()
    X = 'X'
    O = 'O'

    while True:
        # Player X turn
        game_state, announce = player_choice(X)
        print('\n'+announce)
        if game_state != True:
            break
        # Player O turn
        game_state, announce = player_choice(O)
        print('\n'+announce)
        if game_state != True:
            break

    # Ask for Rematch
    rematch = input("\nWould you like to play again? Y/N : ")
    if rematch.upper() == 'Y':
        play_game()
    else:
        print("--------------------- Good Bye!! Thanks for Playing -------------------")

play_game()        
        
    
        
    
    
