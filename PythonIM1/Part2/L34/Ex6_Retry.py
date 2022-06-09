import random

name_to_num = {
    "rock": 0,
    "spock": 1,
    "paper": 2,
    "lizard": 3,
    "scissors": 4
}
def rpsls(player_choice):
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
game = True
name = ["rock", "paper", "scissors", "lizard", "spock"]
while game:
    print("chooses rock, paper, scissors, lizard or spock")
    ask = True
    while ask == True:
        player_choice = input("please try to write the exact name")
        if player_choice.lower() in name:
            ask = False

    rpsls(player_choice)
    print("do you want to try again? Y/N")
    ans = input()
    while ans.lower() != "y" and ans.lower() != "n":
        print("Y/N")
        ans = input()
    if ans == "y":
        game = True
    else:
        game = False

