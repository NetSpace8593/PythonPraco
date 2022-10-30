#SEQUENCES
"""
-Sequences allow you to store multiple values in an organized and efficient
fashion.
There are 7 sequence types:
strings, bytes, lists, tuples, bytearrays, buffers and range objects.

There are 10 sequence operations in python, they are:
Length, Slice, Index, Concatenation, Max Value, Select, Count, Membership,
Min Value, Sum
"""
#Sequence Operations
#1. Length operation
name = "amuls"
list1 = [10, 20, 3.4, 5, 6, 5, 5, 5, 3]
tuple1 = (10, 2, 3, 4.5, 5, 3, 3, 2, 5)

#Finding the length of above sequences
print("Lengths of the sequences")
print(len(name))
print(len(list1))
print(len(tuple1))

#2.Select operation
#Selecting an individaul element from a sequence
print("Selecting individual elements form the sequences")
print(name[0])
print(list1[4])
print(tuple1[3])

#3.Slice operation
#If you want only part of the sequence
print("Slicing the Sequences above to get part of the sequence")
print(name[1:4])#It reads, index 1 element included and index 4 element excluded
print(list1[1:])
print(tuple1[:2])#If you leave first part of the range blanc, python assumes it
#to be the first element.

#4. Count Operation
#If you want to know how many times an element is present in a sequence
print("Checking how many times a character is present in a sequence")
print(name.count('m'))
print(list1.count(5))
print(tuple1.count(3))

#5. Index Operation
#Specifies the position index for a character
print("Checks index of a character in a sequence")
print(name.index('l'))
print(list1.index(5))
print(tuple1.index(4.5))
