# Python program to reverse a tuple

# Example tuple
tuple1 = ([1,2,3,4,5],'Hello','World',[6,7,8,9,10],100,'Programming','HPC',['a','b','c'],'Testing',500)

rev_list = []

# Function to reverse a tuple
def reverse_tuple(tuple1):
    tuple_rev = tuple1[::-1]
    return tuple_rev

#Testing if reversal works
print("Reversing tuple: ",reverse_tuple(tuple1))



