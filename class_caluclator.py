class twovalue :
    def __init__(self,a,b):
        self.a=a
        self.b=b

class sums(twovalue):
    def sum(self):
        addition=self.a+self.b
        return addition
class minus(twovalue):   
    def subt(self):
        subtract=self.a-self.b
        return subtract
class mul(twovalue):   
    def mult(self):
        multiple=self.a*self.b
        return multiple

class div(twovalue):
    def divd(self):
        division=self.a/self.b
        return division
    
print("="*30)
while True:
    operator=int(input("enter the operator number : \n"))
    a=int(input("enter the first variable\n"))
    b=int(input("enter the second variable \n"))
    if operator==1:
        x=sums(a,b)
        print(x.sum())
    elif operator==2:
        x=minus(a,b)
        print(x.subt())
    elif operator==3:
        x=mul(a,b)
        print(x.mult())
    elif operator==4:
        x=div(a,b)
        print(x.divd())
    elif operator==0:
        break
    else:
        print(" oops try again! \n  you enter wrong operator ")
    