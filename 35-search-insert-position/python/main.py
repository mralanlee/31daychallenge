class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        """ exit early for weird cases """
        """ covers empty array """
        if len(nums) < 1:
            return 0

        """ if this is smaller than the lowest item in the array, return 0"""
        if target < nums[0]:
            return 0

        """ if target is larger than the largest element in array, then make it the last one"""
        if target > nums[len(nums) - 1]:
            return len(nums)

        """ using binary search because of sorted array """

        """ create helper function so I can do this recursively"""
        def helper(arr, left, right):
            mid = left + (right - left) // 2
            if arr[mid] == target:
                return mid

            """ [0, 2, 4] target=1 """
            """ 0 (mid - 1) < target=1 < 2 (old mid index) < 4 """
            if arr[mid - 1] < target and target < arr[mid]:
                return mid

            """ 2 (mid) < target=3 < 5 (mid+1)... [0,3,5]"""
            if arr[mid] < target and target < arr[mid + 1]:
                return mid + 1

            if arr[mid] > target:
                """
                this means that the mid point is now greater than our sorted array
                so in an example [1, 3, 5, 6] and our target is 5
                """
                return helper(arr, left, mid - 1)
            else:
                return helper(arr, mid + 1, right)

        return helper(nums, 0, len(nums) - 1)
