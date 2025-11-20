##辗转相除法/欧几里得算法
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    
def gcd2(a,b):
    while b>0:
        r=a%b
        a=b
        b=r
    return a

##应用：实现分数运算
class Fraction:
    def __init__(self,a,b): ###分子numerator：a；分母denominator
        self.a=a
        self.b=b
        x=self.gcd(a,b)
        self.a/=x
        self.b/=x

    def gcd(self,a,b):
        while b>0:
            r=a%b
            a=b
            b=r
        return a

    def zgs(self,a,b):
        x=self.gcd(a,b)
        return a*b/x

    def __add__(self,other):
        a=self.a
        b=self.b
        c=other.a
        d=other.b
        denominator=self.zgs(b,d)
        numerator=a*(denominator/b)+c*(denominator/d)
        return Fraction(numerator,denominator)

    def __str__(self):
        return "%d/%d"%(self.a,self.b)
    
f=Fraction(30,16)
print(f)
a=Fraction(1,3)
b=Fraction(1,2)
print(a+b)