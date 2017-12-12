"""
Problem: 
Level: 
Tags: 
Technique:
Status:

Problem Description:  

Lesson:
"""


class Solution(object):





#
#           test code for terminal runs
#

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

    # Final pass/fail readout
    print('')
    if err == 0:
        print('PASSED ALL TESTS')
    else:
        print('FAILED A TEST: DEBUG!!!')
    
