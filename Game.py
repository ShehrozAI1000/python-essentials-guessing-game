# Cisco Python Essentials 1 - Project 1
# Project: Number Guessing Game

import random
# it is used for to import random modules 

secret_number=random.randint(1,100)
# use to allow the computer to select one number between 1 to 100
attempt=0
# it will show that how many attempts you made for win or succeed 
while True:
        # use of while loop to run the program again and again untill we do not 
        # succeed  
        user_number=int(input("**** Enter you number **** "))
        attempt +=1 
    # it will ask the user choice and every time will increase 1 try 
    # untill we do not reach real destination 
        if user_number==secret_number:
        # here conditional statements use 
            print("**** You have been succeed **** ")
            print(f"**** You made {attempt} attempts to win **** ")
            break
        elif user_number<secret_number:
        # if number will be small it will show this message and suggest you for try again 
            print("Sorry, Your entered number is small Please try again ---> ")
        else:
            print("Your number is larger than guess number enter small number --->")
        # in that case number is larger so it will recommend you for entering small number 
    
print("*** Game Over *** \n ** You are win ** ") 