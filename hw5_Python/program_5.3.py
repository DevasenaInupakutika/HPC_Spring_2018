# Python program to remove an item in a tuple

# Example tuple
tuple1 = ([1,2,3,4,5],'Hello','World',[6,7,8,9,10],100,'Programming','HPC',['a','b','c'],'Testing',500)

# Function to remove an item in the tuple
def remove_item(tuple1, item1):
    list_tup = list(tuple1)
    list_tup.remove(item1)
    tuple1 = tuple(list_tup)
    return tuple1

#Testing if adding item function works
print("Removing item1 from tuple: ",remove_item(tuple1,100))

print("Removing item2 from tuple: ",remove_item(tuple1,'Testing'))



