import zlib, sys, base64, os

class Compress:
    '''This will compress any input and create a .kzc file'''
    def __init__(self, file_name):
        self.name = file_name
        this_text = open(file_name,"r").read()
        compress = base64.b64encode(zlib.compress(this_text,7))
        self.contents = compress
        self.size = sys.getsizeof(compress)

    def size_of(self):
        return self.size

    def complete(self):
        new_name = self.name + ".kzc"
        file_write = open(new_name,"w")
        file_write.write(self.contents)
        os.system("rm " + self.name)
