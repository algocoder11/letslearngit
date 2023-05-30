class Sum():
    def __init__(self,a=0,b=0):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b

sums=Sum(5,10)

print("The Sum is", sums.add())

