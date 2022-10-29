#Loop Controls Break and Continue
"""
In some situations you want to exit a loop or skip a part of the loop, this
can be done using Loop Controls Break and Continue respectively
"""
"""Example using while loop"""
#i)Using Break
count = 0
while count <= 5:
    if count == 3:
        break
    else:
        print(count)
    count = count + 1
print("Thank you")

"""Example using for loop"""
for count in [20, 38, 22, 13, 53, 89, 21]:
    if count == 53:
        break
    else:
        print(count)
print("You are awesome")

"""Example 2"""
for letter in "amuls":
    if letter == 'u':
        break
    else:
        print(letter)
print("Thank you")

#ii)Using Continue
"""Example 1 in for loop"""
for letter in "amuls":
    if letter == 'u':
        continue
    else:
        print(letter)
print("Thank you")

"""Example 2 in for loop"""
for count in [20, 38, 22, 13, 53, 89, 21]:
    if count == 53:
        continue
    else:
        print(count)
print("You are awesome")
"""Note: Terminating a loop means end of the loop"""

"""Example 3 in While Loop with increament"""

num = -1
while num < 10:
    num = num + 1
    if num == 5:
        continue
    else:
        print(num)
    
print("Thank you")

"""Example 4 in While Loop with decreament"""
num1 = 11
while num1 > 1:
    
    num1 = num1 - 1
    if num1 == 5:
        continue
    else:
        print(num1)
print("Thank you")
