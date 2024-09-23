class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left_index = 0
        right_index = 0

        # we can have current_sub_string_set as string, but set is faster to add, check and delete. So, set.
        current_sub_string_set = set()
        biggest_sub_string_length = 0

        while right_index < len(s):

            # checking if new character is already part of current_sub_string_set.
            # if yes, removing characters from left, until
            if s[right_index] in current_sub_string_set:

                # removing all element till current character.
                while s[left_index] != s[right_index]:
                    current_sub_string_set.remove(s[left_index])
                    left_index += 1
                left_index += 1

                # here we should also remove old current character.
                # But since we have to add in next line, we can skip it.

            current_sub_string_set.add(s[right_index])
            biggest_sub_string_length = max(biggest_sub_string_length, len(current_sub_string_set))
            right_index += 1

        return biggest_sub_string_length
