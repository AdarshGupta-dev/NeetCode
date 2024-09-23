from typing import List


class Solution:

    # we need to convert a list of string to a single string and back to original form.
    # we cannot add "--" or something as string may already have same separator, and our logic will fail.
    # we are adding length of string and separator. e.g. "4-". Now are are sure 4 character after - is part of original list.
    # we also need "-" as 4word will fail if first character of word is number.

    def encode(self, strs: List[str]) -> str:
        final = ""

        for i in strs:
            final += f"{len(i)}-{i}"

        return final

    def decode(self, s: str) -> List[str]:

        final = []
        i = 0
        length = len(s)

        while i < length:
            j = i

            while s[j] != '-':
                j += 1

            t = int(s[i:j])
            final.append(s[j + 1: j + t + 1])

            i = j + t + 1

        return final
