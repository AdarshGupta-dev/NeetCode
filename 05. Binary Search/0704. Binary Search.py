from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            # we have found the target. Returning its index
            if nums[mid] == target:
                return mid

            # If x is greater, ignore left half
            elif nums[mid] < target:
                low = mid + 1

            # If x is smaller, ignore right half
            else:
                high = mid - 1

        # If we reach here, then the element
        # was not present
        return -1
