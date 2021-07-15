'''
Median of Two Sorted Arrays
'''

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):

        '''
        merged_array = nums1 + nums2
        merged_array= sorted(merged_array)
        length= len(merged_array)
        if length%2 == 0:
            print("yes")
            median =  (merged_array[(length//2) -1] + merged_array[(length//2) ]) / 2
        else :
            median = merged_array[length//2]
            
        return median
        '''

        nums1+=nums2
        nums1.sort()
        n = len(nums1)
        mid = n/2
        if n%2==0:
            mid = int(mid)
            return (nums1[mid] + nums1[mid-1])/2
        else:
            return nums1[int(mid)]
