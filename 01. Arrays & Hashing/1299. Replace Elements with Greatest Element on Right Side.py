from typing import List


# Solution 1
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        new_list = []
        new_max = -1

        for i in reversed(arr):
            new_list.append(new_max)
            new_max = max(i, new_max)

        return reversed(new_list)


# Solution 2
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        new_max = -1

        # starting from right as number are to be replaced with max from right.
        for i in range(len(arr) - 1, -1, -1):
            temp = arr[i]
            arr[i] = new_max
            new_max = max(temp, new_max)

        return arr
