class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # edge case, when s is empty string.
        # null set is sub-set of all sets, including another null set.
        if not s:
            return True

        # need to check if all strings from s, appear in t.
        # they must also appear in same order they did in s.
        index = 0
        for i in t:

            # checking ith character in t is same as index-th character in s.
            # if yes, we found 1 character from s in t, in order. 
            # now, we need to check following characters.
            if i == s[index]:
                index += 1

            # if index is same as length of s, we have found all characters from s in t.
            if index == len(s):
                return True

        # not all characters were found.
        return False
