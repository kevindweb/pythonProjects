import sys
if len(sys.argv) == 1:
    print "You need to type a number after the file name for the program to work"
    quit()
max_num = int(sys.argv[1])
min_num = 0
count = 0
print("This system will guess a number that you think of between 0 and " + str(max_num))
print "Type 'lower', 'higher', or 'exact' when prompted based on your number"


def ask_user():
    answer = raw_input("Type 'lower', 'higher', or 'exact' ")
    return answer
while True:
    count += 1
    middle = (max_num - min_num) / 2 + min_num
    print middle
    try_answer = ask_user()
    if try_answer == 'exact':
        print "Yay, it took " + str(count) + " tries"
        break
    elif try_answer == 'lower':
        max_num = middle
    else:
        min_num = middle

