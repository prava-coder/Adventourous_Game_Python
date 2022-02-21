#program to play an adventute game
print("-----------WELCOME TO ADVENTURE GAME--------")
def playagain():
    opinion=input("Do you want to play again...(yes/no):\n")
    if opinion=="yes":
        print("Alright let's start the game again")
        adv_level1()
    else:
        print("comeback when you are interseted")
        print("-----GOOD BYE----")


def adv_level1():
    option=input("choose left or right to move forward in the game:(left/right)\n")
    if option=="left":
        print("sorry buddy...bad luck")
        print("You have choosen the wrong path")
        playagain()
    elif option=="right":
        print("collect the coins in the path..")
        adv_level2()
    else:
        print("the entered option is not in the list")
        print("start the game again")
        playagain()

def adv_level2():
    option=input("which coins are you collected:(silver/gold)\n")
    if option=="silver":
        print("Bad Luck,silver coins are not valid..")
        print("go back to previous level")
        adv_level1()
    elif option=="gold":
        print("you entered to next level ")
        adv_level3()
    else:
        print("your choice is not in the option")
        playagain()

def adv_level3():
    option=input("collect the ticket in your path:(black/white):\n")
    if option=="black":
        print("your ticket is not valid..bad luck")
        playagain()
    elif option=="white":
        print("you are eligible to enter to the adventourous house...")
        print("you won the game")

adv_level1()