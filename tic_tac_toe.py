# Tic-Tac-Toe Game
from IPython.display import clear_output
def create_board():
    row = {             # dictionary of characters that will make up board
    "blanks": " ",
    "sides": ' *'
    }
    board = {       # dictionary that contains how many characters make up an aspect of the board
        "first": 2*(5*row["blanks"] + row["sides"]) + 7*row["blanks"],
        "vertical": ("\n" + 2*(5*row["blanks"] + row["sides"]) + 7*row["blanks"]),
        "horizontal": ("\n" + "*" + 10*row["sides"])
    }
    top = board["first"] + 2*board["vertical"] + board["horizontal"]
    middle = 3*board["vertical"] + board["horizontal"]
    bottom = 3*board["vertical"]
    board = top + middle + bottom           #the board itself
    print(board)
    return [board, [] ]

def modify_board(info, marker):
    board = info[0]
    played = info[1]
    player = marker
    test = 0
    dialogue = f"{player}, please select a box based on the numpad keyboard (1-9): "
    error = f"{player}, please enter an integer based on the numpad keyboard!"
    error2 = f"{player}, this box is already occupied. Please select an unoccupied box: "
    while True:
        if test == 1:
            break
        try:
            play_choice = int(input(dialogue))
            if play_choice in range(1, 10) and play_choice not in played:
                break
            elif play_choice in played:
                while True:
                    test = 0
                    try:
                        play_choice = int(input("\n" + error2))
                        if play_choice in range(1,10) and play_choice not in played:
                            test = 1
                            break
                    except:
                        print("\n" + error)
                        break
            else:
                print("\n" + error)
        except:
            print("\n" + error)
    boxes = {
    7: board[:24] + marker + board[25:],
    8: board[:32] + marker + board[33:],
    9: board[:39] + marker + board[40:],
    4: board[:112] + marker + board[113:],
    5: board[:120] + marker + board[121:],
    6: board[:127] + marker + board[128:],
    1: board[:200] + marker + board[201:],
    2: board[:208] + marker + board[209:],
    3: board[:215] + marker + board[216:]
    }
    clear_output()
    print(boxes[play_choice])
    played.append(play_choice)
    return [boxes[play_choice], played]

def choose_marker():
    markers = ["X", "O"]
    print("Choose between yourselves who will be player 1.")
    dialogue = "Player 1, please choose if you want to be 'X' or 'O': "
    error = "Player 1, please enter answer as 'X' or 'O'!"
    while True:                 # reprompts the user until they choose x or o
        answer = input(dialogue)
        if answer.upper() == markers[0] or answer.upper() == markers[1]:    # allows lowercase x and o to be valid choices
            break
        else:
            print("\n" + error)
            continue
    if answer.upper() == markers[0]:    # assigns player2 the free marker
        answer = answer.upper()
        player2 = markers[1]
    else:
        answer = answer.upper()
        player2 = markers[0]
    return [answer, player2]    # return player1 and player2 markers

def game_check(info):
    board = info[0]     # board is the first variable in the info list
    boxes = {
    7: board[24],
    8: board[32],
    9: board[39],
    4: board[112],
    5: board[120],
    6: board[127],
    1: board[200],
    2: board[208],
    3: board[215]}
    plays = [ \
    [boxes[7], boxes[8], boxes[9]], \
    [boxes[4], boxes[5], boxes[6]], \
    [boxes[1], boxes[2], boxes[3]]]         # pseudo 2 dimensional array of the spots on the board
    for i in range(0, 3):
        if plays[i][0] == plays[i][1] == plays[i][2] != " ":    # horizontal winner check
            winner = plays[i][0]
            print(f"{winner} HAS WON THE GAME!!!!!!")
            return "won"
        elif plays[0][i] == plays[1][i] == plays[2][i] != " ":  # vertical winner check
            winner = plays[0][i]
            print(f"{winner} HAS WON THE GAME!!!!!!")
            return "won"
        elif plays[0][2*(i%2)] == plays[1][1] == plays[2][2*(i%-2) + 2] != " ":
            winner = plays[1][1]    # diagonal winner check
            print(f"{winner} HAS WON THE GAME!!!!!!")
            return "won"

def run_game():
    print("Hello welcome to a game of tic-tac-toe!")
    while True:            # while loop to keep the game running until the player chooses NO
        i = 0
        info = create_board()   # first create the board
        markers = choose_marker()   # then have users choose markers
        while True:         # while loop for the actual gameplay that breaks once TIED or WON
            marker = markers[i%2]
            i += 1
            info = modify_board(info, marker)
            check = game_check(info)
            if check == "won":
                break
            elif i == 9:
                print("The game has been tied")
                break
        prompt = input("Would you like to play again? YES or NO: ").upper() # prompt to play again
        if prompt not in ("YES", "NO"): # something other than yes or no then reprompt
            while True:
                prompt = input("Please enter your answer as YES or NO: ").upper()
                if prompt in ("YES", "NO"):
                    break
        if prompt == "YES":  # if yes run the game again, can type yes however many times they want
            clear_output()   # clear the output to clean the interface
            continue
        else:                       # else stop the game
            break

if __name__ == "__main__":
    run_game()
