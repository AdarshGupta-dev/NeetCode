from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # we need to group words by anagram
        final = {}

        for word in strs:

            # sorting word alphabetically.
            # sorted takes iterator and return sorted iterator
            # join takes iterator and add them together to form a string.
            sorted_word = ''.join(sorted(word))

            # is sorted_word is in final, that we have word that is anagram of previously added word. 
            # adding this word to list.
            if sorted_word in final:
                final[sorted_word].append(word)

            # if not, this word is first of kind.
            else:
                final[sorted_word] = [word]

        # values are our answer. Adding them a list.
        return list(final.values())
