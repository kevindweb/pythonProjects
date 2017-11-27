my_file = open('another_test.js','r')
my_string_code = my_file.read()
inside_quotes = False
last_quote = ' '
previous_letter = 'null'
prev_letter = 'null'
var_list = []
two_previous = 'null'
space_here = False
comment_here = False
filter_comment = False

def testFilter(this_char):
    global inside_quotes
    global previous_letter
    global two_previous
    global last_quote
    global space_here
    global filter_comment
    if this_char=='r' and previous_letter=='a' and two_previous=='v':
        # var needs space after it
        space_here = True
    elif this_char=='n' and previous_letter=='o' and two_previous=='i':
        # ends in ion - "function"
        space_here = True
    elif this_char=='*' and previous_letter=='/':
        filter_comment = True
        print("starting comment")
    elif this_char=='/' and previous_letter=='*':
        filter_comment = False
        print('ending comment')
    elif (this_char=='\"' or this_char=='\'' or this_char=='`'):
        if last_quote==' ':
            last_quote = this_char
            inside_quotes = True
        elif last_quote==this_char:
            if inside_quotes:
                inside_quotes = False
            else:
                inside_quotes = True
        else:
            if not inside_quotes:
                inside_quotes = True
                last_quote = this_char
    if not previous_letter == "null":
        two_previous = previous_letter
    previous_letter = this_char
    if not inside_quotes:
        if this_char==" ":
            if space_here:
                space_here = False
                return True
            if filter_comment:
                return True
            return False
    if this_char==";":
        return False

    return True


def testMap(this_char):
    global prev_letter
    global comment_here
    return_char = this_char
    if prev_letter=="null":
        if this_char=="\n":
            return_char = ""
    elif prev_letter=="/" and this_char=="/":
        comment_here = True
        return_char = "*"
    else:
        if this_char=="\n":
            if comment_here:
                comment_here = False
                return_char = "*/;"
            elif not(prev_letter=="" or prev_letter==" " or prev_letter=="{" or prev_letter=="\n" or prev_letter==":"):
                return_char = ";"
            else:
                return_char = ""
    prev_letter = this_char
    return return_char

my_test_filter = list(filter(testFilter,list(my_string_code)))
my_test_map = list(map(testMap,my_test_filter))
print("".join(my_test_map))
