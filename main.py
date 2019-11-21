import random

from functions import *

"""creation of departure variables"""
continue_game = True
print("Welcome on shifumi game")

while continue_game == True: # create loop for reload the game
    score_user=0 # initalize both score at 0
    score_computer=0

    print(name_choice())

    while score_user !=3 and score_computer !=3: #loop stop when score_user or score_computer is 3
        compare_score()
    rematch=input("do you want to play again ? enter yes for rematch and no for quit").lower()
    if rematch =="no" or rematch == "n" or rematch =="quit" or rematch == "q" or rematch== "stop":
        continue_game = False #if user choose stop the game continue_game become false and while loop stop

    else:
        continue_game = True #restart the game if user wants
