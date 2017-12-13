"""
Problem: 25 Reverse Nodes in k-Group
Level: Hard
Tags: 
Technique:Pointer Manipulation, 3 Pointers
Status: Accepted

Problem Description:  
 Given a linked list, reverse the nodes of a linked list k at a time and return its modified list. k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
You may not alter the values in the nodes, only nodes itself may be changed.
Only constant memory is allowed.

Must be Space O(1)

Given this linked list: 1->2->3->4->5
For k = 2, you should return: 2->1->4->3->5
For k = 3, you should return: 3->2->1->4->5 
"""
import math

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        # trivial
        if (head == None) or (head.next == None):
            return head
        if k == 1:
            return head
        
        
        # find length (O(N))
        N = 0
        point = head
        while point != None:
            N = N + 1
            point = point.next
        reversals = math.floor(N/k)
        remainder = N % k

        # trivial case
        if reversals == 0:
            return head

        # initialize the loop
        head0  = ListNode(None) # head of Global list
        tailG  = head0 # tail of corrected Global list 
        tailK  = head # tail of K group unit
        # reverse all K-Groups
        for i in range(reversals):
            # reverse the k group (standard prev,curr,next)
            prev = tailK
            curr = prev.next
            for j in range(k-1):
                next = curr.next
                curr.next = prev
                prev      = curr
                curr = next
            # assign global markers
            tailG.next = prev
            tailG      = tailK
            # reset tail for next loop
            tailK = curr
        # take care of remainder
        if remainder == 0:
            tailG.next = None
        else:
            tailG.next = curr
         
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
    # test 0
    method = 'K too large'
    vals = [1,2,3,4,5]
    K    = 6
    head0 = ListNode(None)
    head  = head0
    for v in vals:
        head.next = ListNode(v)
        head = head.next
    head = head0.next
    expected_answer = [1,2,3,4,5]
    output = sol.reverseKGroup(head, K)
    observed_answer = []
    while output != None:
        observed_answer.append(output.val)
        output = output.next
    err = err + print_test(expected_answer, observed_answer,method)

    # test 1
    method = 'reverse k = 2 perfect multiple'
    vals = [1,2,3,4]
    K    = 2
    head0 = ListNode(None)
    head  = head0
    for v in vals:
        head.next = ListNode(v)
        head = head.next
    head = head0.next
    expected_answer = [2,1,4,3]
    output = sol.reverseKGroup(head, K)
    observed_answer = []
    while output != None:
        observed_answer.append(output.val)
        output = output.next
    err = err + print_test(expected_answer, observed_answer,method)

    # test 2
    method = 'reverse k = 2 with remainder'
    vals = [1,2,3,4,5]
    K    = 2
    head0 = ListNode(None)
    head  = head0
    for v in vals:
        head.next = ListNode(v)
        head = head.next
    head = head0.next
    expected_answer = [2,1,4,3,5]
    output = sol.reverseKGroup(head, K)
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
    
