import sys
if len(sys.argv) == 1:
    quit()
number_list = ["1","2","3","4","5","6","7","8","9","0"]
del sys.argv[0]
credit_card = list("".join(sys.argv))
empty_credit_card = list()
count = 0
summation = 0
check_digit = 0
checked = False

def sumList(list):
    count = 0
    for thing in list:
        count+=thing
    return count

for thing in range(len(credit_card)):
    val = credit_card[len(credit_card)-1-thing]
    if val in number_list:
        if not checked:
            check_digit+=int(val)
            checked = True
        else:
            val = int(val)
            if count%2==0:
                val*=2
            if val>=10:
                val-=9
                empty_credit_card.append(val)
            else:
                empty_credit_card.append(val)
            count+=1

print(empty_credit_card)
print(sumList(empty_credit_card))
print(check_digit)
if summation%10==check_digit:
    print("Credit card number is valid")
else:
    print("Credit card number is invalid")
