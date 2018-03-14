import string
import math

def power(op1, op2):
    return math.pow(op1, op2)

def divide(op1, op2):
    return op1/op2

def mult(op1, op2):
    return op1*op2

def add(op1, op2):
    return op1+op2

def sub(op1, op2):
    return op1-op2

operate = {
# list values in the form of [precedence, associativity, function]
    "^": [4, "right", power],
    "/": [3, "left", divide],
    "*": [3, "left", mult],
    "+": [2, "left", add],
    "-": [2, "left", sub]
}

operators = list(operate.keys())

def polish(arr):
    queue = []
    for el in arr:
        if el in operators:
            #do operator stuff
            # operate on the two numbers in the queue and push result
            queue.append(operate[el][2](int(queue.pop(0)), int(queue.pop(0))))
        else:
            queue.append(el)
    if queue:
        return queue[0]
    else:
        print("Errors!!")

def shunting(eq):
    # initialize correct stacks/queues
    operator_stack = []
    queue = []
    while eq:
        token = eq[0]
        if token.isdigit():
            queue.append(token)
        elif token in operators:
            if operator_stack:
                while operator_stack and operator_stack[-1] != "(" and ((operate[operator_stack[-1]][0] > operate[token][0]) or (operate[operator_stack[-1]][0] == operate[token][0] and operate[operator_stack[-1]][1] == "left")):
                    print("token: " + token)
                    queue.append(operator_stack.pop(-1))
            operator_stack.append(token)
        elif token == "(":
            operator_stack.append(token)
        elif token == ")":
            try:
                while operator_stack[-1] != "(":
                    queue.append(operator_stack.pop(-1))
                operator_stack.pop(-1)
            except IndexError:
                print("There was an error with parenthesis")
                return []
        eq.pop(0)
    while operator_stack:
        queue.append(operator_stack.pop(-1))
    return queue


def tokenize(eq):
    # returns array of tokens (eg. 100 is not 1,0,0)
    token = ""
    tokens = []
    for inx in range(len(eq)):
        if eq[inx].isdigit():
            # print("token: " + token + " eq[inx]: " + eq[inx])
            token += eq[inx]
        elif eq[inx] in operators:
            tokens.append(token)
            token = eq[inx]
            tokens.append(token)
            token = ""
        else:
            # add variable tokens here! (eg. 2x = 2*x)
            if token:
                tokens.append(token)
                token = ""
        if inx == len(eq)-1:
            tokens.append(token)
    return tokens

if __name__ == "__main__":
    eq = input("What is your input equation to solve? \n").lower()
    eq = tokenize(eq)
    print(polish(shunting(eq)))
