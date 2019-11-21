import random

def name_choice():
    """this function allow the player to choose enter a name or pseudo """
    username=""
    while username =="": #if value of user is empty the loop continue
        user=input("please enter your name or pseudo")
        return username

def user_choice():
    """this function allows the player to choose his movement,
    if the player enters nothing or something else than pierre papier ciseaux he starts again  """
    answer=""
    while answer not in ["pierre","papier","ciseaux"]: # the loop turn until answer is in list
        answer=input("Choose pierre , papier or ciseaux").lower() #if user enter a letter in uppercase .lower permit
    return answer                                             #to put value in tiny

def computer_choice():
    """this function makes it possible to randomly select values """
    list1=["pierre","papier","ciseaux"]
    computer_answer=random.choice(list1) # choose random element in list1
    return computer_answer

def user_score():
    user_score=0
    return user_score

def computer_score():
    computer_score=0
    return computer_score

def compare_score() :
    stone="pierre"
    paper="papier"
    scissor="ciseaux"
    user_answer=user_choice() #call function user_choice
    computer_answer=computer_choice() #call function computer_choice
    print(computer_answer)
    score_user=user_score()
    score_computer=computer_score()

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
    return score_user,score_computer
