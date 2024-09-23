from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # hard coding first row of pascal's triangle.
        # coding requirement says, input will be of minimum length of 1.
        pascal_triangle_list = [[1]]

        # running input - 1 times, as first has already been hard-coded.
        for _ in range(numRows - 1):

            # fetch last row. Adding padding to prevent handling of edge cases.
            previous_row = [0] + pascal_triangle_list[-1] + [0]

            # creating new row.
            new_row = []
            for index in range(len(previous_row) - 1):
                new_row.append(previous_row[index] + previous_row[index + 1])

            # appending new row
            pascal_triangle_list.append(new_row)

        return pascal_triangle_list
