import random

from functions import *

"""creation of departure variables"""
continue_game= True
print("Welcome on shifumi game")

while continue_game == True: # create loop for reload the game
    score_user=0 # initalize both score at 0
    score_computer=0

    print(name_choice())

    while score_user !=3 and score_computer !=3: #loop stop when score_user or score_computer is 3
        stone="pierre"
        paper="papier"
        scissor="ciseaux"
        user_answer=user_choice() #call function user_choice
        computer_answer=computer_choice() #call function computer_choice
        print(computer_answer)

        """user win case """

        if computer_answer == stone and user_answer == paper: # paper win against stone
            score_user+=1
            print("//////////////////////////////////////////////////")
            print("you win your score is", score_user ) #display user score
            print("computer's score is",score_computer) #display computer's score
            print("//////////////////////////////////////////////////")
        if user_answer == stone and computer_answer == scissor: #stone win against scissor
            score_user+=1
            print("//////////////////////////////////////////////////")
            print("you win your score is", score_user ) #display user score
            print("computer's score is",score_computer) #display computer's score
            print("//////////////////////////////////////////////////")
        if computer_answer == paper and user_answer == scissor: #scissor win against paper
            score_user+=1
            print("//////////////////////////////////////////////////")
            print("you win your score is", score_user ) #display user score
            print("computer's score is",score_computer) #display computer's score
            print("//////////////////////////////////////////////////")
        """computer win case """

        if user_answer == stone and computer_answer == paper:
            score_computer+=1
            print("//////////////////////////////////////////////////")
            print("you loose your score is", score_user ) #display user score
            print("computer's score is",score_computer) #display computer's score
            print("//////////////////////////////////////////////////")
        if user_answer == paper and computer_answer == scissor:
            score_computer+=1
            print("//////////////////////////////////////////////////")
            print("you win your score is", score_user ) #display user score
            print("computer's score is",score_computer) #display computer's score
            print("//////////////////////////////////////////////////")
        if computer_answer == stone and user_answer== scissor:
            score_computer+=1
            print("//////////////////////////////////////////////////")
            print("you win your score is", score_user ) #display user score
            print("computer's score is",score_computer) #display computer's score
            print("//////////////////////////////////////////////////")
        """ draw case"""
        if user_answer == computer_answer:
            print("//////////////////////////////////////////////////")
            print("draw no one win ")
            print("your score",score_user)
            print("computer's score is",score_computer)
            print("//////////////////////////////////////////////////")
    rematch=input("do you want to play again ? enter yes for rematch and no for quit").lower()
    if rematch =="no" or rematch == "n" or rematch =="quit" or rematch == "q" or rematch== "stop":
        continue_game = False #if user choose stop the game continue_game become false and while loop stop

    else:
        continue_game = True #restart the game if user wants
