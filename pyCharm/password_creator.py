from random import randint
import string
invalidChars = set(string.punctuation.replace("_", ""))
list_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()1234567890"


def request_word():
    special_word = raw_input("Type a special word if you want one, otherwise type 'q'. ")
    if special_word == 'q':
        special_word = ''
    return special_word


def request_length():
    pass_length_here = int(raw_input("How long would you like the password? "))
    while pass_length_here > 20:
        print "Please keep the length under 21"
        pass_length_here = int(raw_input("How long would you like the password? "))
    return pass_length_here


def request_amount():
    num_pass_here = int(raw_input("How many passwords do you want? "))
    while num_pass_here > 8:
        print "Please keep the amount under 9"
        num_pass_here = int(raw_input("How many passwords do you want? "))
    return num_pass_here


def check_pass(pass_name):
    pass_name = list(pass_name)
    if not any(x.isupper() for x in pass_name):
        pass_name.append(list_characters[randint(26, 51)])
    if not any(x.islower() for x in pass_name):
        pass_name.append(list_characters[randint(0, 25)])
    if not any(x.isdigit() for x in pass_name):
        pass_name.append(str(randint(0, 10)))
    if not any(char in invalidChars for char in pass_name):
        pass_name.append(list_characters[randint(52, 61)])
    return "".join(pass_name)

pass_length = request_length()
num_pass = request_amount()
my_word = request_word()
passwords = []
count = 0


def create_password(lengthy, word):
    password = ""
    if len(word) > 1:
        word = list(word)
        word[1] = str(randint(0, 10))
        word = "".join(word)
    for things in range(lengthy-len(word)):
        password += list_characters[randint(0, len(list_characters)-1)]
    password = list(password)
    password.insert(randint(0, len(password)-1), word)
    return "".join(password)

while count < num_pass:
    passwords.append(create_password(pass_length, my_word))
    count += 1

for thing in passwords:
    print check_pass(thing[0:pass_length])
