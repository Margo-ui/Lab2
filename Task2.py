class Count:
    def func(self, fname):
        self.file = open(fname, "r")

        self.number_of_lines = 0
        self.number_of_words = 0
        self.number_of_characters = 0
        for line in self.file:
          self.line = line.strip("\n")
          self.words = line.split()
          self.number_of_lines += 1
          self.number_of_words += len(self.words)
          self.number_of_characters += len(self.line)

        self.file.close()
        print("lines:", self.number_of_lines, "words:", self.number_of_words, "characters:", self.number_of_characters)
fname = 'File1.txt'
a = Count()
try:
    a.func(fname)
except:
   print('File not found')