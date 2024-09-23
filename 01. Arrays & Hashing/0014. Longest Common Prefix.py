from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sub_string = ""

        # edge case, if strs is empty. No strings
        if not strs:
            return sub_string

        first_word = strs[0]

        # maximum length of common prefix cannot be greater than first word / or any word from the list.
        for index in range(len(first_word)):

            # fetching nth character from first word.
            char = first_word[index]

            # checking if rest of the words have same character on nth index.
            for word in strs[1:]:

                # 2 points of failure
                # 1. Word is smaller than n, thus can not any have character on nth position.
                # 2. nth character is not same.
                if len(word) <= index or word[index] != char:
                    return sub_string

            # adding character to sub_string. Now we are sure, every word have this character.
            index += 1
            sub_string += char

        return sub_string
