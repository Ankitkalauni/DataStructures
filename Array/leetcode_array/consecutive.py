#1
'''
Given a binary array nums, return the maximum number of consecutive 1's in the array.
'''
nums = [1,1,0,1,1,1,1]

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        # count = 0
        # length = 0
        # for num in nums:
        #     if num == 1:
        #         length += 1
        #     else:
        #         count = max(length, count)
        #         count = 0
        # return max(count, length)
        countt = []
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count+=1
            elif nums[i] == 0:
                countt.append(count)
                count = 0
        if count != 0:
            countt.append(count)
        return max(countt)

            
sett = Solution()
sett.findMaxConsecutiveOnes(nums)