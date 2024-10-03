from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Solution is backtracking while storing data in stack.
        1. We can add more open bracket if number of current brackets in stack is less than n.
        2. We can add more close bracket if number of close brackets are less than close brackets in stack.
        3. Lastly, for stack to valid, we need open bracket in stack = close bracket in stack = n
        """
        stack = []
        all_permutations = []

        def backtrack(open_bracket_count, close_bracket_count):

            # condition 3. if all three are equal, we have a solution. adding it to result.
            if open_bracket_count == close_bracket_count == n:
                all_permutations.append("".join(stack))
                return

            # condition 1. if open bracket count is less than n. we can add another.
            if open_bracket_count < n:
                stack.append("(")
                backtrack(open_bracket_count + 1, close_bracket_count)
                stack.pop()

            # condition 2. if close bracket count is less than open bracket count. we can add more.
            if close_bracket_count < open_bracket_count:
                stack.append(")")
                backtrack(open_bracket_count, close_bracket_count + 1)
                stack.pop()

        backtrack(0, 0)
        return all_permutations
