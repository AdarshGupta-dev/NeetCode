from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # converting to set and checking if both are still same.
        return len(nums) != len(set(nums))
