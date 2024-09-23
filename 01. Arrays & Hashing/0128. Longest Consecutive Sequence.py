from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # we need to find start of sequence, then we can find its length.

        # converting to set for ease.
        nums = set(nums)
        greatest_max = 0

        for n in nums:

            # if n -1 exists in nums, it is not start of sequence.
            if n - 1 in nums:
                continue

            # we can have multiple sequences, checking length of current sequence.
            temp_max = 1
            while True:
                n += 1
                if n in nums:
                    temp_max += 1

                else:
                    greatest_max = max(greatest_max, temp_max)
                    break

        return greatest_max
