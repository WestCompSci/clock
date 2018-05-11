"""
 ____ 
|____|
|____|

"""

register = [] * 7
test_register = [1, 0, 1, 1, 0, 1, 1]
register = test_register

if register[0] == 1:
    print (" ____")
else:
    print ("    ")

if register[1] == 1:
    print ("|", end="")  # This ensures that the below will not be on a new line
else:
    print (" ", end="")

if register[2] == 1:
    print ("____", end="")
else:
    print ("    ", end="")

if register[3] == 1:
    print ("|")
else:
    print (" ")

if register[4] == 1:
    print ("|", end="")
else:
    print (" ", end="")

if register[5] == 1:
    print ("____", end="")
else:
    print ("    ", end="")

if register[6] == 1:
    print ("|")
else:
