'''Encapsulation -> where it will bind the data and functions'''

'''public -> can be accessible from anywhere in the program'''

'''Private attributes -> we cannot access the variables
 directly and these attributes are declared __ (double underscores)'''

'''Protected -> we cannot access the variables directly but we can access by 
using inheritance declared with _ (single underscores)'''

#  Private attribute and protected attribute
class Student:
    def __init__(self,name,sal):
        self._name = name
        self.__sal = sal

    def disp(self):
        print(self._name)    
        print(self.__sal)

s = Student("John",20000)
s.disp()
