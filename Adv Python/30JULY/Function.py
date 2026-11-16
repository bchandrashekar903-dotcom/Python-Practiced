# Function to check a given number is even or odd
 
# def even_odd(n):
#     if n%2==0:
#         return f'Even : {n}'
#         # return ('Even is',n)
#     else:
#         return f'Odd is {n}'
# n = eval(input("Enter the number:"))
# print(even_odd(n))

# # Function to find max and min of a list
# def max_min(lst):
#     max = lst[0]
#     min = lst[0]
#     for i in lst:
#         if i>max:
#             max = i
#         if i<min:
#             min = i
#     return max,min
# lst = list(map(int,input("Enter the numbers:").split()))
# max,min = max_min(lst)
# print("Maximum number:",max)
# print("Minimum number:",min)

# def max_min(a,b):
#     if a>b:
#         return f'Maximum is :{a}',f'Minimum is :{b}'
#     else:
#         return f'Minimum is :{a}',f'Maximum is :{b}' 

# print(max_min(eval(input("Enter number:")),eval(input("Enter 2 number:"))))

    
# Function can be - Assign a function -> to a variable

# # define function
# def add(a,b):
#     return a+b

# # call function
# x = add(10,20)
# print(x)    


# # Function within the function
# def disp(str):
#     def msg():
#         return 'Welcome to '
#     result = msg()+str
#     return result
# print(disp("Python programming"))


# # def function variable length arguments -> *args

# def disp(*args):
#     for i in args:
#         print(i)
# disp('Hello','wolcome','to','python','programming')


# # define function to add by **kwargs

# def disp(**kwargs):
#     for key,value in kwargs.items():
#         print('key={}, value={}'.format(key,value))
#         print(f'key = {key} , value = {value}')
# disp(name = 'Muneeb',age=22,city='Karachi')

# # Local and Gobal variables Scope of the function
# a = 10             #Global
# print(a)
# def myfun():
#     a = 20          #Local
#     print(a)
# myfun()
# print(a)

# # Global keyword to access the entire value
# a = 10             #Global
# print(a)
# def myfun():
#     global a        #this will assign the value to the entire program
#     a = 20          #Local
#     print(a)
# myfun()
# print(a)





 


