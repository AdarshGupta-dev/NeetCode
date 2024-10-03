from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []  # pair: [temp, index]

        for index, temperature in enumerate(temperatures):

            # if we have higher temperature than top of stack, we have found an ans.
            # subtracting original index from current index will provide number of days.
            while stack and temperature > stack[-1][0]:
                _, stack_index = stack.pop()
                answer[stack_index] = index - stack_index

            # adding temperature and current index
            stack.append((temperature, index))
        return answer
