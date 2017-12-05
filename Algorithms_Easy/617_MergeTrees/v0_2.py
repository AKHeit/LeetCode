"""
Problem: 728_SelfDividingNums
Level: Easy
Technique: Recursive
Accepted

Problem Description:
Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.
You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree. 
Problem Description:
"""

# Definition for a binary tree node.
class TreeNode(object):
    """
    Tree Node defined by LeetCode Problem
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
    """
    hacked test code for terminal runs
    t1 = [1,3,2,5]
    t2 = [2,1,3,null,4,null,7]
    tm = [3,4,5,5,4,None,7]
    """

    tree1 = TreeNode(1)
    tree1.left = TreeNode(3) 
    tree1.right= TreeNode(2)
    tree1.left.left = TreeNode(5)
    tree2 = TreeNode(2)
    tree2.left = TreeNode(1) 
    tree2.right= TreeNode(3)
    tree2.left.right = TreeNode(4)
    tree2.right.right = TreeNode(7)

    s = Solution()
    merged = s.mergeTrees(tree1,tree2)
    answer = []
    answer.append(merged.val)
    answer.append(merged.left.val)
    answer.append(merged.right.val)
    node = merged.left.left
    if node != None:
        answer.append(node.val)
    else:
        answer.append(None)
    node = merged.left.right
    if node != None:
        answer.append(node.val)
    else:
        answer.append(None)
    node = merged.right.left
    if node != None:
        answer.append(node.val)
    else:
        answer.append(None)
    node = merged.right.right
    if node != None:
        answer.append(node.val)
    else:
        answer.append(None)
    
    expected_answer = [3,4,5,5,4,None,7]
    print('Expected Answer: {}'.format(expected_answer)) 
    print('Observed Answer: {}'.format(answer)) 

