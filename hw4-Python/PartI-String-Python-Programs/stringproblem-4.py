#Python program to string modification

def modify_string(str):
     
    str_res = ""   
    
    if len(str) < 2:
        str_res = " " 

    else:
        str_res = str[:2] + str[-2:]

    return str_res

# Testing the above defined function
print("For w3resource word: ",modify_string("w3resource"))

print("For w3 word: ",modify_string("w3"))
 
print("For w word: ",modify_string("w")) 
