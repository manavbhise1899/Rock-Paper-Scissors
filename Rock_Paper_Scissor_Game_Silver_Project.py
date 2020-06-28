import random  
print("Winning Rules of the Rock Paper Scissor Game as follows: \n"
								+"Rock vs Paper->Paper wins \n"
								+"Rock vs Scissor->Rock wins \n"
                                                                +"Paper vs Rock->Paper wins \n"
                                                                +"Paper vs Scissor->Scissor wins \n"
                                                                +"Scissor vs Rock->Rock wins \n"
                                                                +"Scissor vs Paper->Scissor wins \n"
                                                                +"Rock vs Rock->Tie \n"
                                                                +"Paper vs Paper->Tie \n"
                                                                +"Scissor vs Scissor->Tie \n")

while True: 

	print("Enter choice \n 1. Rock \n 2. Paper \n 3. Scissor \n") 
	choice = int(input("User turn: ")) 
	while choice > 3 or choice < 1: 
		choice = int(input("enter valid input: ")) 
	if choice == 1: 
		choice_name = 'Rock'
	elif choice == 2: 
		choice_name = 'Paper'
	else: 
		choice_name = 'Scissor'
		
	print("user choice is: " + choice_name) 
	print("\nNow its computer turn.......") 

	comp_choice = random.randint(1, 3) 
	
	while comp_choice == choice: 
		comp_choice = random.randint(1, 3) 

	if comp_choice == 1: 
		comp_choice_name = 'Rock'
	elif comp_choice == 2: 
		comp_choice_name = 'Paper'
	else: 
		comp_choice_name = 'Scissor'
		
	print("Computer choice is: " + comp_choice_name) 

	print(choice_name + " V/s " + comp_choice_name) 

	if((choice == 1 and comp_choice == 2) or
	(choice == 2 and comp_choice ==1 )): 
		print("Paper wins => ", end = "") 
		result = "Paper"
		
	elif((choice == 1 and comp_choice == 3) or
		(choice == 3 and comp_choice == 1)): 
		print("Rock wins =>", end = "") 
		result = "Rock"
	else: 
		print("Scissor wins =>", end = "") 
		result = "Scissor"

	if result == choice_name: 
		print("<== User wins ==>") 
	else: 
		print("<== Computer wins ==>") 
		
	print("Do you want to play again? (Y/N)") 
	ans = input() 

	if ans == 'n' or ans == 'N': 
		break
	 
print("\nThanks for playing") 
