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