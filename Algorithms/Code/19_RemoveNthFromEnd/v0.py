"""
Problem:19 Remove Nth Node from end of list 
Level: Medium 
Tags: 
Technique: 
Status: Accepted

Problem Description:  
Given a linked list, remove the nth node from the end of list and return its head.
For example,
   Given linked list: 1->2->3->4->5, and n = 2.
   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass. 

Lesson:
Need to be creative to get around O(1) constraint
Additional explicit looping is easier then clever looping
"""

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        Assume n is valid
        Time O(n) for a single traversal
        Space O(1)
        """
        # trival cases
        if head == None:
            return None
        if (head.next == None) and (n == 1):
            return None
        # initialize a pre and post pointer
        head0  = ListNode(None)
        head0.next = head
        pre = head0
        post= head0
        count = 0
        for i in range(0,n):
            post = post.next
            count = count + 1
        while post.next != None:
            pre = pre.next
            post = post.next
        pre.next = pre.next.next
        return head0.next

    def removeNthFromEnd_hash(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        Assume n is valid
        Method: use hash table and object mutability
        Space O(n) for the hash table
        Time O(n) for traversal
        """
        # trival cases
        if head == None:
            return None
        if (head.next == None) and (n == 0):
            return None
        # add 0 index
        head0 = ListNode(None)
        head0.next =  head
        # put elements into hash table 
        N = 0 
        nodes = {0:head0}
        while head != None:
            N = N + 1
            nodes[N] = head
            head = head.next
        # rearrange elements
        pre = nodes[N-n]
        if n == 1:
            post = None
        else:
            post = nodes[N-n+2]
        pre.next = post
        # return
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
    method = 'removeNthFromEnd'
    prehead = ListNode(None)
    head = prehead
    vals = [2,3,4,1,0,100,2]
    N = 3
    for v in vals: 
        head.next = ListNode(v) 
        head = head.next
    head = prehead.next
    expected_answer = vals[:]
    expected_answer.pop(-N)
    output = sol.removeNthFromEnd(head,N)
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
    
