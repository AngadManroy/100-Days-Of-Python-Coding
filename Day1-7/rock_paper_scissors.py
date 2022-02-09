from os import system
import random as r

def game():
    choice=True
    inp=-1
    while choice:
        inp = input("What do you pick!?")
        if inp==0:
            return
        else:
            eng=r.randint(1,4)
            if inp==eng:
                print("It is a draw!")
            elif inp==1 and eng!=3:
                print("You win!")
            elif inp==2 and eng!=1:
                print("You win!")
            elif inp==3 and eng!=2:
                print("You win!")
            else:
                print("You lose!")
    return

if __name__=="__main__":
    choice = int(input(("Are you ready to play the game?\n[1]Yes\n[2]NO\n")))
    if (choice==0):
        system.exit(0)
    else:
        print("Type 1 for Rock, 2 for Scissor, 3 for paper and type 0 to exit the game!")
        game()