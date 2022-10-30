#TUPLES
"""
Tuples are quite similar to lists. This is a group of different types of elements.
Tuple is immutable. It cannot be altered in any way and this is where it differs
with lists. Lists are also created using square brackets while tuples are created
using parentheses.
"""
#Example of Tuple
animal = ("dog", "cat", "monkey")
print(animal)
"""
Tuple are zero based index.
"""
#Printing the first element of the tuple above
print(animal[0])

#Creating nested tuples
tuple1 = ((10, 2, 3), (3.5, 4))
print(tuple1)
print(tuple1[0][1])

#Creating an empty tuple
num = ()
print(num)

"""
Tuples do not have any operations such as:
*Sort
*Replace
*Delete
*Append etc

This is because it is immutable
"""
