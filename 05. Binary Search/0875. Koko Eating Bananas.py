from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def can_eat_all_banana(speed: int) -> bool:
            time = 0
            for pile in piles:
                # Equivalent to math.ceil(pile / speed)
                # how does this work.
                # suppose pile is 4 and speed is 3.
                # trick is to add something that makes 4 next divisible number i.e. 6; but divisible numbers should not become next divisible number
                # we can not make 3, 6, or 9 next divisible number. so we are adding 1 less than speed.
                time += (pile + speed - 1) // speed
                if time > h:
                    return False
            return True

        low, high = 1, max(piles)

        while low <= high:
            mid = (low + high) // 2

            if can_eat_all_banana(mid):
                high = mid - 1
            else:
                low = mid + 1

        return low  # Low will be the minimum speed once the loop terminates
