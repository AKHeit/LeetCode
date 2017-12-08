"""
Problem: 206 reverse linked list
Level: easy 
Tags: linked list
Technique: 
Status: 

Problem Description:
reverse a linked list
"""

#Definition for singly-linked list.
class ListNode:
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
        """

    def addNode_head(self, node_h, val):
        """
        adds node to head
        :type node_h: ListNode (original head)
        :type val: ListNode (new head)
        :rtype     : ListNode
        """
        # copy old values
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

    # test addNode_head
    method = "addNode_head: checkvals"
    inp_0  = ListNode(1)
    inp_1  = 300
    out    = sol.addNode_head(inp_0,300)
    expected_answer = [300,1] 
    observed_answer = [None,None]
    observed_answer[0] = out.val
    observed_answer[1] = out.next.val
    e = print_test(expected_answer, observed_answer,method)
    err = err + e


    method = "addNode_head: isnext none"
    expected_answer = [False, True]
    observed_answer = [None,None]
    observed_answer[0] = out.next
    observed_answer[1] = out.next.next
    for i in range(len(observed_answer)):
        observed_answer[i] = (observed_answer[i] == None)
    print(observed_answer)


    # test full reversal
    """
    method  =
    head      = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    expected_answer = [4,3,2,1]

    # test 1
    input  = 
    rows    = 1
    columns = 4 
    observed_answer = sol.
    expected_answer = 
    e = print_test(expected_answer, observed_answer,method)
    err = err + e
    """

    #
    # Final pass/fail readout
    #
    print('')
    if err == 0:
        print('PASSED ALL TESTS')
    else:
        print('FAILED A TEST: DEBUG!!!')



