'''                   File Handling                   '''
# with open("bnc.txt","w+")as f:
#     data = f.write("Hello bitm")
# # data = f.read(4)
#     print(data)
# f.close()


f = open("bnc.txt","a")
f.write("hello bitm i am here")
f.close()


'''Read Functions     
read()
read(n)
readlines()

Write Functions
write()
writeline()
 '''



'''Create a text file and insert the college data
we are learning file input and output using java
i like programming in java
Task 1:Replace all the occurances of java with python 
Task 2:Check whether the word learning exists in the text file or not '''

with open ("bnc.txt","w") as f:
     f.write("i like programming in java\n")
     f.write("we are learning file input and output using java")

# Task 1:Replace all the occurances of java with python 
with open ("bnc.txt","r") as f:
    data = f.read()
    new_data = data.replace("java","python")
print(new_data)

# Task 2:Check whether the word learning exists in the text file or not 
word = "learning"
with open ("bnc.txt","r") as f:
    data = f.read()
    if(word in data):
        print(f"{word} is present in the file")
    else:
        print(f"{word} is not present in the file")