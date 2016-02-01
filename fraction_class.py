def gcd(n, d):
  
    while d:
        n, d = d, n % d
    return n

class fraction(object):
    def __init__(self,n=None,d=None):
        self.numerator = n
        self.denominator = d

    def __str__(self):
        i = self.numerator // self.denominator
        num = self.numerator % self.denominator
        if i == 0:
             return "%s / %s" % (self.numerator , self.denominator)
        else:
             return "%s  %s / %s" % (i , (self.numerator % self.denominator) ,  self.denominator)

    def numerator(self,n):
        self.numerator = n 

    def denominator(self,d):
        self.denominator = d

    def __mul__(self,rhs):
        x = self.numerator * rhs.numerator
        y = self.denominator * rhs.denominator
        return fraction(x,y)

    def __add__(self, frac):
        sum = self.numerator * frac.denominator + frac.numerator * self.denominator
        g = gcd(sum, self.denominator * frac.denominator)
        return fraction(sum // g, self.denominator * frac.denominator // g)

		
		





if __name__ == '__main__':
    a = fraction(1,2)
    b = fraction(4,5)
    c = a * b
    print(c)
    c = a + b 
    print(c)
