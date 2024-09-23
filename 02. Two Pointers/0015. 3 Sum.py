from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for pointer_1 in range(len(nums) - 2):

            # we have already sorted the list.
            # if first number is positive, we will not find, any other negative number afterwards.
            # exiting the loop.
            if nums[pointer_1] > 0:
                break

            # if number is same as last number, no need to check, we have already tried all combinations.
            if pointer_1 > 0 and nums[pointer_1] == nums[pointer_1 - 1]:
                continue

            # using sliding window on rest of list.
            pointer_2, pointer_3 = pointer_1 + 1, len(nums) - 1

            while pointer_2 < pointer_3:

                # sum of all three pointers
                total_sum = nums[pointer_1] + nums[pointer_2] + nums[pointer_3]

                # if sum is greater, we need to reduce it. Sliding pointer_3 (right most pointer) left, to reduce number it points to.
                if total_sum > 0:
                    pointer_3 -= 1

                # if sum is smaller, we need to increase it. Sliding pointer_2 (middle pointer) right, to increase number it points to.
                elif total_sum < 0:
                    pointer_2 += 1

                # if sum equals to 0. We have out all three numbers.
                else:
                    res.append([nums[pointer_1], nums[pointer_2], nums[pointer_3]])

                    # we still need to check other combinations.
                    # moving second pointer right, until it points to any other number.
                    pointer_2 += 1
                    while nums[pointer_2] == nums[pointer_2 - 1] and pointer_2 < pointer_3:
                        pointer_2 += 1

        return res
