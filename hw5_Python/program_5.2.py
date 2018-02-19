# Python program to add an item in a tuple

# Example tuple
tuple1 = ([1,2,3,4,5],'Hello','World',[6,7,8,9,10],100,'Programming','HPC',['a','b','c'],'Testing',500)

# Function to add an item in the tuple
def add_item(tuple1, item1):
    list_tup = list(tuple1)
    list_tup.append(item1)
    tuple1 = tuple(list_tup)
    return tuple1

#Testing if adding item function works
print("Adding item1 to tuple: ",add_item(tuple1,'Added New Item'))

print("Adding item2 to tuple: ",add_item(tuple1,[56,67,78,89,9]))



