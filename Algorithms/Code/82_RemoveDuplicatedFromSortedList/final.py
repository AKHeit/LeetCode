"""
Problem: 82 Remove Duplicates from Sorted List 2
Level: Medium
Tags: 
Technique: 3 Pointers
Status: Accepted

Problem Description:  
 Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3. 

Lesson: 
For while condition loops, make sure condition is evaluatable
"""


class Solution(object):

    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        3 pointers
        Space O(1)
        Time O(n)
        """
        # trivial
        if (head == None) or (head.next == None):
            return head
        # initialize pointers 
        head0      = ListNode(None)
        head0.next = head
        prev = head0
        curr = prev.next
        next = prev.next.next
        # loop through linked list
        while next != None:
            # update the pointer for previous
            if curr.val == next.val:
                while (next != None) and (curr.val == next.val):
                    next = next.next
                prev.next = next
            else:
                prev = prev.next
            # update curr and next if room exists
            if next == None:
                pass
            else:
                curr = prev.next
                next = prev.next.next
        return head0.next




#
#           test code for terminal runs
#
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def addNode_head(node_h, val):
        """
        adds node to head
        :type node_h: ListNode (original head)
        :type val: ListNode (new head)
        :rtype     : ListNode
        :method calls: NONE
        """
        nn = ListNode(val)
        nn.next = node_h
        return nn

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
    method = 'simple deletion; easy backend'
    vals = [1,1,1,2,3]
    head0 = ListNode(None)
    head  = head0
    for v in vals:
        head.next = ListNode(v)
        head = head.next
    head = head0.next
    expected_answer = [2,3]
    output = sol.deleteDuplicates(head)
    observed_answer = []
    while output != None:
        observed_answer.append(output.val)
        output = output.next
    err = err + print_test(expected_answer, observed_answer,method)

    # test 2 
    method = 'delete all'
    vals = [1,1]
    head0 = ListNode(None)
    head  = head0
    for v in vals:
        head.next = ListNode(v)
        head = head.next
    head = head0.next
    expected_answer = []
    output = sol.deleteDuplicates(head)
    observed_answer = []
    while output != None:
        observed_answer.append(output.val)
        output = output.next
    err = err + print_test(expected_answer, observed_answer,method)


    # test 3 
    method = 'delete multipule runs'
    vals = [1,2,2,2,3,3,4,5,5,5,6]
    head0 = ListNode(None)
    head  = head0
    for v in vals:
        head.next = ListNode(v)
        head = head.next
    head = head0.next
    expected_answer = [1,4,6]
    output = sol.deleteDuplicates(head)
    observed_answer = []
    while output != None:
        observed_answer.append(output.val)
        output = output.next
    err = err + print_test(expected_answer, observed_answer,method)


    # Final pass/fail readout
    print('')
    if err == 0:
        print('PASSED ALL TESTS')
    else:
        print('FAILED A TEST: DEBUG!!!')
    
