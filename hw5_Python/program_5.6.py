# Python program to create set difference

# Example set
set1 = set(['HPC','IoT Security','Communication','Mathematics','DSP','Mathematics'])
set2 = set([100, 30, 80, 40, 60, 'IoT Security','Communication'])

# Function for set difference between 2 sets in Python
def diff_set(set1,set2):
    return set1.difference(set2)

#Testing if the difference function works
print("Difference between 1 and 2: ",diff_set(set1,set2))
print("Difference between 2 and 1: ",diff_set(set2,set1))

