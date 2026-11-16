'''              Recursion                '''
'''             Fibonacci using function  Big Oh(n)    '''
# def fib(n):
#     if n == 0 or n == 1:
#         return n
#     return fib(n-2)+fib(n-1)
# n = int(input("Enter the number:"))
# print(fib(n))

'''         Factorial using function       '''
# def fact(n):
#     if n == 0 or n == 1:
#         return 1
#     return n*fact(n-1)
# print(fact(5))


'''Function using iterative '''
# n = int(input("Enter the number:"))
# fact = 1
# while n!=0:
#     fact = fact*n
#     n = n-1
# print(fact)

# n = int(input("Enter the number:"))
# fact = 1
# for i in range(n,0,-1):
#     fact*=i
# print(fact)

'''        Palindrome using Two pointer '''
# def is_palindrome(s):
#     low = 0
#     high = len(s)-1
#     while low<high:
#         if s[low]!= s[high]:
#             return "Not a palindrome"
#         low+=1
#         high-=1
#     return "Palindrome"
# s = input("Enter the string:")
# print(is_palindrome(s))


'''Move Zeroe's to the end without altring the list     '''
# n = list(map(int,input("Enter the numbers:").split()))
# n.sort()
# for i in n:
#     if i==0:
#         n.remove(i)
#         n.append(i)
# print(n) 

# def moveZeroes(nums):
#     x = []
#     y = []
#     for num in nums:
#         if num != 0:
#             x.append(num)
#         else:
#             y.append(num)
#     nums = x+y
#     return nums
# print(moveZeroes([0,1,0,3,12]))


'''   Moving Zeroes Leet code     '''
# class Solution:
#     def moveZeroes(nums):
#         idx = 0
#         for i in range(len(nums)):
#             if nums[i]!=0:
#                 nums[idx]=nums[i]
#                 idx+=1
#         for i in range(idx,len(nums)):
#             nums[i]=0
# s = Solution()
# nums = list(map(int,input("Enter the numbers:").split()))
# s.moveZeroes(nums)
# print(nums)





'''Subsets ->  are part of set values that may be continue part or discontinues part 
and we have formula for subsets 2^n

Subarrays ->  doesn't contain empty arrays and discontinues parts are not allowed 

Subsequence -> is similar to subsets but empty sets are not allowed in subsequence'''
 

'''Minion Game Hackerrank'''
# def minion_game(string):
#     # your code goes here
#     vowels = 'AEIOU'
#     s_s  = 0
#     k_s = 0
#     for i in range(len(s)):
#         if s[i] in vowels:
#             k_s+=len(s)-i
#         else:
#             s_s+=len(s)-i
#     if k_s>s_s:
#         print("Kevin",k_s)
#     elif s_s>k_s:
#         print("Stuart",s_s)
#     else:
#         print("Draw")
# if __name__ == '__main__':
#     s = input("Enter the string:")
#     minion_game(s)


'''      Without using slicing reverse the string '''
# str = input("Enter the string:").split() 
# def reverse(str):
#     l = 0
#     r = len(str)-1
#     while(l<r):
#         str[l],str[r] = str[r],str[l]
#         l+=1
#         r-=1
#     return str
# print(reverse(str))


'''2nd minimum and 2nd maximmum '''
# lst = list(map(int,input("Enter the numbers:").split()))

# s = sorted(set(lst))
# print(s)

# print("2nd minimum: ",s[1])
# print("2nd maximum: ",s[-2])


# arr = list(map(int,input("Enter the numbers:").split()))
# small = float('inf')
# for i in arr:
#     if i<small:
#         small = i
# print(small)

# arr = list(map(int,input("Enter the numbers:").split()))
# smallest_1st = arr[0]
# largest_1st = arr[0]

# for i in arr:
#     if i<smallest_1st:
#         smallest_1st = i
# for i in arr:
#     if i>largest_1st:
#         largest_1st = i

# largest_2nd = float('-inf')
# smallest_2nd = float('inf')
# for i in  arr:
#     if largest_1st>i>largest_2nd:
#         largest_2nd = i
#     if smallest_1st<i<smallest_2nd:
#         smallest_2nd = i

# print("1st minimum: ",smallest_1st)
# print("2nd minimum: ",smallest_2nd)

# print("1st maximum: ",largest_1st)
# print("2nd maximum: ",largest_2nd)

'''          Prefix Sum of the array         '''
arr = [2,3,7,9]
p = [0]*(len(arr)+1)
for i in range(1,len(arr)+1):
    p[i] = p[i-1]+arr[i-1]
print(p)

'''        Suffix Sum of the array            '''
arr = [2,3,7,9]
s = [0]*(len(arr)+1)
for i in range(len(arr)-1,-1,-1):
    s[i] = s[i+1]+arr[i]
print(s)

