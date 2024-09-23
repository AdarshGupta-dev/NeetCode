from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # iterating through all numbers and counting there frequency
        occrance_frequency = {}
        for number in nums:
            occrance_frequency[number] = occrance_frequency.get(number, 0) + 1

        # frequency table. Which numbers appeared this many times.
        # for e.g. if index 1 have 2. It will mean, number 2 appeared exactly 2 times in nums.
        # list because, 2 or more different numbers can appear extract n times.
        frequency_table = [[] for _ in range(len(nums) + 1)]
        for number, frequency in occrance_frequency.items():
            frequency_table[frequency].append(number)

        # higher frequency will be at last. Thus starting from last element.
        result = []
        for number in frequency_table[::-1]:
            result.extend(number)

            # we need only k most frequent numbers.
            if len(result) == k:
                break

        return result
