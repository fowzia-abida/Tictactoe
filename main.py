# This is a simple Python game.

tictac = ["-", "-", "-",
          "-", "-", "-",
          "-", "-", "-"]
game_is_on = True
winner = None

#who's turn it is

ongoing_player = "X"


def display():
    print(tictac[0] + "|" + tictac[1] + "|" + tictac[2])
    print(tictac[3] + "|" + tictac[4] + "|" + tictac[5])
    print(tictac[6] + "|" + tictac[7] + "|" + tictac[8])


def play_tictac():

#display the empty board
 display()

 while game_is_on :

    turn_time(ongoing_player)
    check_if_game_over()


    # hand it out to the other player
    flip_player()

#the game ended

 if winner == "X" or winner == "0":
     print(winner + "  won")
 elif winner == None:
    print("tie")

def turn_time(player):
  print( player +" 's turn." )
  place_input  = input("choose position to play :")

  valid = False
  while not valid:

          while place_input not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                 place_input = input("invalid, choose from 1 - 9 to play")



          place_input = int(place_input) - 1 # to set the position correctly and to match with the funtion tictac index number


          if tictac[place_input] == "-":
              valid = True
          else:
             print("Not empty here , choose another place !!!")


  tictac[place_input] = player


  display()

def check_if_game_over():
    winner_check()
    check_if_tie()
def winner_check():

    global winner

    #check rows
    row_winner = check_rows()
    #check  columns
    column_winner = check_columns()

    #check corner_from_corner

    corner_winner = check_corner_to_corner()


    if row_winner :
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif corner_winner:
        winner = corner_winner
    else:
        winner= None
        return

def check_rows():
    global game_is_on
    #check any rows have same value and not empty
    row_1 = tictac[0]== tictac[1] == tictac[2] != "-"
    row_2 = tictac[3]== tictac[4] == tictac[5] != "-"
    row_3 = tictac[6]== tictac[7] == tictac[8] != "-"
#if any row matches, there's a win
    if row_1 or row_2 or row_3:
        game_is_on = False
    if row_1:
        return  tictac[0]
    elif row_2:
        return tictac[3]
    elif row_3:
         return tictac[6]
    return

def check_columns():
    global game_is_on
    #check any rows have same value and not empty
    column_1 = tictac[0]== tictac[3] == tictac[6] != "-"
    column_2 = tictac[1]== tictac[4] == tictac[7] != "-"
    column_3 = tictac[2]== tictac[5] == tictac[8] != "-"
    #if any column matches, there's a win
    if column_1 or column_2 or column_3:
        game_is_on = False
    if column_1:
        return  tictac[0]
    elif column_2:
        return tictac[1]
    elif column_3:
        return tictac[2]
    return


def check_corner_to_corner():
    global game_is_on
    #check any rows have same value and not empty
    corner_1 = tictac[0]== tictac[4] == tictac[8] != "-"
    corner_2 = tictac[6]== tictac[4] == tictac[2] != "-"
    #if any column matches, there's a win
    if corner_1 or corner_2 :
        game_is_on = False
    if corner_1:
        return  tictac[0]
    elif corner_2:
        return tictac[6]

    return

def check_if_tie():
    global  game_is_on
    if "-" not  in tictac:
        game_is_on = False
    return
def flip_player():
    global ongoing_player
    if ongoing_player == "X":
        ongoing_player ="0"

    elif ongoing_player == "0":
        ongoing_player = "X"
    return

play_tictac()
