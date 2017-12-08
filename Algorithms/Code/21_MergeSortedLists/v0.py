"""
Problem: 21 Merge Two Sorted Lists
Level: easy
Tags: linked lists, merge, pointers
Technique: brute force, iterative, recursive
Status: Accepted

Problem Description:
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Lesson:
- unchanging dummy node to start
- drop off dummy for final answer
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """
    Solution format for LeetCode
    """
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        Build list out iteratively
        Time O(n)
        Space O(1): for recursive calling
        """
        # trivial cases
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        # preset a dummy head
        head_dummy = ListNode(None)
        prev = head_dummy
        # loop through lists 
        while (l1 != None) and (l2 != None):
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
                prev = prev.next
            else:
                prev.next = l2
                l2 = l2.next
                prev = prev.next
        # append none empty list
        if l1 == None:
            prev.next = l2
        else:
            prev.next = l1
        # lop off dummy head and return
        head = head_dummy.next
        return head


    def mergeTwoLists_recur(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        Recursive changing links from the maximal element
        Time O(n)
        Space O(n): for recursive calling
        """
        # recursive null (and trivial cases)
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        # recursive calling
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

    def mergeTwoLists_bf(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        Brute force construction of new list
        Space O(n) for the new list
        Time O(n) for looping through the list
        """
        # trivial merges
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        # set head
        if l1.val <= l2.val:
            head  = ListNode(l1.val)
            l1 = l1.next
        else:
            head  = ListNode(l2.val)
            l2 = l2.next
        tail = head
        # grow tail
        while (l1 != None) and (l2 != None):
            if l1.val <= l2.val:
                tail.next = ListNode(l1.val)
                tail = tail.next
                l1 = l1.next
            else:
                tail.next = ListNode(l2.val)
                tail = tail.next
                l2 = l2.next
        # finish merge
        if l1 == None:
            tail.next = l2
        else:
            tail.next = l1
        # return
        return head


    

if __name__== "__main__":
    """
    test code 
    """ 

    def print_test(ans_e,ans_o,name):
        """
        prints tests in standardized format
        :type ans_e: expected answer in printable format
        :type ans_o: observed answer in printable format
        """
        print('~'*40)
        if ans_o != ans_e:
            error = 1
            print("########## FAIL ##########")
            print("TEST: {} :: Status: FAIL".format(name))
        else:
            error = 0
            print("TEST: {} :: Status: PASS".format(name))
        print('TEST: {} :: Expected: {}'.format(method, ans_e))
        print('TEST: {} :: Observed: {}'.format(method, ans_o))
        return error


    err  = 0
    sol  = Solution()
    # test 1
    method = "mergeTwoLists"
    head1           = ListNode(1)
    head1.next      = ListNode(2)
    head1.next.next = ListNode(4)
    head2           = ListNode(1)
    head2.next      = ListNode(3)
    head2.next.next = ListNode(4)
    expected_answer = [1,1,2,3,4,4]
    merged = sol.mergeTwoLists(head1,head2)
    observed_answer = []
    observed_answer.append(merged.val)
    while merged.next != None:
        merged = merged.next
        observed_answer.append(merged.val)
    err = err + print_test(expected_answer, observed_answer,method)

    #
    # Final pass/fail readout
    #
    print('')
    if err == 0:
        print('PASSED ALL TESTS')
    else:
        print('FAILED A TEST: DEBUG!!!')



