class Rectangle:
   def __init__(self, length=1, width=1):
       if length in range(0, 20) and width in range(0, 20):
         self.length = length
         self.width = width
       else :
        print("wrong diapason")
   def get_len(self):
       return self.length
   def get_wid(self):
       return self.width
   def Area(self):
       return self.length * self.width
   def Perimeter(self):
       return 2 * (self.length + self.width)
   def Print(self):
       print(str(self.length) + " X " + str(self.width))
l = float(input("Enter the length: "))
w = float(input("Enter the width: "))
a = Rectangle(l, w)
print(str(a.Area()) + " " + str(a.Perimeter()))
a.Print()