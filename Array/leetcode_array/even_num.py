'''
Find Numbers with Even Number of Digits
'''
nums = [555,901,482,1771]

class Solution:
    def findNumbers(self, nums):
        countt = []
        count = 0
        for i in range(len(nums)):
            countt.append(len(str(nums[i])))
            
        for j in countt:
            if j%2==0:
                count+=1
        return count
            
sett = Solution()
sett.findNumbers(nums)
