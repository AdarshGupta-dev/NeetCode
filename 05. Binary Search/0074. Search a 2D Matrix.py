from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Get the number of rows and columns in the matrix.
        row_count, column_count = len(matrix), len(matrix[0])

        # Treat the matrix as a continuous sorted array.
        # 'low' is the start index, and 'high' is the end index (last element).
        low, high = 0, row_count * column_count - 1

        # Perform binary search while the search range is valid (low <= high).
        while low <= high:

            # Calculate the middle index as the average of low and high.
            mid = (low + high) // 2

            # Convert the 1D index 'mid' back to 2D matrix coordinates.
            # 'mid // column_count' gives the row, and 'mid % column_count' gives the column.
            mid_element = matrix[mid // column_count][mid % column_count]

            # If the mid-element matches the target, return True.
            if mid_element == target:
                return True

            # If the mid-element is smaller than the target, discard the left half (move low).
            elif mid_element < target:
                low = mid + 1

            # If the mid-element is larger than the target, discard the right half (move high).
            else:
                high = mid - 1

        # If the target is not found in the matrix, return False.
        return False
