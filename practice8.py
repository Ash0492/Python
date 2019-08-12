
import random


#The Game of Rock, Paper and Scissors

#Rules of the game
print('Winning rules of the game are as follows:\n'+
'Rock VS Paper => Paper wins\n'
+'Rock VS Scissor => Rock Wins\n'
+'Paper VS Scissor => Scissor wins')

while True:
    print("Please enter one the below choices:\n"+ "1. Rock\n"+"2.Paper\n"+ "3.Scissors\n")

    user_choice = int(input("Please enter your choice(user turn):"))



while user_choice > 3 or user_choice < 1: 
     user_choice = int(input("enter valid input: ")) 

if user_choice == 1:
    choice_name = "Rock"
elif user_choice == 2:
    choice_name = "Paper"
else:
    choice_name = "Scissor"

    print("user choice is: " + choice_name) 

print("\nNow its computer turn.......") 
comp_choice = random.randint(1, 3) 
	

while comp_choice == choice: 
		comp_choice = random.randint(1, 3) 

	
if comp_choice == 1: 
        comp_choice_name = 'Rock'
elif comp_choice == 2: 
        comp_choice_name = 'paper'
else: 
		comp_choice_name = 'scissor'
		
print("Computer choice is: " + comp_choice_name) 

print(choice_name + " V/s " + comp_choice_name) 

	
if((user_choice == 1 and comp_choice == 2) or
	(user_choice == 2 and comp_choice ==1 )): 
		print("paper wins => ", end = "") 
		result = "paper"
		
elif((user_choice == 1 and comp_choice == 3) or
		(user_choice == 3 and comp_choice == 1)): 
		print("Rock wins =>", end = "") 
		result = "Rock"
else: 
		print("scissor wins =>", end = "") 
		result = "scissor"

	
if result == choice_name: 
		print("<== User wins ==>") 
else: 
		print("<== Computer wins ==>") 
		
print("Do you want to play again? (Y/N)") 
ans = input() 


if ans == 'n' or ans == 'N': 
    break
	

print("\nThanks for playing") 
