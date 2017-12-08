"""
Problem: 206 reverse linked list
Level: easy 
Tags: linked list
Technique: iterative, recursion
Status: Accepted

Problem Description:
reverse a linked list

Takeaways:
can save space by modifying list rather than build new list
modify list both iteratively and recursively

To do:
fixed the broken recursive calling 
"""

#Definition for singly-linked list.
class ListNode:
    """
    Comment out while running in LeetCode
    Keep while running locally
    """
    def __init__(self, x):
        self.val  = x
        self.next = None

class Solution(object):
    """
    Solution format for LeetCode
    """
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        :method calls:
        Time O(n)
        Space O(1)
        """
        # trivial cases
        if head == None:
            return head
        if head.next == None:
            return head

        # set tail
        prev = head
        curr = head.next
        prev.next = None
        # loop through
        while curr.next != None:
            next      = curr.next
            curr.next = prev
            prev      = curr
            curr      = next
        # create head
        curr.next = prev

        return curr

        

    def reverseList_recur(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        :method calls: reverseList
        Recursion on self - editing the .next values
        Time O(n)
        Space O(n) depth of recursion
        """
        # garbage input
        if head == None:
            return 

        if head.next == None:
            head_r = head
            return head_r
        else: 
            head_r = self.reverseList(head.next)
            head.next.next = head
            head.next      = None
            return head_r

    def reverseList_bf(self, head):
        """
        Brute force creation of new list
        :type head: ListNode
        :rtype: ListNode
        :method calls: addNode_head 
        Time O(n)
        Space O(n) for newly created list
        """
        if head == None:
            return head
        ans  = ListNode(head.val)
        tail = (head.next == None)
        while not tail:
            head = head.next
            ans  = self.addNode_head(ans, head.val) 
            tail = (head.next == None)
        return ans


    def addNode_head(self, node_h, val):
        """
        adds node to head
        :type node_h: ListNode (original head)
        :type val: ListNode (new head)
        :rtype     : ListNode
        :method calls: NONE
        """
        nn = ListNode(node_h.val)
        nn.next = node_h.next
        node_h.val  = val
        node_h.next = nn 
        return node_h


if __name__== "__main__":
    """
    test code 
    """ 

    #
    # standardized printing of test results
    #
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

    #
    # testing starts here 
    #
    err  = 0
    sol  = Solution()

    # test addNode_head  checking values fields
    method = "addNode_head: checkvals"
    inp_0  = ListNode(1)
    inp_0.next = ListNode(-30)
    inp_1  = 300
    out    = sol.addNode_head(inp_0,300)
    expected_answer = [300,1,-30] 
    observed_answer = [None,None,None]
    observed_answer[0] = out.val
    observed_answer[1] = out.next.val
    observed_answer[2] = out.next.next.val
    err = err + print_test(expected_answer, observed_answer,method)
    
    # test addNode_head  checking next field
    method = "addNode_head: isnext none"
    expected_answer = [False, False, True]
    observed_answer = [None, None, None]
    observed_answer[0] = out.next
    observed_answer[1] = out.next.next
    observed_answer[2] = out.next.next.next
    for i in range(len(observed_answer)):
        observed_answer[i] = (observed_answer[i] == None)
    err = err + print_test(expected_answer, observed_answer,method)


    # test full reversal
    method  = "reverseList"
    head = ListNode(4)
    head = sol.addNode_head(head, 3)
    head = sol.addNode_head(head, 2)
    head = sol.addNode_head(head, 1)
    expected_answer = [4,3,2,1]
    observed_answer = [None] * len(expected_answer)
    head_r = sol.reverseList(head)
    observed_answer[0] = head_r.val
    observed_answer[1] = head_r.next.val
    observed_answer[2] = head_r.next.next.val
    observed_answer[3] = head_r.next.next.next.val
    err = err + print_test(expected_answer, observed_answer,method)


    

    #
    # Final pass/fail readout
    #
    print('')
    if err == 0:
        print('PASSED ALL TESTS')
    else:
        print('FAILED A TEST: DEBUG!!!')



