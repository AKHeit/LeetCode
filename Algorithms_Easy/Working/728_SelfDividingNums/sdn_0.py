#
# Lengthy Docstring about Python Rules
#
"""
PYTHON HELP
- sudo apt-get install pylint
- help(object/class) will get the description and docstring u
- q exits the help menu
- ctrl + l clears the terminal
- type(object) will report back a class
- print(object) will specify object and it's hex address
- help(object/class) will show documentation of said class
- pylint xxx.py to run guido style check
"""

import math


#
# Define SubFunctions
#
def isSelfDividing(num, debug=False):
    """
    :type n: integer
    :return Boolean
    """

    # Find number of digits
    n = num
    if n < 0:
        n = -n
    d = math.log10(n)
    d = math.ceil(d)
    digits = d
    del d, n
    if debug:
        print('DEBUG isSelfDividing: '
              '{} has {} digits'.format(num, digits))


    # Pull out digit counts
    answer = True
    n = num
    if n < 0:
        n = -n
    for d in range(1, digits+1):
        r = n%(10**d)
        r = math.floor(r/(10**(d-1)))
        #false for a 0 digit
        if r == 0:
            return False
        s = n%r
        if s != 0:
            answer = False
        if debug:
            print('DEBUG isSelfDividing: '
                  'digit {} of {} is {} remainder {}'.format(d, n, r, s))
    return answer

#
# Test Code
#
if __name__ == "__main__":
    testvals = range(1,23)
    answers = []
    for i_val in testvals:
        ISD = isSelfDividing(i_val, debug=False)
        if ISD:
            answers.append(i_val)
    print(answers)
        
