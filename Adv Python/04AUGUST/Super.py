# Super 
# calling suoer class construtor from child class constructor using super()

# class A:
#     def __init__(self):
#         print("Super class constructor")

# class B(A):
#     def __init__(self):
#         print("Child class constructor")
#         super().__init__()
# b = B()


# # calling super class method from child class method using super()
# class A:
#     def m1(self):
#         print("Super class A:m1 method")
# class B(A):
#     def m2(self):
#         print("Child class B:m2 method")
#         super().m1()
# b = B()
# b.m2()


# # calling super class variable from child class method using super()
# class A:
#     x = 10
#     def m1(self):
#         print("Super class A:m1 method")

# class B(A):
#     x = 20
#     def m1(self):
#         print("Child class x variable",self.x)
#         print("Super class x variable",super().x)
# b = B()
# b.m1()


