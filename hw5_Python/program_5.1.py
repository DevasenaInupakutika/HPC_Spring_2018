# Python program to create a tuple with 10 numbers and print one item

# Example tuple
tuple1 = ([1,2,3,4,5],'Hello','World',[6,7,8,9,10],100,'Programming','HPC',['a','b','c'],'Testing',500)

# Function to print nth index item from tuple
def print_tuple_item(tuple1, n):
    return tuple1[n]


print("4th Tuple item is: ",print_tuple_item(tuple1,3))

print("10th Tuple item is: ",print_tuple_item(tuple1,9))



