import os
import timeit
import re

def writeNextFile(contents, file):
    fh = open(file,"w")
    fh.write(contents)

def runNextFile(contents, num):
    file = "./start" + num + ".py"
    writeNextFile(contents, file)
    # os.system("python " + file)
    # quit()

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
        return False

def split_by_func(contents):
    func_list = {}
    starting = False
    curr_search = ""
    curr_index = 0
    contents = contents.split("\n")
    for index,x in enumerate(contents):
        if starting:
            if not x.split() and not contents[index + 1][0].isspace():
                func_list[curr_search] = [curr_index,index]
                curr_search = ""
                starting = False
        elif x[0:3] == "def":
            starting = True
            curr_index = index + 1
            curr_search = re.split("\s|\(",x)[1]
    return func_list

def rewrite(contents, line, where, what, one_indent, functions=None):
    special_words = ["def","if","elif","else","try","except","for","class","with","while","finally"]
    contents = contents.split("\n")
    new_contents = []
    searching = False
    removeUntil = 0
    remove = False
    for index,x in enumerate(contents):
        if line in x:
            indents = ""
            for z,y in enumerate(x):
                if not y.isspace():
                    break
                else:
                    indents += y
            what = indents + what
            f_word = x.split()[0]
            func_name = re.split("\s|\(",line)[1]
            if functions and func_name in functions:
                removeUntil = functions[func_name][1]
            if f_word in special_words:
                what = one_indent + what
            if where == "prepend":
                new_contents.append(x)
                new_contents.append(what)
            elif where == "append":
                searching = True
                new_contents.append(x)
                # if after function, append "what" at end
            elif where == "remove":
                new_contents.append(x)
                new_contents.append(what)
                remove = True
                searching = True
                # find function or conditional contents, replace all with "what"
        elif searching:
            if index < removeUntil + 1:
                if not remove:
                    new_contents.append(x)
            else:
                if not remove:
                    new_contents.append(what)
                new_contents.append(x)
                searching = False
                remove = False
            #print("searching for end of function")
        else:
            #if searching:
            new_contents.append(x)
    return "\n".join(new_contents)

def addInfo(content, file_spec):
    os_stat_list = ["MODE", "INO", "DEV", "NLINK", "UID", "GID", "SIZE", "ATIME", "MTIME", "CTIME", "FILENUM", "PREVFILENAME"]
    file_name = file_spec[1]
    file_spec = list(os.stat(file_name)) + file_spec
    new_file_spec = "previous_file_spec = {"
    for i,x in enumerate(file_spec):
        x_key = "\"" + os_stat_list[i] + "\":"
        x_val = str(x)
        if is_number(x):
            new_file_spec += x_key + x_val + ","
        else:
            new_file_spec += x_key + "\"" + x_val + "\"}"
    content = content.split("\n")
    if content[0][0] == "p":
        content[0] = new_file_spec
    else:
        content.insert(0, new_file_spec)
    return "\n".join(content)

if __name__ == "__main__":
    this_file = __file__.split(".")[0]
    file_open = open(__file__,"r")
    file_number = str(int(this_file[5:len(this_file)]) + 1)
    file_content = file_open.read()
    func_list = split_by_func(file_content)
    file_content = addInfo(file_content, [file_number,__file__])
    file_content = rewrite(file_content, "def writeNextFile", "remove", "print(\"data\")", "    ", func_list)
    runNextFile(file_content, file_number)
