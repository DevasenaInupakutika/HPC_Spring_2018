# Python program to remove the characters which have odd index values from a non-empty string

# Example string
str1 = 'Test Program'

# Function to remove character from odd indices
def char_nodd_remove(str):  
    str_res = ""   
    for i in range(len(str)):  
        if i % 2 == 0:  
            str_res =  str_res + str[i]  
    return str_res

# Testing the above defined function
print("Resultant string is: ", char_nodd_remove(str1))


