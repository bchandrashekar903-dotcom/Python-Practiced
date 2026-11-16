# Tuples
# Creating tuples and concatenating and converting into list
tpl_a = (1,34,1,4,32,4)
tpl_b = (1,2,65,4,34,2)
tpl = tpl_a.__add__(tpl_b)
lst = sorted(tuple(set(tpl)))
print(lst)
print("The third max number is :",lst[-3])

# Splitting them into 2 halves
low = 0
high = len(lst)-1
mid = (low+high)//2
# if mid%2==0:
print(lst[:mid+1]," ",lst[mid+1:])
lst.sort()

# Frequency of the number
for i in tpl:
    print(f"{i} repeated : {tpl.count(i)} times")

# Removing duplicates
def duplicate(tp):
    sets = set()
    result=[]
    for i in tp:
        if i not in sets:
            sets.add(i)
            result.append(i)
    result.sort()
    return result
print(duplicate(lst))

unique = sorted(tuple(set(lst)))
print("After removing duplicates",unique)


for i in lst:
    if i%3 == 0:
        print(n)


 
 

