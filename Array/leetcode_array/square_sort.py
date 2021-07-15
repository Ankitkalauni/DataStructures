'''
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
'''

class Solution:
    def sortedSquares(self, numbs):
        n = len(numbs)
        for i in range(n):
            numbs[i] = numbs[i] * numbs[i]
        return sorted(numbs)
    
sol = Solution()
nums = [-4,-1,0,3,10]
sol.sortedSquares(nums)
