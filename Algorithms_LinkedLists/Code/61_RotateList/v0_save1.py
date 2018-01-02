"""
Problem: 61 Rotate List
Level: Medium
Tags:  Linked List
Technique: 
Status: 

Problem Description:   
Given a list, rotate the list to the right by k places, where k is non-negative.

Example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.

Lesson: 
"""


###########################################
#
#    LeetCode solution class
#
###########################################
class Solution(object):
    def rotateRight(self, head, k):
        """
        description
        Time  O()
        Space O()
        """

        # return the trivial cases
        if head is None:
            return head
        if head.next is None:
            return head
        if k == 0:
            return head






###########################################
#
#    linked list helpers for local testing
#
###########################################
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

def list_tolinkedlist(list):
    """
    converts lists to linked lists
    use to make easy test code
    """
    head = ListNode(None)
    tail = head
    for v in list:
        tail.next = ListNode(v)
        tail = tail.next
    return head.next

def linkedlist_tolist(linkedlist):
    """
    converts linkedlists to lists

    """
    list = []
    tail = linkedlist
    while tail != None:
        list.append(tail.val)
        tail = tail.next
    return list

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
    print('TEST: {} :: Expected: {}'.format(name, ans_e))
    print('TEST: {} :: Observed: {}'.format(name, ans_o))
    return error



###########################################
#
#   code for local testing
#
###########################################
if __name__== "__main__":
    """
    test code 
    """ 
    err  = 0
    sol = Solution()

    # test linked list helpers
    name = 'test helpers: list to linkedlist converters'
    input = [1,2,3,4]
    output = linkedlist_tolist(list_tolinkedlist(input))
    err = err + print_test(input, output, name)

    # test 
    name = 'edge case: []'
    input = []
    input_a = list_tolinkedlist(input)
    input_b = 4
    expected = []
    output = sol.rotateRight(input_a,input_b)
    observed = linkedlist_tolist(output)
    err = err + print_test(expected, observed, name)

    # test 
    name = 'edge case: list length 1'
    input = [1]
    input_a = list_tolinkedlist(input)
    input_b = 4
    expected = [1]
    output = sol.rotateRight(input_a,input_b)
    observed = linkedlist_tolist(output)
    err = err + print_test(expected, observed, name)

    # test 
    name = 'edge case: rotate 0'
    input = [1,2,3,4]
    input_a = list_tolinkedlist(input)
    input_b = 0
    expected = [1,2,3,4]
    output = sol.rotateRight(input_a,input_b)
    observed = linkedlist_tolist(output)
    err = err + print_test(expected, observed, name)

    # Final pass/fail readout
    print('')
    if err == 0:
        print('PASSED ALL TESTS')
    else:
        print('FAILED A TEST: DEBUG!!!')
    
