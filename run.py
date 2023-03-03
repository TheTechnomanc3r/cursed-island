
# Import 

import random
import os
from time import sleep

# ASCI color codes

#Main logo in ASCI Code

def mainLogo():

    print("""\033[32m 
   ______                         __   ____     __                __
  / ____/_  _______________  ____/ /  /  _/____/ /___ _____  ____/ /
 / /   / / / / ___/ ___/ _ \/ __  /   / // ___/ / __ `/ __ \/ __  / 
/ /___/ /_/ / /  (__  )  __/ /_/ /  _/ /(__  ) / /_/ / / / / /_/ /  
\____/\____/_/  /____/\___/\____/  /___/____/_/\____/_/ /_/\____/   
-----------------------------------------------------------------
#################################################################
""")

#Game over screen in ASCI Code

def gameOver():
    print("""\033[31m
   ▄▄ •  ▄▄▄· • ▌ ▄ ·. ▄▄▄ .           ▌ ▐·▄▄▄ .▄▄▄  
▐█ ▀ ▪▐█ ▀█ ·██ ▐███▪▀▄.▀·    ▪     ▪█·█▌▀▄.▀·▀▄ █·
▄█ ▀█▄▄█▀▀█ ▐█ ▌▐▌▐█·▐▀▀▪▄     ▄█▀▄ ▐█▐█•▐▀▀▪▄▐▀▀▄ 
▐█▄▪▐█▐█ ▪▐▌██ ██▌▐█▌▐█▄▄▌    ▐█▌.▐▌ ███ ▐█▄▄▌▐█•█▌
·▀▀▀▀  ▀  ▀ ▀▀  █▪▀▀▀ ▀▀▀      ▀█▄▀▪. ▀   ▀▀▀ .▀  ▀
  """)

def tryAgain():
    print("You died..")
    print("Do you wanna try again? y/n")

    tryChoice = input(">> ")

    if tryChoice == ("y"):
              
        newGame()

    elif tryChoice == ("n"):


        print("Closing game ...")
        sleep(1)
        exit()
                   



#Complete game logo

def winScreen():
    print("################################")
    print("### congratulations you won! ###")
    print("################################")  

# Function to clear the screen

def clearScreen():
    input("Press ENTER key to Continue...")
    os.system("clear")

# quick clear

def qclear():
    os.system("clear") 

# Print Prologue

def prologue():

    print("\033[1;32m[Prologue]\n")
    print("\033[1;30mYour lovely sailbot semester in the caribbean didn´t go as planned,")
    print("and after going trough a heavy storm you crashed on a deserted island")

    print("The Island is tropical with palms, white sand and a dense jungle is seen in the distant.\n")       

# Starts a new game

def newGame():

    mainLogo()  

    print("\033[1;30mWelcome! Do you want to start a new game? y / n")

    startGame = input(">> ")

    if startGame == ("y"):
    
        print("Game Starting...")  
        sleep(0.3)
        qclear()
        prologue()
        firstChoice()

    elif startGame == ("n"):

        print("Closing game ...")
        sleep(1)
        exit()

    else:
        print("Invalid choice! Please enter y or n")
        qclear()
        sleep(0.3)
        newGame()             


def firstChoice():

    print("Do you want to go to the jungle or go back to the boat?\n")
    print("go to \033[1;32m(J)ungle\n")
    print("\033[1;30mgo back to \033[1;34m(B)oat\n")

    startChoice = input("\033[30m>> ")

    if startChoice == ("j"):
        print("You head for the jungle!")
        clearScreen()
        jungle()

    elif startChoice == ("b"):
        print("You go back to the boat")
        sleep(0.3)
        gameOver()
        tryAgain()

    else:
        print("Invalid choice Select J or B")
        sleep(0.3)
        firstChoice()
        qclear()

# Jungle
def jungle():

    print("You walk trough the dense jungle and suddenly you stumble")
    print("upon a large river with a hanging bridge on top of it")
    print("--------------------------------------------------")
    print("It looks unstable, But your best bet is to continue...\n")
    print("Do you wanna (R)un fast over or \n walk (S)lowly over it")  

    print("""\033[36m
    / |           /|    
   /  |          / |   
  /   |_________/__|
 /    /________/___/
/ |  _________/_|_
  | /________/__|/
   _________/___
  /________/___/
 _________/____
/________/___/
    
    
    """) 

    


#---------------------- NEW GAME STARTS HERE ------------------------

newGame()



# Bridge


# Cave