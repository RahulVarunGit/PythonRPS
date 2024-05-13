import random
import sys
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

print("Rock Paper Scissors".center(60,"="))
playerChoice = int(input("1 ROCK \n 2 PAPER \n 3 SCISSORS \n ENTER YOUR CHOICE : "))
computerChoice = int(random.choice('123'))

print("Result".center(60,"="))
print("Player choice is " + str(RPS(playerChoice)).replace("RPS.",""))
print ("Computer choice is " + str(RPS(computerChoice)).replace("RPS.",""))

if (playerChoice == 1 and computerChoice == 2) or (playerChoice == 2 and computerChoice == 3) or (playerChoice == 3 and computerChoice == 1) :
    print("You loose 😒")
elif (playerChoice == computerChoice) :
    print("Tie game. Try again. 😲")
else :
    print("You won 😁")
print("Play again".center(60,"="))        
