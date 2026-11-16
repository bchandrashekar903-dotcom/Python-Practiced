# Passing members of a class to another class

# class Employee:
#     def __init__(self,name,sal):
#         self.name = name
#         self.sal = sal

#     def disp(self):
#         print(f"Name is {self.name}\nSalary is {self.sal}")

# class Sal_incr:
#     # Method
#     def incr(e):
#         e.sal += e.sal*0.1
#         e.disp()

# e=Employee("John",5000)
# Sal_incr.incr(e)
 

class Person:
    def __init__(self, name, sal):
        self.name = name
        self.sal = sal

    def disp(self):
        print(f"Name is {self.name}")

    class DOB:
        def __init__(self, dd, mm, yyyy):
            self.dd = dd
            self.mm = mm
            self.yyyy = yyyy

        def show(self):
            print(f"DOB is {self.dd}/{self.mm}/{self.yyyy}")

class Sal_incr:
    def incr(e):
        e.sal += e.sal * 0.1
        e.disp()
        print("Updated Salary:", e.sal)


# Create Person object
p = Person("John", 50000)
p.disp()

# Create DOB object
d = Person.DOB(15, 8, 1947)
d.show()

# Increase salary
Sal_incr.incr(p)