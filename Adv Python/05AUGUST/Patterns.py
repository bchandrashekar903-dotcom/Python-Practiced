# '''             Square Pattern              '''
# n = 4
# for i in range(n):
#     for j in range(n):
#         print("*",end = " ")
#         # print(i+1,end = " ")
#     print("\n")
# print("     This is the Square Pattern         \n")


# '''        Right angled triangle  Pattern       '''
# n = 4
# for i in range(n):
#     print("*   " * (i+1))
#     print("\n")
# print("     This is the Right angled triangle  Pattern       \n")


# '''       Fourth quadrant pattern              '''
# n= 4
# for i in range(n):
#     for j in range(i,n):
#         print("* ",end = " ")
#     print("\n")


# '''        Right angled triangle  Pattern   (Alphabets)   '''
# n = 4
# for i in range(n):
#     for j in range(i+1):
#         print(chr(65+j),end = " ")
#     print("\n")


'''     Floyd's Triangle (prints(1st value as 1 and next increments in every next row))            '''
# num= 1
# n = 4
# for i in range(n):
#     for j in range(i+1):
#         print(num,end = " ")
#         num+=1

#     print("\n")


# '''   Floyd's Triangle (prints(1st value as "A" and next increments in every next row))            '''

# alpha = 65
# n = 4
# for i in range(n):
#     for j in range(i+1):
#         print(chr(alpha),end = " ")
#         alpha+=1
#     print("\n")

'''   Floyd's Triangle (A,B,C,D in reverse order)    '''

# alpha = 65
# n = 4
# for i in range(n-1,-1,-1):
#     for j in range(i+1):
#         print(chr(alpha),end = " ")
#         alpha+=1
#     print("\n")

# alpha = 65
# n = 4
# for i in range(n-1,-1,-1):
#     for j in range(i+1):
#         print( "*",end = " ")
#     print("\n")


'''          Pyramid pattern         '''
# Using one for loop
# n= 4
# for i in range(n):
#     print(" "*(n-i-1) +"* "*(i+1))


# Using two for loops
# n = 4
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end = "")
#     for k in range(i+1):
#         print("* ",end = "")
#     print()

# '''               Pyramid  Steps Pattern   ''' 
# n = 4
# for i in range(n):
#     for j in range(n-i-1):
#         # Modify in spaces to change the structure of the pattern
#         print(" ",end = " ")
#     for k in range(2*i+1):
#         print("* ",end = "")
#     print()

'''          Inverted Pyramid         '''
# n = 4
# for i in range(n-1,-1,-1):
#     print(" "*(n-i-1) + "* "*(i+1))





'''                 Hallow Square Pattern              '''

# n = 5
# for i in range(n):
#     for j in range(n):
#         if (i == 0 or i == n-1 or j == 0 or j == n-1):
#             print("*",end = " ")
#         else:
#             print(" ",end = " ")
#     print()


'''         Hallow Hover class Pyramid       '''
# n = 4
# for i in range(n-1,-1,-1):
#     print(" "*(n-i-1) + "* "*(i+1))
# for i in range(1,n):
#     print(" "*(n-i-1) + "* "*(i+1))


'''           Hallow Right Angle Triangle 1st Quadrant           '''

# n = 4
# for i in range(n):
#     for j in range(i+1):
#         if i==n-1 or j==0 or i==j:
#             print("*" ,end = " ") 
#         else:
#             print(" ",end = " ")
#     print()


# '''           Hallow Daimond             '''

# n = 4
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end = "")
#     for j in range(i+1):
#         if j == 0 or i==j:
#             print("*" ,end = " ") 
#         else:
#             print(" ",end = " ")
#     print()
# n = 4
# for i in range(n-2,-1,-1):
#     for j in range(n-i-1):
#         print(" ",end = "")
#     for j in range(i+1):
#         if j == 0 or i==j:
#             print("*" ,end = " ") 
#         else:
#             print(" ",end = " ")
#     print()


'''            Hallow Pyramid                    '''
# # Reverse of the pyramid pattern
# n = 4
# for i in range(n-1,-1,-1):
#     for j in range(n-i-1):
#         print(" ",end = "")
#     for j in range(i+1):
#         if  i == n-1 or j == 0 or i==j:
#             print("*" ,end = " ") 
#         else:
#             print(" ",end = " ")
#     print()

'''             Normal of the hallow pyramid pattern      '''
# n = 4
# for i in range(1,n):
#     for j in range(n-i-1):
#         print(" ",end = "")
#     for j in range(i+1):
#         if i == n-1 or j == 0 or i==j:
#             print("*" ,end = " ") 
#         else:
#             print(" ",end = " ")
#     print()

'''           Hallow Odd sequence pattern of pyramid        '''
 
# n = 10
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end = " ")
#     for k in range(2*i+1):
#         if k == 0 or k == 2*i:
#             print("* " ,end = " ") 
#         else:
#             print(" ",end = " ")
#     print()
# n =10
# for i in range(n-2,-1,-1):
#     for j in range(n-i-1):
#         print(" ",end = " ")
#     for k in range(2*i+1):
#         if k == 0 or k == 2*i:
#             print("* " ,end = " ") 
#         else:
#             print(" ",end = " ")
#     print()
 

'''           Square and X pattern     '''
n = 11
for i in range(n):
    for j in range(n):
        if (i==0 or i==n-1 or i==j or j==n-i-1 or j==0 or j==n-1):
            print("*  ",end = " ")        # i+j == n-1    
        else:
            print("  ",end = "  ")
    print()




 