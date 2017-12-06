"""
Problem: 566 Reshape Matrix
Level: Easy
Technique: 
Status: 

Problem Description:
In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different size but keep its original data.
You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively.
The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.
If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix. 
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
        e   = r   * c
        r0 = len(nums)
        c0 = len(nums[0])
        e0 = r0 * c0
        if e != e0:
            print('Dimensions inaccurately input')
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
    hacked test code for terminal runs
    """
    m0 = [[1, 2], [3, 4]] 
    s  = Solution()
    m1 = s.matrixReshape(m0,4,1) 
    print(m1)


    #print('Expected Answer is {}'.format(expected_answer))
    #print('Observed Answer is {}'.format(observed_answer))
