# Sets

set1 = {1,12,3,4,56,6}
set2 = {3,4,5,7,9}
set3 = {3,6,4}

# Length of list
lst = list(set1)
lst.extend(list(set2))
lst.extend(list(set3))
print()
print("List is:",lst)
print("Length of List is :",len(lst))
print()

# Union ,Intersection, Difference
set_u = set1.union(set2,set3)
set_i = set1&set2&set3
set_d= set1.difference(set2,set3)
print(f"Union :{set_u}\nIntersection :{set_i}\nDifference :{set_d}")
print()

# Missing values
full_range = set(range(min(lst), max(lst) + 1)) 
missing = full_range - set(lst)
print()

# Frequency of the numbers
for i in lst:
    print(i,f"repeated:{lst.count(i)} times")
print()

# Max and min element
set = set(lst)
print("Max value :",max(lst))
print("Min value :",min(lst))
print()

# Average values
sum = 0
for i in lst:
    sum+=i
avg = sum/len(lst)
print("Average values :",avg)
print()

print("Missing items:", sorted(missing)) 
print()

# Common elements
common = set1&set2&set3
print("Common elements are:",common)
print()
 





