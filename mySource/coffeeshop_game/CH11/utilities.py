def welcome():
    print("ClydeBank Coffee Shop Simulator, Version 1.00")
    print("Copyright (C) 2022 ClydeBank Media, All Rights Reserved")
    print("Let's collect some information before we start the game.\n")

def prompt(display = "Please input a string", require = True):
    if require:
        s = False
        while not s:
            s = input(display + " ")
    else:
        s = input(display + " ")
    return s
def convert_to_float(s):
    # If conversion fails, assign 0 to it.
    try:
        f = float(s)
    except ValueError:
        f = 0
    return f

def x_of_y(x, y):
    num_list = []
    # Return a list of x copied of y
    for i in range(x):
        num_list.append(y)
    return num_list