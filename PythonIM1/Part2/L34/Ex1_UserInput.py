ask = True
name = ["rock", "paper", "scissors", "lizard", "spock"]
print("chooses rock, paper, scissors, lizard or spock")
while ask == True:
    a = input("please try to write the exact name")
    if a.lower() in name:
        ask = False

print("Finish")