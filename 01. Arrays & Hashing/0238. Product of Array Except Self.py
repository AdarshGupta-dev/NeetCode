from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # we need to return a list, where on nth index is product of all numbers in nums expect, original number on nth position.

        # approach.
        # we will iterate through original list twice, once from left, and once from right.
        # in each iteration we will multiply with product of n number from original list to n+1 (or n-1 in second iteration) of result.

        length = len(nums)
        product_list = [1] * length

        product = 1
        # from first to second last.
        for i in range(length - 1):
            product *= nums[i]
            product_list[i + 1] = product

        product = 1
        # from last to second.
        for i in range(length - 1, 0, -1):
            product *= nums[i]
            product_list[i - 1] *= product

        return product_list
