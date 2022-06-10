import random

exit = False # this means the user has not exited the game

#user points
userpoints = 0
computerpoints = 0

while exit == False:
    #options to choose  from
    options = ["rock", "paper", "scissors"]
    user_input = input("Chosse rock, paper, scissors or exit: ")
    #computer choice choosing randoml from the list
    computer_input = random.choice(options)

    if user_input == "exit":
        print(f"Game is ended.Your total is {userpoints} and computer total score is {computerpoints}")
      
        exit = True
    if user_input == "rock":
        if computer_input == "rock":
            print("Your input is rock")
            print("computer input is rock")
            print("its a tie")
        elif computer_input == "paper":
            print("Your input is rock")
            print("computer input is paper")
            print("computer wins")
            computerpoints += 1 # this counts the number of points
        elif computer_input == "scissors":
            print("Your input is rock")
            print("computer input is scissors")
            print("you win")
            userpoints += 1 # this counts the number of points
    elif user_input == "paper":
         if computer_input == "rock":
            print("Your input is paper")
            print("computer input is rock")
            print("you win!")
            userpoints += 1
         elif computer_input == "paper":
            print("Your input is paper")
            print("computer input is paper")
            print("its a tie")
            
         elif computer_input == "rock":
            print("Your input is paper")
            print("computer input is scissors")
            print("computer win")
            computerpoints += 1
    if user_input == "scissors":
        if computer_input == "rock":
            print("Your input is scissors")
            print("computer input is rock")
            print("comp wins")
            computerpoints += 1
        elif computer_input == "paper":
            print("Your input is scissors")
            print("computer input is paper")
            print("you win")
            userpoints += 1 # this counts the number of points
        elif computer_input == "scissors":
            print("Your input is scissors")
            print("computer input is scissors")
            print("its a tie")


    elif user_input != "rock" or user_input != "paper" or user_input != "scissors":
            print("It is an invalid input")


