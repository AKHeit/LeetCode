"""
Problem: 566 Reshape Matrix
Level: Easy
Tags: Basic, Math
Technique: Simple Math
Status: Accepted

Problem Description:
In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different size but keep its original data.
You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively.
The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were. If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.
"""
class Solution(object):
    """
    Solution format for LeetCode
    """
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """

        # Return original matrix for faulty dim
        e  = r * c
        r0 = len(nums)
        c0 = len(nums[0])
        e0 = r0 * c0
        if e != e0:
            return nums
        del e, r0, c0, e0

        # Reshape original matrix into vector
        array = []
        for row in nums:
            array = array + row
            
        # Sort into new elements
        m  = [[None]*c]*r
        i0 = 0
        i1 = c
        for row in range(r):
            rn     = array[i0:i1]
            m[row] = rn[:]
            i0     = i1
            i1     = i1 + c

        return m



if __name__== "__main__":
    """
    test code for terminal runs
    both unit tests and full answers
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
    
    # test matrixReshape 1
    method  = 'matrixReshape'
    matrix   = [[1, 2], [3, 4]]
    rows    = 1
    columns = 4 
    observed_answer = sol.matrixReshape(matrix, rows, columns) 
    expected_answer = [[1,2,3,4]]
    e = print_test(expected_answer, observed_answer,method)
    err = err + e
    # test matrixReshape 2
    method  = 'matrixReshape'
    matrix   = [[1, 2], [3, 4]]
    rows    = 4
    columns = 1 
    observed_answer = sol.matrixReshape(matrix, rows, columns) 
    expected_answer = [[1], [2], [3], [4]]
    e = print_test(expected_answer, observed_answer,method)
    err = err + e

    # test matrixReshape 3
    method  = 'matrixReshape'
    matrix   = [[1, 2], [3, 4]]
    rows    = 2
    columns = 5 
    observed_answer = sol.matrixReshape(matrix, rows, columns) 
    expected_answer = matrix
    e = print_test(expected_answer, observed_answer,method)
    err = err + e

    print('')
    if err == 0:
        print('PASSED ALL TESTS')
    else:
        print('FAILED A TEST: DEBUG!!!')



