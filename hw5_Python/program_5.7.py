# Python program to add a key to the dictionary

# Example dictionary
dict1 = {0:10,1:20}

# Function for adding a key to dictionary
def add_key(dict1,new_key, new_value):
    dict1[new_key] = new_value 
    return dict1

#Testing if the adding key function works
print("Adding '2' key: ",add_key(dict1,2,30))
print("Adding '3' key: ",add_key(dict1,3,40))

print("Adding 'New' key: ",add_key(dict1,'New','NewValue'))
