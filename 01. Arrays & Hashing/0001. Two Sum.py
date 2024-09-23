from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # we will add target - current = required here.
        required_number_map = {}

        for index, num in enumerate(nums):

            # checking if previous numbers have requirement for current.
            if num in required_number_map:
                # returning index of previous number's and current number's
                return [required_number_map[num], index]

            # if current number was not need beforehand, it's requirement to map
            required_number_map[target - num] = index

        # no need to add default return as we are sure, above return will always be hit.
