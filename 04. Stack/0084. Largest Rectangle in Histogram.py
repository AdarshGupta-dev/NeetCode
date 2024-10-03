from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []  # Stack will store pairs: (index, height)

        # Iterate over each bar in the histogram
        for index, height in enumerate(heights):
            # The `start` variable tracks the furthest left index where the current `height` can extend
            start = index

            # This loop ensures the stack maintains an increasing order of heights
            # If we find a bar that is shorter than the one on top of the stack,
            # it means we need to calculate the largest rectangle that can be formed
            # with the height at the top of the stack.
            while stack and stack[-1][1] > height:
                # Pop the stack since the current height `height` is shorter, meaning
                # we can no longer extend the rectangle represented by the popped height
                start, prev_height = stack.pop()

                # Calculate the maximum area for the popped height, which can extend from `start` to `index - 1`
                max_area = max(max_area, prev_height * (index - start))

            # Push the current height onto the stack, along with the `start` index
            # This ensures that even shorter bars pushed after this one will correctly calculate
            # rectangles from the furthest left point.
            stack.append((start, height))

        # Now process any remaining bars in the stack.
        # These bars extend to the end of the histogram, i.e., to the last index `len(heights) - 1`.
        for start, height in stack:
            max_area = max(max_area, height * (len(heights) - start))

        return max_area
