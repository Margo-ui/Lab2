class Rational:
    def gcd(self, a, b):
        if (self.a == 0):
            return self.b
        elif (self.b == 0):
            return self.a
        elif (self.a == self.b):
            return self.a
        elif (self.a > self.b):
            return gcd(self.a - self.b, self.b)
            return gcd(self.a, self.b - self.a)
    def __init__(self, x=1, y=1):
        self.num = x
        self.denom = y
        if (y == 0):
            self.denom = 1
    def fraction(self):
        self.x = str(self.num)
        self.y = str(self.denom)
        return self.x + "/" + self.y
    def decimal(self, place):
        self.no = float(self.num / self.denom)
        self.str = str(self.no)
        return self.str
r1 = Rational(3, 6);
r2 = Rational(4, 10);
print(str(r1.fraction()) + " " + str(r1.decimal(2)))
print(str(r2.fraction()) + " " + str(r2.decimal(2)))