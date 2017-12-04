#
# Lengthy Docstring about Python Rules
#
"""
PYTHON HELP
- sudo apt-get install pylint
- built in functions: https://docs.python.org/3/library/functions.html
- help(object/class) will get the description and docstring u
- q exits the help menu
- ctrl + l clears the terminal
- type(object) will report back a class
- print(object) will specify object and it's hex address
- help(object/class) will show documentation of said class
- pylint xxx.py to run guido style check

BASH HELP
- printf "\033c" to clear terminal for real

VIM HELP
- 
"""

import math

class Solution(object):
    """
    Solution format for LeetCode
    """

    def selfDividingNumbers(self, left, right, debug=False):
        """
        :type left: int
        :type right: int
        :type return: List[int]
        :method calls: self.isSelfDividing
        """

        testvals = range(left, right+1)
        answers = []
        for i_val in testvals:
            ISD = self.isSelfDividing(i_val, debug)
            if ISD:
                answers.append(i_val)
        return answers
            
    def isSelfDividing(self, num, debug=False):
        """
        :type num: integer
        :type return: Boolean
        :method calls: NONE
        """
        # Find number of digits
        n = num
        if n < 0:
            n = -n
        d = math.log10(n)
        d = math.ceil(d)
        digits = int(d)
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
    """
    test code here
    """
    s = Solution()
    l = 1
    r = 22
    expected_answer = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
    actual_answer = s.selfDividingNumbers(l,r,debug=False)
    print(actual_answer)

