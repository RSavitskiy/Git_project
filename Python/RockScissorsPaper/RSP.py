import random

game = ["rock", "scissors", "paper"]
sp = 0
fp = 0
games = 0
while (fp < 3 and sp < 3):
    firstPlayer = random.choice(game)
    secondPlayer = random.choice(game)
    print("first player " + firstPlayer)
    print("second player " + secondPlayer)

    if ((firstPlayer == "rock") and (secondPlayer == "rock")):
        games = games + 1
        print("let's play ")

    if ((firstPlayer == "paper") and (secondPlayer == "paper")):
        games = games + 1
        print "let's play"

    if ((firstPlayer == "scissors") and (secondPlayer == "scissors")):
        games = games + 1
        print "let's play"

    if ((firstPlayer == "paper") and (secondPlayer == "rock")):
        print "win first player"
        games = games + 1
        fp = fp + 1
    if ((firstPlayer == "paper") and (secondPlayer == "scissors")):
        print "win second player"
        games = games + 1
        sp = sp + 1
    if ((firstPlayer == "scissors") and (secondPlayer == "rock")):
        print("win second player")
        games = games + 1
        sp = sp + 1
    if ((firstPlayer == "scissors") and (secondPlayer == "paper")):
        print("win first player")
        games = games + 1
        fp = fp + 1
    if ((firstPlayer == "rock") and (secondPlayer == "paper")):
        print "win second player"
        games = games + 1
        sp = sp + 1
    if ((firstPlayer == "rock") and (secondPlayer == "scissors")):
        print "win first player"
        games = games + 1
        fp = fp + 1
    print("--------")

print(fp)
print(sp)
print(games)

if sp == 3:
    print("after " + str(games) + " games win second player")
if fp == 3:
    print("after " + str(games) + " games win first player")





