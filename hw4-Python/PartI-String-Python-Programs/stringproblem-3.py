#Python program to add suffix to a string depending on its length

# Function to add suffix to a string depending on its length
def add_suffix(str):
     
    str_res = ""   
    
    if len(str) < 3:
        str_res = str 

    elif len(str) >= 3:
        if str[-3:] == 'ing':
            str_res = str + 'ly'
        else:
            str_res = str + 'ing'

    return str_res

# Testing the above defined function
print("For Read word: ",add_suffix("Read"))

print("For Or word: ",add_suffix("Or"))
 
print("For Programming word: ",add_suffix("Programming")) 
