from operator import truediv
import random

your_name = input("Enter your name : ")
print("Hey",your_name+"!!\n","Welcome to the Dice rolling Simulator.\n")

random_number = random.randint(1,6)


while True:
    mode = input('Wanna Roll the Dice ? type "Y" to roll or type "Q" to quite : \n').upper()

    if mode == "Y":
        print("The number is :",random_number)
    if mode == "Q":
        quit()