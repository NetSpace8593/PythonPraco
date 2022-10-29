#CONTROL STRUCTURES
"""Control Structures tell in which order a program is going to be executed."""
#Types of Control Structure
"""
1.Sequential Control
2.Selection Control
3.Iterative Control
"""

#Sequential Control
print("hello")
print("Welcome")
print("home is good")
print("welcome to my academy")
#Selection Control
"""This is based on a condition, if true the program runs if false it runs
the other print"""
var = int(input("enter an integer value"))

if var < 10:
    print("Value is less than 10")

else:
    print("Value is greater than 10")
#Iterative Control
var = 0
while var < 10:
    print(var)
    var = var + 1

#Selection Control Statement
#i)if-else Statements
"""Below if condition is true it will perform the action in the if block and
if the condition is false, it will perform the action on the else block

if condition:
    action 
else:

    action
    
"""

"""Example of program to check whether the student got passing marks or not"""
marks = int(input("Enter your marks in maths:"))
if marks >= 35:
    print("You got passing grades")
else:
    print("Sorry you got failing grades")

#ii)MultiWay Statement
#-Nested-if
"""A nested if is an if statement that is the target of another if statement
or an if statement inside another if statement"""

"""All the conditions in an Nested-if need to be true, otherwise it will not
run.
Nested if is used when a user or something needs more than one condition to be
fulfilled. For example, for one to be admitted to a school, they need to have
a number of conditions to be met."""
name = "Nickson"
college = "Strathmore"
marks = 56
if college == "Strathmore":
    if name == "Nickson":
        print("Nickson of Strathmore University got: ", marks, "marks")

#- elif or else if
"""Provides multiple options"""
"""elif helps us to check for multiple conditions"""
"""Example of a longer method of elif"""
x = 20
y = 45
z = 23
if x > y and x > z:
    print("x is greater")
else:
    if z > y:
        print("z is greater")
    else:
        print("y is greater")

"""Simpler method of elif"""
if x > y and x > z:
    print("x is greater")

elif z > y:
    print("z is greater")

else:
    print("y is greater")

#Iterative Control
#i)For Loop
"""
Iterative control statements repeatedly execute instructions
Examples are: for statement and while statement
"""
"""Syntax
for variable in sequence
    action
"""
"""Example"""
for letter in "Python":
    print("Character is", letter)

for letter2 in [29, 38, 53, 53]:
    print(letter2)

for letter3 in [23, 53, 83, 21, 13, 53, 11]:
    if letter3 >= 25:
        print(letter3, "greater than 25")
    else:
        print(letter3, "less than 25")
#ii)While Loop
"""
Syntax:
while condition:
    statement
"""
"""Example"""
count = 1
while count <= 5:
    print(count)
    count = count + 1
print("Good bye")

"""
Above is a definite loop because we have included an increament statement
which will guide the program to run to the set limit, however an indefinite
loop does not have an increment stement therefore it will run forever.
Example of indefinite loop
count = 1
while count <= 5:
    print(count)
"""

