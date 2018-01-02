"""
Problem: 143 Reorder List
Level: Medium
Tags:  Linked List
Technique: 
Status:  Accepted

Problem Description:   
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
You must do this in-place without altering the nodes' values.
For example: Given {1,2,3,4}, reorder it to {1,4,2,3}

Lesson: 
"""


###########################################
#
#    LeetCode solution class
#
###########################################
import math
class Solution(object):
    def reorderlist(self, linkedlist):
        """
        Split, Reverse, Merge
        Time  (O(n))
        Space (O(1))
        """

        # trivial returns
        if not linkedlist:
            return linkedlist
        if not linkedlist.next:
            return linkedlist

        # Split list
        head = ListNode('dummy')
        head.next = linkedlist
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        middle = slow.next
        slow.next = None
            
        return 


    def reorderlist_bf(self, linkedlist):
        """
        brute force store pointers in a list
        Time  (O(n))
        Space (O(n))
        """

        # make a list of pointers
        pointers = []
        tail = linkedlist
        while tail != None:
            pointers.append(tail)
            tail = tail.next

        # reassign pointers
        steps = math.floor(len(pointers)/2)
        head = ListNode(None)
        tail = head
        left = 0
        right= len(pointers)-1
        for i_step in range(steps):
            tail.next = pointers[left]
            tail = tail.next
            tail.next = pointers[right]
            tail = tail.next
            left = left + 1
            right = right -1 
        if left == right:
            tail.next = pointers[left]
            tail = tail.next

        tail.next = None
        return head.next





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
    err = 0
    sol = Solution()

    # test 0 linked list helpers
    name = 'test helpers: list to linkedlist converters'
    input = [1,2,3,4]
    expected = input
    observed = linkedlist_tolist(list_tolinkedlist(input))
    err = err + print_test(expected, observed, name)

    # test 1 simple even count
    name = 'reorderlist: length of four'
    input = [1,2,3,4]
    expected = [1,4,2,3]
    output = sol.reorderlist(list_tolinkedlist(input))
    observed = linkedlist_tolist(output)
    err = err + print_test(expected, observed, name)

    # test 2 edge case length 0
    name = 'reorderlist: edge case length 0'
    input = []
    expected = []
    output = sol.reorderlist(list_tolinkedlist(input))
    observed = linkedlist_tolist(output)
    err = err + print_test(expected, observed, name)

    # test 3  edge case length 1
    name = 'reorderlist: edge case length 1'
    input = [1]
    expected = [1]
    output = sol.reorderlist(list_tolinkedlist(input))
    observed = linkedlist_tolist(output)
    err = err + print_test(expected, observed, name)

    print(output)
    print(input)
    print(output.val)


    # Final pass/fail readout
    print('')
    if err == 0:
        print('PASSED ALL TESTS')
    else:
        print('FAILED A TEST: DEBUG!!!')
    
