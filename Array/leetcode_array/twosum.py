'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
'''

def twosum(arr,tar):
    values = {}
    
    for i, num in enumerate(arr):
        remain = tar - num
        if remain in values:
            return [i,values[remain]]
        else:
            values[num] = i
            
arr = [2,7,11,15]

twosum(arr,9)