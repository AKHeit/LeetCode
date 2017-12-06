"""
Problem: 728_SelfDividingNums
Level: Easy
Technique: Brute Force
Accepted

Problem Description:
A self-dividing number is a number that is divisible by every digit it contains.
For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0. Also, a self-dividing number is not allowed to contain the digit zero.
Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible. 
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

    # LeetCode example problem
    s = Solution()
    l = 1
    r = 22
    expected_answer = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
    actual_answer = s.selfDividingNumbers(l,r,debug=False)
    print(actual_answer)

