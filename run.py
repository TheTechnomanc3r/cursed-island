
# Import t

import random
import os
from time import sleep


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

#Complete game logo

def winScreen():
    print("################################")
    print("### congratulations you won! ###")
    print("################################")  

# Function to clear the screen

def clearScreen():
    input("Press any key to Continue")
    os.system("clear")


mainLogo()


print("Welcome! Do you want to start a new game? y / n")

startChoice = input(">> ")

if startChoice == ("y"):
    

    print("Game Starting...")
    sleep(0.5)
    clearScreen()

elif startChoice == ("n"):
    print("Closing game ...")
    sleep(1)
    exit()

else:
    print("Invalid choice! Please enter y or n")             



print("[Prologue]\n")
print("\033[1;30mYour lovely sailbot semester in the caribbean didn´t go as planned,")
print("and after going trough a heavy storm you crashed on this deserted island")

print("The Island is tropical with palms and white sand and a dense jungle in the distant\n")

clearScreen()

