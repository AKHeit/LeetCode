"""
Problem: 143 Reorder List
Level: Medium
Tags:  Linked List
Technique: 
Status: 

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
class Solution(object):
    def solutionmethod():
        """
        description
        Time  O()
        Space O()
        """
        return []






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

    # test 0 linked list helpers
    name = 'test helpers: list to linkedlist converters'
    input = [1,2,3,4]
    output = linkedlist_tolist(list_tolinkedlist(input))
    err = err + print_test(input, output, name)



    # Final pass/fail readout
    print('')
    if err == 0:
        print('PASSED ALL TESTS')
    else:
        print('FAILED A TEST: DEBUG!!!')
    
