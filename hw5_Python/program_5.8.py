# Python program to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys.

# Declaring an empty dictionary
dict1 = {}

# Function for printing dictionary
def print_dict(dict1):
    for i in range(1,16):
        key = i
        dict1[i] = i*i
    return dict1

#Testing if printing function works
print("Dictionary is: ",print_dict(dict1))
