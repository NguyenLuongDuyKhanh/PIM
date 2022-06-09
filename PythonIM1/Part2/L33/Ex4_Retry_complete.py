# RPS
import random


RPS = ['rock', 'paper', 'scissors']
ans = 0
game = True

while game == True:
    while ans != 'rock' and ans!= 'paper' and ans!= 'scissors':
        print("choose rock, paper or scissors ")
        ans = str(input()).lower()

    print("you choose", ans)
    comp = random.choice(RPS)
    print("opponent choose", comp)

    if ans == "rock" and comp == "scissors":
        print("you won")
    elif ans == "scissors" and comp == "paper":
        print("you won")
    elif ans == "paper" and comp == "rock":
        print("you won")
    elif ans == comp:
        print("it's a tie")
    else:
        print("you lose")

    yn = 0
    while yn != "y" and yn != "no":
        yn = input("do you want to play again? Y/N ").lower()


    if yn == "y":
        game == True
        ans = 0
    else:
        game == False
        print('Bye!')
        break


