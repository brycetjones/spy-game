import os 
from random import randint
print("-----------------------------------------------")
print("Welcome to spy or whatever this game is called!")
print("\n")
print("Select a category:")
print("1. Monsters")
print("2. Loosers and Haters")
print("-----------------------------------------------")

names = []
inputVal = ""

def clear():
    if os.name =="nt":
        os.system('cls')
    else:
        os.system("clear")

# Read selected category
category = int(input())
path = os.getcwd()
if category == 1:
    path += '/cats/monsters'
elif category == 2:
    path += '/cats/loosers'
file = open(path, 'r')
options = file.read().split(',')

# Select random item from category
index = randint(0, len(options))
item = options[index]

# Read inputted names
clear()
while inputVal != 'done':
    inputVal = input("Enter name (Type 'done' if no more players):\n")
    clear()
    if inputVal != 'done':
        names.append([inputVal])
imposter = randint(0, len(names)-1)
for i, x in enumerate(names):
    input("Hand computer to "+ x[0] + " (Type ENTER once you have it).\n")
    if i==imposter:
        input("You are the imposter! (Type ENTER to continue).\n")
        clear()
    else:
        input(x[0] + ", the item is " + item + " (click Enter to continue).\n")
        clear()

