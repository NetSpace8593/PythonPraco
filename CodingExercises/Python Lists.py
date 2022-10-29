#LISTS
#Group of differet types of elements
"""
Characteristics of lists
1. They are mutable - We can change or alter the list
2. Linear Data Structure - Elements are arranged in a linear order
3. Contains mixed types of Elements - Int, Char, Strings can be stored in one
list
4. It is of Variable length -
5. It is zero based indexing - Each value is given an index reference which
starts from zero.

Lists can also contain strings and complex numbers.
"""
#How to create a list
animals = [] #This is an empty list

animals = ['dogs', 'cats', 'monkey']
print(animals[0])

list = [10, 20.4, 'hello', 54] #List with different variables
print(list)

#Nested list ie List inside a list
list2 = [[10, 20], [30, 40]]
print(list2)
print(list2[0][0]) #printing a single value from the nested list
print(list2[1][0])

#A programming example for list
for num in [10, 20, 30, 40]:
    print(num)


#LIST OPERATION
"""
1. Replace - Replaces existing value in a list with a new value
2. Insert - Inserts a new value in a list
3. Sort - Used to sort values of similar type eg when it contains int only
or string only or char only. It will result to an error when it contains
more that one type of values.
4. Delete - If you want to remove some elememts/values from the list
5. Append - This is used when you want to enter a value at the end of the list
6. Reverse - It is used to reverse the original order of a list.
"""
#1.Replace Operation
list3 = [10, 20, 30, 40, 4.6]
list3[2] = 3.7
print(list3)

#2.Insert Operation
"""Syntax for insert operation
name_of_list.insert(index_for_new_value, new_value)
"""
list3.insert(2, "hello")
print(list3)

#3. Sort Operation
animals2 = ['monkey', 'dog', 'cat', 'lion']
animals2.sort()
print(animals2) #The sort operation arranges this list in alphabetical order
#For the case of int, it sorts the values in ascending order, for example
num1 = [23, 53, 89, 822, 23, 19, 9, 3, 5, 589, 329]
num1.sort()
print(num1)

#4. Delete
"""
Syntax: del list[index_to_be_deleted]
"""
del num1[2] #Deleting only one element
print("Num after deleting idex 2\n",num1)

num2 = [23, 53, 89, 822, 23, 19, 9, 3, 5, 589, 329]
del num2[:]#clearing the whole list
print('num 2 is', num2)
"""
Other ways of clearing or deleting values in a list are:
1. clear() method
eg num2.clear() - clears the whole list

2.Reinitialization of a list
eg num2[], will clear the whole list

3.list_name.pop(index) method
eg num2.pop(3) - deletes element specified using index

4. list.remove(index) method
eg num2.remove(3)
"""

#5. Append
animals2.append('donkey')
print(animals2)

#6. Reverse
animals2.reverse()
print(animals2)

#Example to implement all the List Operations
fruits = ['apple', 'banana']
#1. Insert
fruits.insert(2, 'orange')
print(fruits)
#2. Append
fruits.append('Mangoe')
print(fruits)
#3. Sort
fruits.sort()
print(fruits)
#4. Replace
fruits[3] = 'pineapple'
print(fruits)
#4. Delete
del fruits[3]
print(fruits)
#5. Reverse
fruits.reverse()
print(fruits)
