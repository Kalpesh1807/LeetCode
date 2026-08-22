# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        i = 0 
        j = len(nums) - 1

        while i <= j:
            mid = (i + j) // 2 

            if target == nums[mid]:
                return mid
            
            if target > nums[mid]:
                i = mid + 1
            else:
                j = mid - 1

        return i
