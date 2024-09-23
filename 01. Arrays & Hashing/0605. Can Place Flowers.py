from typing import List


# solution 1
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        end = len(flowerbed)

        # we can plant flowers at both ends,
        # if second left and second right does not have flowers already.
        # adding zeros to each end. No edge cases does not need to be handled.
        flowerbed = [0] + flowerbed + [0]
        available_spaces = 0

        # starting from 1, as we have added dummy 0 in beginning
        index = 1

        while index <= end:
            # checking if condition has already been satisfied. No need to check any further.
            if n <= available_spaces:
                return True

            # if there is a flower, increasing count by 2, we can not plant next to it.
            if flowerbed[index] == 1:
                index += 2
                continue

            # checking if all condition are satisfied.
            elif (flowerbed[index - 1] == 0
                  and flowerbed[index] == 0
                  and flowerbed[index + 1] == 0):
                available_spaces += 1
                index += 2  # no need to check adjutant plot, as can not plant there.
                continue

            index += 1
            continue

        return n <= available_spaces


# solution 2
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):

            # Check if the current plot is empty.
            if flowerbed[i] == 0:

                # Check if the left and right plots are empty.
                empty_left_plot = (i == 0) or (flowerbed[i - 1] == 0)
                empty_right_lot = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)

                # If both plots are empty, we can plant a flower here.
                if empty_left_plot and empty_right_lot:
                    flowerbed[i] = 1
                    count += 1
                    if count >= n:
                        return True

        return count >= n
