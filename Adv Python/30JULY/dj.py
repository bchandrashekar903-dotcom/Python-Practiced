m = int(input("Enter the starting point: "))
n = int(input("Enter the ending point: "))

def factorial(num):
    if num == 0 or num == 1:
        return 1
    return num * factorial(num - 1)


lst = []

for i in range(m, n + 1):
    f = factorial(i)
    print(f"{i}! --> {f}")
    lst.append(f)

rs = []

for i in range(m, n + 1):
    if i not in lst:
        rs.append(i)

print("Numbers that are not factorial values:", rs)