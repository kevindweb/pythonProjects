import zlib, sys, base64, os

class Decompress:
    '''This will decompress a .kzc file and return correct format'''
    def __init__(self,file_name):
        decompress = zlib.decompress(base64.b64decode(open(file_name,"r").read()))
        self.name = file_name
        self.contents = decompress
        self.size = sys.getsizeof(decompress)

    def size_of(self):
        return self.size

    def complete(self):
        original_file = self.name[0:-4]
        file_write = open(original_file,"w")
        file_write.write(self.contents)
        os.system("rm " + self.name)
