from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:

            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left + 1, right + 1]

            # if sum is less than target, we can increase it by moving left pointer.
            if sum < target:
                left += 1

            # if sum is greater than target, we can decrease it by moving right pointer.
            else:
                right -= 1
