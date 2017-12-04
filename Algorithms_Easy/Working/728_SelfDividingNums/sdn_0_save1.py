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

import math


#
# Define SubFunctions
#
def isSelfDividing(num, debug = False):
    """
    :type n: integer
    :return Boolean
    """

    n = num
    if n < 0:
        n = -n
    d = math.log10(n)
    d = math.ceil(d)
    digits = d
    del d,n
    if debug:
        print('DEBUG isSelfDividing: '
                '{} has {} digits'.format(num,digits))


    #### pull digits from 
    ISD = True
    n = num
    if n < 0:
        n = -n
    for d in range(1,digits+1):
        r = n%(10**d)
        r = math.floor(r/(10**(d-1)))
        if r == 0:
            return False
        s = n%r
        if s != 0:
            ISD = False
        if debug:
            print('DEBUG isSelfDividing: '
                    'digit {} of {} is {} remainder {}'.format(d,n,r,s))

    return ISD




   

#
# Test Code
#
if __name__ == "__main__":
    a = isSelfDividing(203,debug = True)
    print(a)
