from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            # Calculate the mid-index
            mid = (low + high) // 2

            # If the middle element is the target, return its index
            if nums[mid] == target:
                return mid

            # Determine if the left half is sorted
            if nums[low] <= nums[mid]:
                # Check if the target lies within the sorted left half
                if nums[low] <= target < nums[mid]:
                    # If yes, discard the right half and search the left half
                    high = mid - 1
                else:
                    # Otherwise, discard the left half and search the right half
                    low = mid + 1
            else:
                # Otherwise, the right half must be sorted
                # Check if the target lies within the sorted right half
                if nums[mid] < target <= nums[high]:
                    # If yes, discard the left half and search the right half
                    low = mid + 1
                else:
                    # Otherwise, discard the right half and search the left half
                    high = mid - 1

        # If the target is not found, return -1
        return -1
