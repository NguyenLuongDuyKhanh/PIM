import random

name_to_num = {
    "rock": 0,
    "spock": 1,
    "paper": 2,
    "lizard": 3,
    "scissors": 4
}

name = ["rock", "paper", "scissors", "lizard", "spock"]
print("chooses rock, paper, scissors, lizard or spock")
ask = True
while ask == True:
    player_choice = input("please try to write the exact name")
    if player_choice.lower() in name:
        ask = False

print()
print("player chooses", player_choice)
player_num = name_to_num[player_choice]

comp_choice = random.choice(name)
comp_num = name_to_num[comp_choice]
print("computer chooses", comp_choice)

if (player_num - comp_num) % 5 >= 3 and (player_num - comp_num) % 5 <= 4:
    print("computer wins!")
elif (comp_num - player_num) % 5 >= 3 and (comp_num - player_num) % 5 <= 4:
    print("player wins!")
else:
    print("it's a tie!")


