class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # here we need 2 maps.
        # map1 will keep record of which alphabet of s, we are mapping with witch alphabet of t.
        # map2 can be set, as we only need to know which alphabets of t has already been mapped. 
        map1 = {}
        map2 = set()

        for index in range(len(s)):
            # if ith character is not in map1, but in map2.
            # it has been previously mapped with something.
            if s[index] not in map1 and t[index] in map2:
                return False

            # if ith character of s has been previously mapped but not with ith character of t.
            # one character can not be mapped with 2 characters
            if s[index] in map1 and map1[s[index]] != t[index]:
                return False

            # adding new mapping to map1 and mapped character to set.
            if s[index] in map1 or t[index] not in map2:
                map1[s[index]] = t[index]
                map2.add(t[index])

        return True
