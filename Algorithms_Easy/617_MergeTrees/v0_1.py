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

# Definition for a binary tree node.
class TreeNode(object):
    """
    As defined by LeetCode Problem
    """
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    """
    Solution format for LeetCode
    """
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        if t1 == None && t2 == None:
            return
        if t2 == None:
            t = t1
        else:
            t = t1 + t2
        """""
        
        # base cases, no addition is necessary (need return values)
        if t1 is None and t2 is None:
            return None
        if t1 is None:
            return t2
        if t2 is None:
            return t1
        
        # if addition is necessary, invoke recursion
        # use left additivity
        t1.val += t2.val
        t1.left  = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1    


if __name__== "__main__":
    # test code for terminal runs
    #[1,3,2,5]
    #[2,1,3,null,4,null,7]

    tree1 = TreeNode(1)
    tree1.left = TreeNode(3) 
    tree1.right= TreeNode(2)
    tree1.left.left = TreeNode(5)

    tree2 = TreeNode(2)
    tree2.left = TreeNode(1) 
    tree2.right= TreeNode(3)
    tree2.left.right = TreeNode(5)
    







