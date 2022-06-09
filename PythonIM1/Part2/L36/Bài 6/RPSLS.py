import random


name_to_num = {
    "rock": 0,
    "spock": 1,
    "paper": 2,
    "lizard": 3,
    "scissors": 4
}
num_to_name = {
    0 : "rock",
    1 : "spock",
    2: "paper",
    3: "lizard",
    4 : "scissors"
}

def rpsls(player_choice):
    print()
    print("player chooses", player_choice)
    player_num = name_to_num[player_choice]
    comp_num = random.randrange(0,5)
    comp_choice = num_to_name[comp_num]
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
        print("please try to write the exact name")
        a = input()
        for i in range(5):
            if a.lower() == name[i]:
                ask = False
                break

    rpsls(a)

    print("do you want to try again? Y/N")
    ans = input()
    while ans.lower() != "y" and ans.lower() != "n":
        print("Y/N")
        ans = input()
    if ans == "y":
        game = True
    else:
        game = False
