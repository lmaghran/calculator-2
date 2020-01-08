"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
running = True
# repeat forever:
while running:
#     read input
    user_input= input("Please enter an operator and some numbers >  ")
#     tokenize input
    token= user_input.split(" ")
    first_token= token[0]
#    print (first_token)
#     if the first token is "q":
#         quit
    if first_token == "q":
        running = False
#   else:
    else:
        if first_token == "+":
            print(add(float(token[1]), float(token[2])))

        elif first_token == "-":
            print(subtract(float(token[1]), float(token[2])))

        elif first_token == "*":
            print(multiply(float(token[1]), float(token[2])))

        elif first_token == "/":
            print(divide(float(token[1]), float(token[2])))
        
        elif first_token == "square":
            print(square(float(token[1]), float(token[2])))
        
        elif first_token == "cube":
            print(cube(float(token[1]), float(token[2])))
        
        elif first_token == "pow":
            print(power(float(token[1]), float(token[2])))

        elif first_token == "mod":
            print(mod(float(token[1]), float(token[2])))

        elif first_token == "x+":
            print(add_mult(float(token[1]), float(token[2])))

        elif first_token == "cubes+":
            print(add_cubes(float(token[1]), float(token[2])))