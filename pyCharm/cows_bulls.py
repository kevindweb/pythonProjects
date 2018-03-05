from random import randint
print "Let's play a game called cows and bulls"
num = str(randint(1000, 9999))
cows = 0
bulls = 0


def user_guess():
    new_guess = raw_input("Type a four digit number")
    if new_guess == num:
        print "Yay you got the number"
        print "Total: %i cows, %i bulls" % (cows, bulls)
        return
    for thing in range(0, len(new_guess)):
        if num[thing] == new_guess[thing]:
            cows += 1
        elif num[thing + 1] == new_guess[thing] or /
            num[thing]

