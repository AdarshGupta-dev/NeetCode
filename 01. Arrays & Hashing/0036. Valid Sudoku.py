from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # for sudoku to be valid, it must pass 3 condition. 
        # 1. No duplicate in row.  -> this can be tested while iteration.
        # 2. No duplicate in column.  -> need to create new lists 
        # 3. No duplicate in mini-square.  -> need to create new lists.

        rows = [set() for _ in range(9)]
        smaller_squares = [set() for _ in range(9)]

        for i, column in enumerate(board):
            nums = set()

            for j, num in enumerate(column):
                if num == '.':
                    continue

                # condition 1 check.
                if num in nums:
                    return False
                else:
                    nums.add(num)

                # condition 2 check.
                if num in rows[j]:
                    return False
                else:
                    rows[j].add(num)

                # condition 3 check.
                # adding to mini-square list. (j // 3) *3 + (i // 3) will also work.
                if num in smaller_squares[j // 3 + (i // 3) * 3]:
                    return False
                else:
                    smaller_squares[j // 3 + (i // 3) * 3].add(num)

        return True
