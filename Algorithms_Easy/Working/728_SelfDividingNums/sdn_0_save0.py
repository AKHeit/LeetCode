#
# Lengthy Docstring about Python Rules
#
"""
PYTHON HELP
- help(object/class) will get the description and docstring u
- q exits the help menu
- ctrl + l clears the terminal
- type(object) will report back a class
- print(object) will specify object and it's hex address
- help(object/class) will show documentation of said class
"""







#
# Define SubFunctions
#
def isSelfDividing(num, debug = False):
    """
    :type n: integer
    :return Boolean
    """

    #### no zeros
    if num%10 == 0:
        return False
    #### identify power
    n = num
    p = 0
    x = 0
    while x == 0:
        d = 10**p
        r = n/d
        if r > 10 or r < -10:
            p = p + 1
        else:
            x = 1
    power = p
    del x,r,d,p
    if debug:
        print("DEBUG isSelfDividing: power of {} is {}".format(num,power))
    return False



   

#
# Test Code
#
if __name__ == "__main__":
    a = isSelfDividing(-11,debug = True)
    print(a)
