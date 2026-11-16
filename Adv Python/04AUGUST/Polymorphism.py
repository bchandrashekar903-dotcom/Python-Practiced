'''Adding complex numbers'''

class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img
    # def cal(self,complex): 
    def __add__(self,num2):     #dundar function to add the numbers
        newreal = self.real+num2.real
        newimg = self.img+num2.img
        return Complex(newreal,newimg)

    def __sub__(self,num3):
        newreal = self.real-num3.real
        newimg = self.img-num3.img
        return Complex(newreal,newimg)

    def display(self):
        print(f"{self.real}i + {self.img}j")

c1 = Complex(2,4)
c2 = Complex(3,7)
c3 = c1+c2
c3.display()
c4 = c1-c2
c4.display()
# c3 = c1.cal(c2)    #c2 acts as a value for complex