import os
os.system("cls") # for å få det oppp i terminalen uten masse tillegs info.

#This is a comment.
print("Hello,World!")

if 5 > 2:
    print("Five is greater than two!")

"""
Variables and creating them:
    Phyton has no command for declaring a variable.
    A variable is created the moment you first assign a value to it.
"""

#Eksemple variables: 

x = 5
y = "John"

print(x)
print(y)

"""
    Variables do not need to be declared with any particular type, 
    and can even change type after they have been set.

    Casting: 
    If you want to specify the data type of a variable,
    this can be done with casting.
"""

a = str(3)      # a will be '3'
b = int(3)      # b will be 3
z = float(3)    # z will be 3.0

"""
    You can get the type of a variable with the type() function.
"""

print(type(x))  # Will print: <class 'int'>
print(type(y))  # Will print: <class 'str'>

""" 
Variable Names:
    A variable can have a short name (like x and y) or a more
    descriptive name (age, carnage, total_volume). Rules of Python
    variables:
        - A variable name must start with a letter or the underscore character
        - A variable name cannot start with a number.
        - A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and_ ).
        - Variable names are case-sensitive.
        - A variable name cannot be any of the Python keywords.

Multi Words Variable Names:
    Camel Case:
        myVariableName = "John"
    Pascal Case:
        MyVariableName = "John"
    Snake Case:
        my_variable-name = "John"
"""

print(x, y)

