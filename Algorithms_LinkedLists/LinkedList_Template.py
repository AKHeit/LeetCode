"""
Problem: 
Level:
Tags: 
Technique: 
Status: 

Problem Description:  

Lesson: 
"""
import math
class Solution(object):
    def answermethod():
        return []


#
#
#           test code with ListNode helpers
#
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
    # test 0
    method = 'merge2Lists'
    l1 = [1,3,5]
    l2 = [2,4,6]
    lists = [l1,l2]
    del l1,l2
    input = []
    for l in lists:
        head = ListNode(None)
        tail = head
        for v in l:
            tail.next = ListNode(v)
            tail = tail.next
        head = head.next    
        input.append(head)
        del head, tail
    expected_answer = [1,2,3,4,5,6]
    output = sol.merge2Lists(input[0], input[1])
    observed_answer = []
    while output != None:
        observed_answer.append(output.val)
        output = output.next
    err = err + print_test(expected_answer, observed_answer,method)

    # test 1
    method = 'mergeKLists 2 Lists'
    l1 = [1,3,5]
    l2 = [2,4,6]
    lists = [l1,l2]
    del l1,l2
    input = []
    for l in lists:
        head = ListNode(None)
        tail = head
        for v in l:
            tail.next = ListNode(v)
            tail = tail.next
        head = head.next    
        input.append(head)
        del head, tail
    expected_answer = [1,2,3,4,5,6]
    output = sol.mergeKLists(input)
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
    
