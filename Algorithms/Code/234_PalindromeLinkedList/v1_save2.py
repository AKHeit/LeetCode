"""
Problem: 234 Palindrome Linked List
Level: Easy 
Tags: 
Technique: pointer manipulation; copying and deep copying 
Status: 

Problem Description:  
Given a singly linked list, determine if it is a palindrome 
Could you do it in O(n) time and O(1) space
"""
import copy as copy
import math as math

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
        

class Solution(object):
    """
    Solution format for LeetCode
    """
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        Compare from midpoint
        Space O(1): just pointer manipulation
        Time O(n): loop through whole list ~2x
        """

        # trivial cases
        if head == None or head.next == None:
            return True
        # count length
        N = 0
        point = head
        while point != None:
            N = N + 1
            point = point.next
        del point
        # create pointer for second half
        half_2 = head
        for i in range(0, math.floor(N/2)):
            half_2 = half_2.next
        if N%2 == 1:
            half_2 = half_2.next
        # reverse first half
        prev = head
        curr = head.next
        prev.next = None
        for i in range(1,math.floor(N/2)):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        half_1r = prev
        del prev, curr
        # loop through lists to check palindrome
        for i in range(math.floor(N/2)):
            if half_1r.val != half_2.val:
                return False
            else:
                half_1r = half_1r.next
                half_2  = half_2.next
        # if no inconsistency; return true
        return True


    def isPalindrome_bf(self, head):
        """
        :type head: ListNode
        :rtype: bool
        Brute force
        Space O(n) : for manual copying of linked list
        Time O(n)  : ~3n, slow for order n
        """

        # trivial cases
        if head == None or head.next == None:
            return True

        # make a new copy o = copy.deepcopy(head)
        # effectively a deep copy
        # deep copy has a recursive limit
        o = ListNode(None)
        o.next = copy.copy(head)
        dummy  = o.next
        while dummy.next != None:
            next = copy.copy(dummy.next)
            dummy.next = next
            dummy = dummy.next
        o = o.next

        # reverse the original
        #r = self.reverseList(head)
        curr = head.next
        prev = head
        prev.next = None
        while curr != None:
            next = curr.next
            curr.next = prev
            prev      = curr
            curr      = next
        r = prev

        
        end = False
        uneq= False

        while (not end) and (not uneq):
            if o is None:
                end = True
            elif o.val != r.val:
                uneq = True
            else:
                o = o.next
                r = r.next

        if end:
            return True
        if uneq:
            return False





#
#           test code for terminal runs
#

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
    method = 'not Palindrome'
    tail = ListNode(0)
    head = tail
    for val in [2,3,4,1,0,100,2]:
        head = addNode_head(head, val)
    expected_answer = False
    observed_answer = sol.isPalindrome(head)
    err = err + print_test(expected_answer, observed_answer,method)

    # test 2
    method = 'is Palindrome'
    tail = ListNode(0)
    head = tail
    for val in [4,1,4,0]:
        head = addNode_head(head, val)
    expected_answer = True
    observed_answer = sol.isPalindrome(head)
    err = err + print_test(expected_answer, observed_answer,method)

    # test 3
    method = 'not Palindrome long'
    tail = ListNode(1)
    head = tail
    for val in [0]*100:
        head = addNode_head(head, val)
    expected_answer = False
    observed_answer = sol.isPalindrome(head)
    err = err + print_test(expected_answer, observed_answer,method)

    # test 4
    method = 'is Palindrome long'
    tail = ListNode(0)
    head = tail
    for val in [0]*500:
        head = addNode_head(head, val)
    expected_answer = True
    observed_answer = sol.isPalindrome(head)
    err = err + print_test(expected_answer, observed_answer,method)
    
    # Final pass/fail readout
    print('')
    if err == 0:
        print('PASSED ALL TESTS')
    else:
        print('FAILED A TEST: DEBUG!!!')
    
