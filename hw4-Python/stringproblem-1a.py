# Python program to calculate the length of string 

# Example string
str1 = 'Checking Program'

# 2 ways 

# 1. Using in-built function
length1 = len(str1)
print("Length of string using in-built function: ",length1)

# 2. Without using a built-in function
length2 = 0

for i in str1:
    length2+=1

print("Length without built-in function: ",length2)
