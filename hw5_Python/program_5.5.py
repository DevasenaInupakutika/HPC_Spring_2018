# Python program to add members in a set

# Example set
set1 = set(['HPC','IoT Security','Communication','Mathematics','DSP','Mathematics'])

# Function to add element to a set in Python
def add_set(set1,item):
    #To add single or multiple items to the set
    set1.update(item)
    return set1

#Testing if adding set function works
print("New Set is: ",add_set(set1,{'Intro to CPS'}))
print("New Set is: ", add_set(set1,set(['Thermodynamics','Machine learning'])))


