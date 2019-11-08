import random
def name_choice():
    """this function allow the player to choose enter a name or pseudo """
    user=""
    while user =="": #if value of user is empty the loop continue
        user=input("please enter your name or pseudo")
    return user

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
