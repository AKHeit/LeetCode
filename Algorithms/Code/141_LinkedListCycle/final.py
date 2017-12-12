"""
Problem: 141 Linked List Cycle
Level: Easy (35%)
Tags: hash table, keys
Technique: double pointers, brute force, hash table
Status: Accepted

Problem Description:
Given a singly linked list, determine if it has a cycle in it. Try to solve in O(n).

Takeaways:
Speed element matching in list from O(n2) to O(n) by using hash table.
Instances of user defined classes are hashable
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    """
    Solution format for LeetCode
    """
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        Hash
        Space O(n) for the hash table built
        Time O(n) iterate roughly 2n times to find loop
        """
        # trivial cases
        if head == None or head.next == None:
            return False
        # initialize hash table
        nodes = {head: 1}
        loop = False
        end = False
        # build out hash table 
        while (not end) and (not loop):
            head = head.next
            if head.next == None:
                end = True
            if head in nodes:
                loop = True
            nodes[head] = 1
        # return values
        if end:
            return False
        if loop:
            return True

    def hasCycle_iter(self, head):
        """
        :type head: ListNode
        :rtype: bool
        Iterative scheme with two pointers with different speeds
        Space O(1) only a couple pointers
        Time O(n) iterate roughly 2n times to find loop
        """
        # trivial cases
        if head == None or head.next == None:
            return False
        # initialize dual speed pointers
        slow = head
        fast = head.next
        end = False
        loop = False
        # find end or loop
        while (not end) and (not loop):
            if fast == slow or fast.next == slow:
                loop = True
            elif fast == None or fast.next == None or fast.next.next == None:
                end = True
            else:
                slow = slow.next
                fast = fast.next.next
        # return values
        if end:
            return False
        if loop:
            return True






#
#
#           test code for terminal runs
#
#


def addNode_head(node_h, val):
        """
        adds node to head
        :type node_h: ListNode (original head)
        :type val: ListNode (new head)
        :rtype     : ListNode
        :method calls: NONE
        :added by AH
        """
        nn = ListNode(val)
        nn.next = node_h
        return nn

def print_test(ans_e,ans_o,name):
    """
    prints tests in standardized format
    :type ans_e: expected answer in printable format
    :type ans_o: observed answer in printable format
    :type name: string indicating method being tested
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

if __name__== "__main__":
    """
    test code 
    """ 

    err  = 0
    sol  = Solution()
    # test 1
    method = 'no cycle'
    tail = ListNode(4)
    head = tail
    for val in [2,3,4,1,0,100,2]:
        head = addNode_head(head, val)
    expected_answer = False
    observed_answer = sol.hasCycle(head)
    err = err + print_test(expected_answer, observed_answer,method)

    # test 2
    method = 'one cycle'
    tail = ListNode(4)
    head = tail
    for val in [2,3,4,1,0,100,2]:
        head = addNode_head(head, val)
    tail.next = head
    expected_answer = True
    observed_answer = sol.hasCycle(head)
    err = err + print_test(expected_answer, observed_answer,method)

    # test 3
    method = 'line then cycle'
    tail = ListNode(4)
    head = tail
    for val in [2,3,4,1,0,100,2]:
        head = addNode_head(head, val)
    tail.next = head.next.next
    expected_answer = True
    observed_answer = sol.hasCycle(head)
    err = err + print_test(expected_answer, observed_answer,method)








    method  ='edit'
    #observed_answer = sol.
    #expected_answer = 
    #err = err + print_test(expected_answer, observed_answer,method)

    # Final pass/fail readout
    print('')
    if err == 0:
        print('PASSED ALL TESTS')
    else:
        print('FAILED A TEST: DEBUG!!!')



