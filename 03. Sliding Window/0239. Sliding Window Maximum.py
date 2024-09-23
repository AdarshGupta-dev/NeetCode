from typing import List


# Brute force approach. Works but needs optimization.
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        left_pointer = 0
        current_max = max(nums[left_pointer: k])
        response = [current_max]

        for index in range(k, len(nums)):
            num = nums[index]
            if num > current_max:
                current_max = num
            elif nums[left_pointer] == current_max:
                current_max = max(nums[left_pointer+1: index+1])

            response.append(current_max)
            left_pointer += 1

        return response

