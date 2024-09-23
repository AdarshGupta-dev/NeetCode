class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if lengths of strings are not same, they can not be anagram.
        if len(s) != len(t):
            return False

        # converting string to list for sorting.
        s = [x for x in s]
        t = [x for x in t]

        # sorting and checking if both are same or not.
        return sorted(s) == sorted(t)
