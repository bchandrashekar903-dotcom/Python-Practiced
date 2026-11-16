''' Range values '''

# '''                Printing table values                    '''
# n = int(input("Enter the number: "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(i*j,end="\t")
#     print()


'''               Printing matrix           '''
row = int(input("Enter the number of rows:"))
matrix = [] 
for i in range(row):
    row = list(map(int,input().split()))
    matrix.append(row)
print(matrix)
    
