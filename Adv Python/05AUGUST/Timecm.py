'''      Big Oh(log n)   Palindrome checking   '''

# n = 123215
# rev = 0
# while n!=0:
#     digit = n%10
#     rev = rev*10+digit
#     n//=10
# if n==rev:
#     print("palindrome",rev)
# else:
#     print("Not a palindrome",rev)


'''         Big Oh(n logn)   Binary search    '''
# n = [7,9,8,6,5]
# n.sort()
# print(n)


'''         Big Oh(n)        Linear search     '''
# n = 4
# for i in range(n):
#     print(i)


'''           Big Oh(n^2)    Bubble sort       '''

# n=5
# for i in range(n):
#     for j in range(n):
#         print(i,j)
#     print()


 

'''         Big Oh(n+n)  is   '''
# for i in range(3):
#     print(i)
# print()
# for j in range(3):
#     print(i,j)
#         


'''        Fibonacci series     '''
# n = int(input("Enter the number:"))
# def fib(n):
#     if n==0 or n==1:
#         return n
#     else:
#         return fib(n-2)+fib(n-1)
# for i in range(n):
#     print(fib(i),end=" ")
    

''' Big Oh(n)            Fibonacci series using iterative method        '''
# n = int(input("Enter the number:"))
# a = 0
# b = 1
# print(a)
# print(b)
# for i in range(2,n+1):
#     c = a+b
#     a,b=b,c
#     print(c)\



'''        Check whether the given number is prime or not    '''
# n = int(input("Enter the number:"))
# for i in range(2,n):
#     if n%i==0:
#         print(f"{n} is not a Prime number")
#         break
# else:
#     print(f"{n} is a Prime number")

''' Using Functions Check whether the given number is prime or not    '''
def is_prime(n):
    for i in range(2,n):
        if n%i == 0:
            return "Not a prime"
        return "Prime"
n = int(input("Enter the number:"))
print(is_prime(n))

    
