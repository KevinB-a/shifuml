from functions import *
import random
"""creation of departure variables"""
continue_game= True
print("Welcome on shifumi game")
while continue_game == True:
    score_user=0
    score_computer=0
    print(name_choice())
    while score_user !=3 and score_computer !=3:
        stone="pierre"
        paper="papier"
        scissor="ciseaux"
        user_answer=user_choice()
        computer_answer=computer_choice()
        print(computer_answer)

        """user win case """

        if computer_answer == stone and user_answer == paper:
            score_user+=1
            print("you win your score is", score_user ,"computer's score is",score_computer)

        if user_answer == stone and computer_answer == scissor:
            score_user+=1
            print("you win your score is", score_user ,"computer's score is",score_computer)

        if computer_answer == paper and user_answer == scissor:
            score_user+=1
            print("you win your score is",score_user,"computer's score is",score_computer)

        """computer win case """

        if user_answer == stone and computer_answer == paper:
            score_computer+=1
            print("computer win computer's score is",score_computer,"and your score is",score_user)

        if user_answer == paper and computer_answer == scissor:
            score_computer+=1
            print("computer win computer's score is",score_computer,"and your score is ",score_user)

        if computer_answer == stone and user_answer== scissor:
            score_computer+=1
            print("computer win computer's score is",score_computer,"and your score is ",score_user)

        """ draw case"""
        if user_answer == computer_answer:
            print("draw no one win points your score",score_user,"and computer's score is",score_computer)

    rematch=input("do you want to play again ? enter yes for rematch and no for quit").lower()
    if rematch =="no" or rematch == "n" or rematch =="quit" or rematch == "q":
        continue_game = False

    else:
        continue_game = True
