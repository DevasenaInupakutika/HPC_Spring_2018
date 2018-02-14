# Python program to remove the nth index character from a nonempty string 

# Example string
str1 = 'Test Program'

# Function to remove character from nth index  
def char_n_remove(n, str):
    
    slice_1 = str[:n]
    slice_2 = str[n+1:]
    
    return slice_1+slice_2

# Testing the above defined function
print(char_n_remove(3,str1))
print(char_n_remove(5,str1))
