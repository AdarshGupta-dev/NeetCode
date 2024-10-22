from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1

        # Check if the array is already sorted (no rotation)
        # If the first element is less than or equal to the last, the smallest element is the first
        if nums[low] <= nums[high]:
            return nums[low]

        # Perform binary search to find the rotation point, which is the smallest element
        while low <= high:
            mid = (low + high) // 2

            # Check if the mid-element is greater than the next element,
            # this means the next element is the smallest (rotation point)
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]

            # Check if the mid-element is smaller than the previous element,
            # this means the mid-element itself is the smallest (rotation point)
            if nums[mid] < nums[mid - 1]:
                return nums[mid]

            # If the mid-element is greater than the last element,
            # it means the smallest element is in the right half (after mid)
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                # If the mid-element is less than or equal to the last element,
                # it means the smallest element is in the left half (before mid)
                high = mid - 1
