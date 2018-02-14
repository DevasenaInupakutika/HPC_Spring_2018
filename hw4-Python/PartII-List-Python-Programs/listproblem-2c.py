# Python program to select odd items of a list (list1)

# Example list

list1 = [1, 3, 'Hello', 45, 'Bye', 78, 'Python']

# List2 is the resultant list and count
list2 = []
count = 0

for i in list1:
    if count % 2 != 0:
        list2.append(list1[count])
    count+=1

print("Odd items of the original list: ",list2)
        

