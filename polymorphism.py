# create a 10 digit numbers where we can use for getting even and odd

class Number():
    def num(self):
        self.nums=[1,2,3,4,5,6,7,8,9,10]
        print(self.nums) 

class Even(Number):
    def get_even(self):
        for i in range(11):
            if i%2==0:
                print(i)

class odd(Number):
    def get_odd(self):
        for i in range(11):
            if i%2!=0:
                print(i)
    

call=Number()
even=Even()
even.get_even()
Odd=odd()
Odd.get_odd()

