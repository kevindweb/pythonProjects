# make map of character count
# count amount of symbols greater than 0
# create nodes with symbols of similar count, starting with lowest (non-zero)
# if uneven, count last with next highest count
# create huffman tree
# set binary representations for all letters in tree
import os.path as path
import operator


class Tree(object):
    def __init__(self, left=None, right=None, data=None):
        self.left = left
        self.right = right
        self.data = data

    def __str__(self, level=0):
        ret = "\t" * level + str(self.data) + "\n"
        if typeCheck(self.left, "Tree"):
            ret += self.left.__str__(level + 1)
        else:
            ret += self.left.__str__()

        if typeCheck(self.right, "Tree"):
            ret += self.right.__str__(level + 1)
        else:
            ret += self.right.__str__()
        return ret


def char_map(text):
    my_map = {}
    arr = []
    for x in text:
        if x in my_map:
            my_map[x] += 1
        else:
            my_map[x] = 1
    sorted_arr = sorted(my_map, key=my_map.__getitem__)
    for item in sorted_arr:
        arr.append((item, my_map[item]))
    return arr


def custom_sum(arr):
    this_sum = 0
    # array will have only two elements
    # can only hold two different data types, tuple(character, count) or Tree(as seen above)
    for i in range(2):
        if type(arr[i]).__name__ == "list":
            this_sum += arr[i][1]
        else:
            this_sum += arr[i].data
    return this_sum


def typeCheck(obj, typ):
    return type(obj).__name__ == typ


def parseNode(obj, binary):
    left = obj.left
    right = obj.right
    if typeCheck(left, "Tree"):
        parseNode(left, binary + "0")
    else:
        left.append(binary + "0")
    if typeCheck(right, "Tree"):
        parseNode(right, binary + "1")
    else:
        right.append(binary + "1")


def findValue(char, tree):
    # returns the binary value for the specific character
    if typeCheck(tree.left, "Tree"):
        val = findValue(char, tree.left)
        if val:
            return val
    elif tree.left[0] == char:
        return tree.left[2]

    if typeCheck(tree.right, "Tree"):
        val = findValue(char, tree.right)
        if val:
            return val
    elif tree.right[0] == char:
        return tree.right[2]
    return None


def parseText(text, tree):
    text_parser = {}
    encoded = ""
    for i in text:
        if i in text_parser:
            encoded += text_parser[i]
        else:
            binary = findValue(i, tree)
            if binary:
                text_parser[i] = binary
                encoded += binary
            else:
                print("i: " + i)
    print("encoded: " + encoded)
    print(text_parser)

if __name__ == "__main__":
    response = input("Is your text in a file (y/n)? ")
    # get input in correct format from user for compression
    in_file = True
    text = ""
    if "y" in response.lower():
        while True:
            file_loc = input("What is the file location: ")
            if path.isfile(file_loc):
                break
            else:
                print("The file does not exist...")
        with open(file_loc, "r") as this_file:
            text = this_file.read()
    else:
        in_file = False
        text = input("Gimme your string: ")
    # descending array of characters in order of count
    sort_arr = char_map(text)
    for tupleEl in range(0, len(sort_arr)):
        sort_arr[tupleEl] = list(sort_arr[tupleEl])
    arr_copy = sort_arr[:]
    # for every iteration
    # sum the lowest two numbers (whether it be a node or tuple)
    # create a node from the sum
    # remove the two lowest
    while(len(sort_arr) > 1):
        curr_data = sort_arr[:2]
        # put first two element in this array
        curr_sum = custom_sum(curr_data)
        # sum the elements
        node = Tree(curr_data[0], curr_data[1], curr_sum)
        sort_arr = [node] + sort_arr[2:]
    root = sort_arr[0]
    # created the tree, now we have to assign binary values, 0 on left, 1 on right
    parseNode(root, "")
    parseText(text, root)
