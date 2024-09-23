from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        # requirement want 2 things.
        # count of number not equal to val
        # and first n element must be not equal to val. It does not care about rest of list.

        left_pointer = 0
        for right_pointer in range(len(nums)):

            # if right points to val, nothing to do.
            # if not, moving current number to position of left and sliding both pointers to right.
            if nums[right_pointer] != val:
                # we do not have to swipe numbers, as question does not care about rest of arrays.
                nums[left_pointer] = nums[right_pointer]
                left_pointer += 1

        return left_pointer
