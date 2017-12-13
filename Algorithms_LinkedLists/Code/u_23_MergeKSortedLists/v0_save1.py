"""
Problem: 23. Merge k Sorted Lists 
Level: Hard
Tags: 
Technique:
Status: 

Problem Description:  
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity

Lesson: 
"""
class Solution(object):
    def merge2Lists(self,l1,l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :type return: ListNode
        """
        # trivial cases
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        # loop through lists
        mh = ListNode(None) #head
        mt = mh #tail
        while (l1 != None) and (l2 != None):
            if l1.val <= l2.val:
                mt.next = l1
                l1 = l1.next
            else:
                mt.next = l2
                l2 = l2.next
            mt = mt.next
        # append remainder
        if l1 == None:
            mt.next = l2
        if l2 == None:
            mt.next = l1
        # return head
        return mh.next

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        K = len(lists)
        # trivial cases
        if K == 0:
            return None
        if K == 1:
            return lists[0]
        # make an even number
        if K % 2 == 1:
            lists[K-2] = self.merge2Lists(lists[K-2],lists[K-1])

k



        return None









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
    
