# Brute-force approach.
# works but too slow.
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # converting string to sorted list.
        s1 = "".join(sorted(s1))

        # converting string to set
        s1_character_set = set(s1)

        # iterating over each character in s2.
        for index in range(len(s2)):
            # checking current character of s2 is in s1?
            if s2[index] in s1_character_set:

                # fetching current_window and converting to sorted list.
                current_window = s2[index - len(s1) + 1: index + 1]
                sorted_string = "".join(sorted(current_window))

                # if both sorted list are same, they permutation of s1 exists in s2.
                if sorted_string == s1:
                    return True

        return False


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # storing count in array.
        # index 0 will have count for a.
        # initializing count with 0.
        count_s1, count_s2 = [0] * 26, [0] * 26

        # adding count till length of s1.
        # we do not need any calculation as condition can not be satisfied till len(s1)
        for i in range(len(s1)):
            count_s1[ord(s1[i]) - ord("a")] += 1
            count_s2[ord(s2[i]) - ord("a")] += 1

        # counting exact matches in both counts
        matches = 0
        for i in range(26):
            if count_s1[i] == count_s2[i]:
                matches += 1

        # sliding window.
        # left pointer is at index 0 and right is at len(s1). 
        # minimum sub-string length needed to satisfy our conditions
        left = 0
        for right in range(len(s1), len(s2)):

            # checking if condition has been satisfied
            if matches == 26:
                return True

            # finding index for character
            left_index = ord(s2[left]) - ord("a")
            right_index = ord(s2[right]) - ord("a")

            # updating 
            count_s2[left_index] -= 1
            count_s2[right_index] += 1

            # what if by adding right index, matches becomes equal
            if count_s1[right_index] == count_s2[right_index]:
                matches += 1

            # what if matches were equal, by adding we overshot.
            elif count_s1[right_index] + 1 == count_s2[right_index]:
                matches -= 1

            # what if by removing left index, matches becomes equal
            if count_s1[left_index] == count_s2[left_index]:
                matches += 1

            # what if matches were equal, by removing now, we don't have match.
            elif count_s1[left_index] - 1 == count_s2[left_index]:
                matches -= 1

            # moving left pointer
            left += 1

        # what if condition were satisfied after last loop
        return matches == 26
