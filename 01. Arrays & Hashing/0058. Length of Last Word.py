# Solution 1
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split()[-1])

    # Solution 2


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0

        # iterating from right side, until we see an space
        for i in range(len(s) - 1, -1, -1):
            if not i:
                return count
            else:
                count += 1

        return count
