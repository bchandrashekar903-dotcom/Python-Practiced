# # Count the number   of vowels,consonants,digitd,and special characters in a string

# str = "I Have Apple @ cost 23789"
# def count(str):
#     v=[];c=[];d=[];s=[]
#     for i in str: 
#         if i.isalpha():
#             i = i.lower()
#             if i in ['a','e','i','o','u']:
#                 v.append(i)
#             else:
#                 c.append(i)
#         elif i.isdigit():
#             d.append(i)
#         else:
#             s.append(i)
#     return v,c,d,s
# v,c,d,s= count(str)

# print("Vowels: ",v)
# print("Consonents: ",c)
# print("Digits: ",d)
# print("Special Characters: ",s)


# # Check whether a given string is a palindrome and list them in a separate lists

# str = input("Enter the string:").split(',')
# def palindrome(str):
#     if str == str[::-1]:
#         print(str,"is a Palindrome")
#     else:
#         print(str,"is not a Palindrome")
# palindrome(str)


# #Count the frequency of each character in a string
# str = input("Enter the string:")
# def frequency(str):
#     for i in str:
#         print(i,":",str.count(i))  
# frequency(str)

# # # Find the longest word in a sentence 
# str = input("Enter the string:").split()
# print("Largest :",max(str,key = len))
    

# # Remove duplicate characters from a string while preserving the original order
# str = input("Enter the string:") 
# def duplicate(str):
#     seen = set()
#     result=[]
#     for i in str:
#         if i not in seen:
#             seen.add(i)
#             result.append(i)
#     return result
# print(duplicate(str))

# ---------------------------LISTS-----------------------------#
# # Find the second largest element in a list
# l = list(map(int,input("Enter the numbers:").split()))
# l.sort()
# print(l[-2])

# # Separate even and odd numbers from a list
# lst = list(map(int,input("Enter the numbers:").split()))
# even = []
# odd =[]
# for i in lst:
#     if i%2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)
# print("Even numbers:",even)
# print("Odd numbers:",odd)


# Reverse duplicate elements from a list
# l = list(map(int,input("Enter the numbers:").split()))
# for i in l:


# Merge two lists and remove duplicate elements
# lst1 = list(map(int,input("Enter the numbers:").split()))
# lst2 = list(map(int,input("Enter the numbers:").split()))
# lst = lst1+lst2
# print(sorted(set(lst)))

# # Count the number of positive,negative,and zero elements in a list

# l = list(map(int,input("Enter the numbers:").split()))
# pos = [];neg = [];zero = []
# for i in l:
#     if i>0:
#         pos.append(i)
#     elif i<0:
#         neg.append(i)
#     else:
#         zero.append(i)
# print("Positive numbers:",sorted(pos))
# print("Negative numbers:",sorted(neg))
# print("Zero numbers:",zero)       

# # Reverse a string without using slices
# str = input("Enter the string:")
# rev = ""
# for i in str:
#     rev = i + rev
# print(rev)

# # Count the number of words in a sentence
# str = input("Enter the string:")
# w = 0
# for i in range(len(str)):
#     if str[i] == " ":
#         w+=1
# print(w+1)

# str = input("Enter the string:").split()
# c = 0
# for i in str:
#     c =c+1
# print(c)

# Replace a word which is present in 2 to 1 eg:10,20,30,40 -> 20,30,40,10
# # # str = input("Enter the string:").split()
# str = "This is a python programming".split()
# rev = str[0]
# for i in str:
#     rev = i+str
# print(str)

# numbers = [10, 20, 30, 40]
# l = input("Enter the numbers:").split(' ')
# first = l[0]
# l.remove(first)
# l.append(first)
# print(l)

# words = "This is a python programming" .split()
# print(" ".join(words[1:]+words[:1]))

# vowels = [a,a,a,e,i,o,u,u]



#'''''' Using Functions to apply different logics to make interactive program''''''#
# def even_odd(n):
#     even = set()
#     odd = set()
#     for i in n:
#         if i%2==0:
#             even.add(i)
#         else:
#           odd.add(i)
#     return even,odd
# n = list(map(int,input("Enter the numbers").split()))
# even,odd = even_odd(n)
# print("Even numbers:",even)
# print("Odd numbers:",odd)

# def replace(str):
#     first = str[0]
#     str.remove(first)
#     str.append(first)
#     return str
# str = input("Enter the strings").split(' ')
# print(replace(str))

# def count_n(n):
#     w = 0
#     for i in range(len(n)):
#         if n[i] == " ":
#             w+=1
#     return w
# n = list(map(int,input("Enter the numbers:").split()))
# counted_numbers = count_n(n)
# print(counted_numbers)

# 
def sum_avg(lst):
    sum = 0
    avg = 0
    for i in lst:
        sum+=i
    print("The sum of numbers:",sum)
    for i in lst:
        sum+=i
    l = len(lst)
    avg = sum/l
    print("The average of list:",avg)
lst = list(map(int,input("Enter the numbers:").split()))
print(sum_avg(lst))
 