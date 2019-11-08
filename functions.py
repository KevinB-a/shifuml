import random
def name_choice():
    """this function allow the player to choose enter a name or pseudo """
    user=""
    while user =="":
        user=input("please enter your name or pseudo")
    return user

def user_choice():
    """this function allows the player to choose his movement,
    if the player enters nothing or something else than pierre papier ciseaux he starts again  """
    answer=""
    while answer not in ["pierre","papier","ciseaux"]:
        answer=input("Choose pierre , papier or ciseaux").lower()
    return answer

def computer_choice():
    """this function makes it possible to randomly select values """
    list1=["pierre","papier","ciseaux"]
    computer_answer=random.choice(list1)
    return computer_answer
