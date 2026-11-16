# # Take range from 1 -30 and add 1-10 11-20 21-30

# sum_10 = 0
# sum_20 = 0
# sum_30 = 0
# for i in range(1,31):
#     if i<=10:
#         sum_10+=i
#     elif i>10 and i<=20:
#         sum_20+=i
#     elif i>20 and i<=30:
#         sum_30+=i
#     else:
#             break
# print("Sum of 10 numbers are:",sum_10)
# print("Sum of 20 numbers are:",sum_20)
# print("Sum of 30 numbers are:",sum_30)

# # Linear search
# lst = list(map(int,input("Enter the number:").split()))
# key = int(input("Enter the number:"))
# for i in lst:
#     if i == key:
#         found = 1
# if found:
#     print("Element found at :",i,"position")
# else:
#     print("Element not found")

# Factorial of a number from 1-30 range
m = int(input("Enter the starting point:"))
n = int(input("Enter the ending point:"))
fact = 1
def fact(n):
    for i in range(1,31):
        if n==1:
            return 1
        return n*fact(n-1)
num = int(input("Enter the number:"))
for i in range(m,n+1):
    f = fact(i)
    print(f"{i}! --> {f}")
    lst.append(f)
rs = []
for i in range(m,n+1):
    if i not in lst:
        rs.append(i)
print(rs)



 
    