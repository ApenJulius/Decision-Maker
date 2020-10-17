import secrets
import os
import sys, time
from os import system
system("title " + "Decision Maker")

def sprint(str):
   for c in str + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(3./90)

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

choice = input("Do you wish for method 1 or 2?: ")

if choice == "1":
    while True:
        n = int(input("How many values do you want to input?: "))

        x = []
        for i in range(n):  # same as range(0, n)
            x.append(input("Input?: "))

        sprint(secrets.choice(x) + '\n')

        ans = input("Do you want to clear? [y/n]")

        if ans == "yes" or ans == "y":
            cls()

        else:
            print("")



elif choice == "2":
    while True:
        x = []
        x.append(input("A decision?: "))
        while True:
            poss = input("Another? or are you [done]? ")
            if poss == "done":
                break

            else:
                x.append(poss)

        sprint(secrets.choice(x) + "\n")

        clear = input("Do you wish to clear?[y/n]: ")

        if clear == "yes" or clear == "y":
            cls()
            print("done")

        else:
            print("")



