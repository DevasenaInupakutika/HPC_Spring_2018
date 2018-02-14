# Python Program to insert a given string (str1) at the beginning of all the items in a given list (list1)

#Example list and string and Resultant list

list1 = [1,2,3,4]
str1 = 'emp'

final_list = []

for i in list1:
   i = str1 + str(i)
   final_list.append(i)

print("Resultant list is: ",final_list)
