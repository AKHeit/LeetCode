"""
Problem: 561 Array Partion 1 
Level: Very Easy
Technique: Brute Force
Accepted

Problem Description:
Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.
Input: [1,4,3,2]
Output: 4
Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4)
Note:
n is a positive integer, which is in the range of [1, 10000].
All the integers in the array will be in the range of [-10000, 10000].
"""

class Solution(object):
    """
    Solution format for LeetCode
    """

    def arrayPairSum(self, nums):
        """
        :type nums: List[int] (even length)
        :rtype: int
        """
        nums.sort()
        a = [None] * int((len(nums)/2))
        b = [None] * int((len(nums)/2))
        for i_ind in range(len(a)):
            a[i_ind] = nums.pop()
            b[i_ind] = nums.pop()
        answer = sum(b)
        return answer


if __name__== "__main__":
    """
    hacked test code for terminal runs
    """
    input = [1,4,3,2]
    expected_answer = 4
    s = Solution()
    observed_answer = s.arrayPairSum(input)
    print('Expected Answer: {}'.format(expected_answer)) 
    print('Observed Answer: {}'.format(observed_answer))
    


