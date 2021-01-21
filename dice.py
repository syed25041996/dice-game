"""Take user input and add the total with the second dice, if the total is 6 or 12 ,the user gets to roll again
every time he scores a double, his score becomes twice """

import random

score = 0
tries = 0
no_of_tries =  int(input("Enter no of tries: "))

while(tries < no_of_tries):
    try:
        second_dice = [1,2,3,4,5,6]
        print("Input a number between 1 to 6: ", end="")
        user = int(input())
        second_dice = random.choice(second_dice) 
        print (f"{user} and {second_dice}, the sum is {user+second_dice}")
        if user == 6  and second_dice == 6:
            score+=2
        elif user+second_dice == 12:
            score+=2
        else:
            score+=1
        tries+=1
    except:
        print("OOPS something went wrong , please try again!")
    
print(f"The total score is {score}")
    
    

