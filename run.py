
# Import

import random
import os
from time import sleep

# ASCI color codes

# Main logo in ASCI Code


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

# Game over screen in ASCI Code

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
                   



# Complete game logo

def winScreen():
    print("\033[32m ################################")
    print("\033[32m ### congratulations you won! ###")
    print("\033[32m ################################\n")  

# Function to clear the screen

def clearScreen():
    input("\033[30mPress ENTER key to Continue...")
    os.system("clear")

# Quick clear

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
        sleep(0.2)
        newGame()             


def firstChoice():

    print("Do you want to go to the jungle or go back to the boat?\n")
    print("go to \033[1;32m(J)ungle\n")
    print("\033[1;30mgo back to \033[1;34m(B)oat\n")

    startChoice = input("\033[30m>> ")

    if startChoice == ("j"):
        print("You head for the jungle!")
        qclear()
        jungle()

    elif startChoice == ("b"):
        print("You go back to the boat")
        print("And is struck by lightning!")
        sleep(0.3)
        gameOver()
        tryAgain()

    else:
        print("\033[31mInvalid choice! Select J or B")
        sleep(0.6)
        qclear()
        prologue()
        firstChoice()

def secondChoice():




    secChoice = input("\033[30m>> ")

    if secChoice == ("r"):
        print("You charge and sprint over the bridge!")
        bridge()


    elif secChoice == ("w"):
        print("You to start to walk slowly over the bridge")
        print("But the bridge collapses and throws you in the river")
        sleep(0.3)
        gameOver()
        tryAgain()

    else:
        print("\033[31mInvalid choice Select r or w")
        sleep(0.5)
        qclear()
        jungle()       

def thirdChoice():

    triChoice = input("\033[30m>> ")

    if triChoice == ("r"):
        print("You rush towards the boat and quickly jumps in")
        print("The Boat looks like a good way to get out of here!\n")
        winScreen()


    elif triChoice == ("f"):
        print("You to start to fight the Gorilla!")
        print("But the Gorilla is too strong and knocks you out!")

        sleep(0.3)
        gameOver()
        tryAgain()

    else:
        print("\033[31mInvalid choice Select r or w")
        sleep(0.5)
        qclear()
        bridge()    

# Jungle
def jungle():

    print("\033[30mYou walk trough the dense jungle and suddenly you stumble")
    print("\033[30mupon a large river with a hanging bridge on top of it")
    print("\033[30m--------------------------------------------------")
    print("\033[30mIt looks unstable, But your best bet is to continue...\n")
    print("\033[30mDo you wanna \033[34m(R)un fast over or \n \033[32m (W)alk slowly over it")  

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

    secondChoice()


def bridge():
    qclear()
    print("")
    print("\033[30mYou made it over safely! \n")
    print("\033[30mYou see the coast again and close to it, a motorboat it seems")
    print("\033[30m--------------------------------------------------------")
    print("""\033[34m
            ____
           /     \__ 
   _______/          \\
~~/__________________/~~~~~~

    """)
    clearScreen()
    print("")
    print("\033[32mSuddenly! An agressive gorilla showed up from the jungle!!\n")
    print("\033[30mDo you wanna \033[34m(F)ight it! or \n \033[33m (R)un to the boat?\n")

    thirdChoice() 
    


# ---------------------- NEW GAME STARTS HERE ------------------------

newGame()
