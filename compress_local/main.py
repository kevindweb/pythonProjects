import os, sys
from os.path import isfile, join
from classes.compress import Compress
from classes.decompress import Decompress

def get_all_files(directory_list, root_dir):
    if len(directory_list):
        print("repeat")
    else:
        

if __name__ == "__main__":
    file_path = sys.argv[1]
    files_list = []
    if not sys.argv[2] == "--directories":
        curr_dir = os.listdir(file_path)
        files_list = [f for f in curr_dir if isfile(join(file_path, f))]
    else:
        files_list = get_all_files([],file_path)

    print("file path",file_path)
    print(files_list)
    # c = Compress("alice_book.txt")
    # print "size:",c.size_of()
    # c.complete()
    # d = Decompress("alice_book.txt.kzc")
    # d.complete()
