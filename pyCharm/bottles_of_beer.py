def bottles(num):
    x = str(num)
    print(x + " Bottles of beer on the wall, " + x + " bottles of beer, take one down, pass it around, " + str(num-1) + " bottles of beer on the wall")

count = 5
while count > 0:
    bottles(count)
    count -= 1
