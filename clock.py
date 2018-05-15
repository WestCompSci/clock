"""
  __
|__|
|__|

"""

num_ref = { # This is a reference dictionary where numbers, like 8, are connected with their assosiated register codes
    1: [0, 0, 0, 1, 0, 0, 1],
    2: [1, 0, 1, 1, 1, 1, 0],
    3: [1, 0, 1, 1, 0, 1, 1],
    4: [0, 1, 1, 1, 0, 0, 1],
    5: [1, 1, 1, 0, 0, 1, 1],
    6: [0, 1, 1, 0, 1, 1, 1],
    7: [1, 0, 0, 1, 0, 0, 1],
    8: [1, 1, 1, 1, 1, 1, 1],
    9: [1, 1, 1, 1, 0, 0, 1],
    0: [1, 1, 0, 1, 1, 1, 1]
}

def display(num):
    register = [num_ref[num1], num_ref[num2]]
    if register[0] == 1:
        print(" __")
    else:
        print("   ")

    if register[1] == 1:
        print("|", end="")  # This ensures that the below will not be on a new line
    else:
        print(" ", end="")

    if register[2] == 1:
        print("__", end="")
    else:
        print("  ", end="")

    if register[3] == 1:
        print("|")
    else:
        print(" ")

    if register[4] == 1:
        print("|", end="")
    else:
        print(" ", end="")

    if register[5] == 1:
        print("__", end="")
    else:
        print("  ", end="")

    if register[6] == 1:
        print("|")
    else:
        print(" ")


def display_time(time):
    digits = [0, 0, 0, 0]
    register = []
    time = str(time)
    for num in range(0, len(time)):
        digits[(num + 1) * -1] = time[num]
    for dig in digits:
        register.append(num_ref[int(dig)])
    print(digits, register)
    for x in register: # For the first line
        if x[0] == 1:
            print(" __", end="")
        else:
            print("   ", end="")
        print("      ", end="")
    print ("\n", end="")
    for x in register: # For the second line
        if x[1] == 1:
            print("|", end="")
        else:
            print(" ", end="")
        if x[2] == 1:
            print("__", end="")
        else:
            print("  ", end="")
        if x[3] == 1:
            print("|", end="")
        else:
            print(" ")
        print("     ", end="")
    print("\n", end="")
    for x in register: # For the fourth line
        if x[4] == 1:
            print("|", end="")
        else:
            print(" ", end="")
        if x[5] == 1:
            print("__", end="")
        else:
            print("  ", end="")
        if x[6] == 1:
            print("|", end="")
        else:
            print(" ")
        print("     ", end="")

user_in = int(input("Enter a number"))
# display(user_in)
display_time(130)
