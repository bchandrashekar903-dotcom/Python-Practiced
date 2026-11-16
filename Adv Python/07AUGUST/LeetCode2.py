'''    Lists   -> separating with and without brackets and commas   '''
# l = [1,2,4,3]
# print(*l)
# print(*l,sep = ",")


'''             Unpacking and packing the lists values      '''
# l = [1,2,3,4,5]
# first,*remaining,last = l
# print(first,remaining,last)


'''             Prefix and suffix product without except self             '''
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         p = [0]*n
#         s = [0]*n
#         ans = [0]*n
#         p[0]=nums[0]
#         for i in range(1,n):
#             p[i] = p[i-1]*nums[i]
#         s[n-1] = nums[n-1]
#         for i in range(n-2,-1,-1):
#             s[i]=s[i+1]*nums[i]
#         ans[0] = s[1]
#         ans[n-1]=p[n-2]
#         for i in range(1,n-1):
#             ans[i]=p[i-1]*s[i+1]
#         return ans
# product = Solution()
# print(product.productExceptSelf([1,2,3,4]))




# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         ans = [1]*n
#         p = 1
#         for i in range(n):
#             ans[i]= p
#             p = p* nums[i]
#         s = 1
#         for i in range(n-1,-1,-1):
#             ans[i]= ans[i]* s
#             s  =s*nums[i]
#         return ans
# product = Solution()
# print(product.productExceptSelf([1,2,3,4]))


# '''189. Rotate Array
# Given an integer array nums, rotate the array to the right by k steps, 
# where k is non-negative.  '''
# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         n = len(nums)
#         k = k%n
#         nums[:] = nums[n-k:]+nums[:n-k]
    
# rotate = Solution()
# print(rotate.rotate([1,2,3,4,5,6,7],3))   


# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         n = len(nums)
#         k = k%n
#         def rev(l,h):
#             while l<h:
#                 nums[l],nums[h] = nums[h],nums[l]
#                 l+=1
#                 h-=1
#         rev(0,n-1)
#         rev(0,k-1)
#         rev(k,n-1)

# arr = list(map(int,input("Enter the numbers:").split()))
# k = int(input("Enter the number:"))
# rotate = Solution()
# print(rotate.rotate(arr,k))  


'''118. Pascal's Triangle
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:'''

# class Solution:
#     def generate(self, numRows: int) -> List[List[int]]:
#         tri = []
#         for i in range(numRows):
#             row = [1]*(i+1)
#             for j in range(1,i):
#                 row[j] = tri[i-1][j-1]+tri[i-1][j]
#             tri.append(row)
#         return tri


'''54. Spiral Matrix
Given an m x n matrix, return all elements of the matrix in spiral order.'''

# class Solution:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         l = 0
#         r = len(matrix[0])-1
#         t = 0
#         b = len(matrix)-1
#         res = []
#         while t<=b and l<=r:
#             # left to right
#             for i in range(l,r+1):
#                 res.append(matrix[t][i])
#             t+=1
#             # top to bottom
#             for i in range(t,b+1):
#                 res.append(matrix[i][r])
#             r-=1
#             # right to left
#             if t<=b:
#                 for i in range(r,l-1,-1):
#                     res.append(matrix[b][i])
#                 b-=1
#             # bottom to top
#             if l<=r:
#                 for i in range(b,t-1,-1):
#                     res.append(matrix[i][l])
#                 l+=1
#         return res

# matrix = list(map(int,input("Enter the matrix:").split()))
# s = Solution()
# print(s.spiralOrder(matrix))


'''867. Transpose Matrix
Given a 2D integer array matrix, return the transpose of matrix
The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.'''

# class Solution:
#     def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
#         row= len(matrix)
#         col = len(matrix[0])
#         ans = [[0]*row for i in range(col)]
#         for i in range(row):
#             for j in range(col):
#                 ans[j][i] = matrix[i][j]
#         return ans

# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# s = Solution()
# print(s.transpose(matrix))


'''48. Rotate Image
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation. '''

# class Solution:
#     def rotate(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         n = len(matrix)
#         for i in range(n):
#             for j in range(i+1,n):
#                 matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
#         for row in matrix:
#             row.reverse()

# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# s = Solution()
# print(s.rotate(matrix))

'''Count no of vowels in a string     '''
# str = "bitm college"
# count = 0
# for i in str:
#     if i in ['a','e','i','o','u']:
#         count+=1
# print("The number of vowels in a string ",count)


'''242. Valid Anagram 
Given two strings s and t, return true if t is an anagram of s, and false otherwise. '''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        alpha = [0]*26
        for ch in s:
            alpha[ord(ch)-ord('a')]+=1
        for ch in t:
            if alpha[ord(ch)-ord('a')]==0:
                return False
            alpha[ord(ch)-ord('a')]-=1
        return True



'''205. Isomorphic Strings
Solved
Easy
Topics
premium lock icon
Companies
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 '''

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ch_s={}
        ch_t={}
        for i in range(len(s)):
            if s[i] not in ch_s:
                ch_s[s[i]]=i
            if t[i] not in ch_t:
                ch_t[t[i]]=i
            if ch_s[s[i]]!=ch_t[t[i]]:
                return False       
            
        return True