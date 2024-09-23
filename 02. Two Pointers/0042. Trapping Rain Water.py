from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # the trick to solving this is to realise, each number can store water min(max in right side, max in left side) - self height.
        left_max = []
        right_max = []

        # finding max at left side.
        temp = 0
        for i in range(len(height)):
            left_max.append(temp)
            temp = max(temp, height[i])

        # finding max at right_max side.
        temp = 0
        for i in range(len(height) - 1, -1, -1):
            right_max.append(temp)
            temp = max(temp, height[i])

        # reversing for easier calculation
        right_max.reverse()

        # calculating max water it can store.
        sum = 0
        for i in range(len(height)):
            temp = min(left_max[i], right_max[i]) - height[i]
            if temp > 0:
                sum += temp

        return sum


# optimized approach.
class Solution:
    def trap(self, height: List[int]) -> int:
        # the trick to solving this is to realise, each number can store water min(max in right side, max in left side) - self height.
        total_capacity = 0
        left_max_list = [0]
        current_left_max = height[0]

        # finding max at left side.
        for i in range(1, len(height)):
            left_max_list.append(current_left_max)

            if height[i] > current_left_max:
                current_left_max = height[i]

        # calculating right max, and storage_capacity
        # no need to start from right most, as it will never hold any water.
        current_right_max = height[-1]
        for i in range(len(height) - 2, -1, -1):
            min_of_maxes = min(current_right_max, left_max_list[i])
            storage_capacity = min_of_maxes - height[i]

            if storage_capacity > 0:
                total_capacity += storage_capacity

            if height[i] > current_right_max:
                current_right_max = height[i]

        return total_capacity
