"""
Problem: 
Level: 
Tags: 
Technique: 
Status: 

Problem Description:
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



