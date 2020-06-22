#Get user to guess between 1-10
#Return if guess is too high or low
#Count number of tries

import random

#Generate random number

random_no = random.randint(1, 11)

#Set number of incorrect guesses to 0

count = 0



while True:
    #Get user to input guess
    
    user_number = int(input("Please guess number between 1-10: "))

    #Check if number is in range
    
    if user_number in range(1, 11):

        #Evaluate if number is same as random number
        
        if user_number == random_no:
            print("you are correct, you had", count, "incorrect guesses")
            break
        elif user_number < random_no:
            print("Your number is too low")
            count += 1
        else:
            print("Your number is too high")
            count += 1
    else:
        print("Invalid number")

