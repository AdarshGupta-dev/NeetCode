from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time_taken_map = {}

        # finding out how much time each fleet of car at all position will take time to reach destination.
        for index in range(len(position)):
            # starting point: distance / speed
            time_taken_map[position[index]] = (target - position[index]) / speed[index]

        current_max = 0
        number_of_fleet = 0

        # reverse sorting dict on basis of keys.
        sorted_by_position = dict(sorted(time_taken_map.items(), reverse=True))
        for time_taken in sorted_by_position.values():

            # if fleet can reach destination before fleet ahead of them.
            # they would have to merge with next fleet and slow down.
            # no need to count them.

            # if fleet will take more time than next, they will count as separate fleet.
            if time_taken > current_max:
                current_max = time_taken
                number_of_fleet += 1

        return number_of_fleet
