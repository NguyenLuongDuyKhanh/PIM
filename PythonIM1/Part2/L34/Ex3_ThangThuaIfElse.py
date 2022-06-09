import random

ask = True
name = ["rock", "paper", "scissors", "lizard", "spock"]
print("chooses rock, paper, scissors, lizard or spock")
user_choice = ''
while ask == True:
    user_choice = input("please try to write the exact name")
    if user_choice.lower() in name:
        ask = False

print("Finish")
comp_num = random.randrange(0,5)
comp_choice = name[comp_num]
print("computer chooses", comp_choice)

if comp_choice == user_choice:
    print("it's a tie!")

#Asume user chooses paper
elif user_choice == 'paper' and comp_choice == 'rock':
    print("player wins!")
elif user_choice == 'paper' and comp_choice == 'spock':
    print("player wins!")
elif user_choice == 'paper' and comp_choice == 'lizard':
    print("computer wins!")
elif user_choice == 'paper' and comp_choice == 'scissors':
    print("computer wins!")

#Asume user chooses scissors
elif user_choice == 'scissors' and comp_choice == 'paper':
    print("player wins!")
elif user_choice == 'scissors' and comp_choice == 'lizard':
    print("player wins!")
elif user_choice == 'scissors' and comp_choice == 'spock':
    print("computer wins!")
elif user_choice == 'scissors' and comp_choice == 'rock':
    print("computer wins!")

#Asume user chooses spock
elif user_choice == 'spock' and comp_choice == 'rock':
    print("player wins!")
elif user_choice == 'spock' and comp_choice == 'scissors':
    print("player wins!")
elif user_choice == 'spock' and comp_choice == 'lizard':
    print("computer wins!")
elif user_choice == 'spock' and comp_choice == 'paper':
    print("computer wins!")

#Asume user chooses lizard
elif user_choice == 'lizard' and comp_choice == 'paper':
    print("player wins!")
elif user_choice == 'lizard' and comp_choice == 'spock':
    print("player wins!")
elif user_choice == 'lizard' and comp_choice == 'rock':
    print("computer wins!")
elif user_choice == 'lizard' and comp_choice == 'scissors':
    print("computer wins!")

#Asume user chooses rock
elif user_choice == 'rock' and comp_choice == 'scissors':
    print("player wins!")
elif user_choice == 'rock' and comp_choice == 'lizard':
    print("player wins!")
elif user_choice == 'rock' and comp_choice == 'spock':
    print("computer wins!")
elif user_choice == 'rock' and comp_choice == 'paper':
    print("computer wins!")