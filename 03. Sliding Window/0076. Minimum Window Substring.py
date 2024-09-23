class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # in window_hashmap we will store frequency of current window of sub-string
        window_hashmap = {}

        # in string_hashmap we will store, frequency of characters in t.
        string_hashmap = {}

        # populating string_hashmap
        for alphabet in t:
            string_hashmap[alphabet] = string_hashmap.get(alphabet, 0) + 1

        # current_match is count of keys for whom values are same in window_hashmap and string_hashmap
        # required_match is maximum matches required that would satisfy our conditions.
        current_match = 0
        required_match = len(string_hashmap)

        # we will store left and right pointers, if conditions are satisfied.
        answer_indices = None

        # we are using sliding window technique. Left pointer will be 0.
        left_pointer = 0

        for right_pointer in range(len(s)):

            # all other alphabet in s, but not in t; are useless. Ignoring them.
            alphabet = s[right_pointer]
            if alphabet not in string_hashmap:
                continue

            # updating window_hashmap
            window_hashmap[alphabet] = window_hashmap.get(alphabet, 0) + 1

            # if count is exactly same, that means we had match in these iterations.
            # if count is greater, we had match in previous iterations.
            if window_hashmap[alphabet] == string_hashmap[alphabet]:
                current_match += 1

            # if we have all matches, then we have a sub-string that satisfy out conditions.
            if current_match == required_match:

                # trying to shrink sub-string from left side.
                # removing form left side.
                while left_pointer < right_pointer:

                    # all other alphabet in s, but not in t; are useless. Ignoring them.
                    alphabet = s[left_pointer]
                    if alphabet not in string_hashmap:
                        left_pointer += 1
                        continue

                    # we are at point, that if we remove character at left index, we will not longer satisfy out conditions.
                    # we have our smallest sub-string till right_pointer
                    if window_hashmap[s[left_pointer]] == string_hashmap[s[left_pointer]]:
                        break

                    # we have extra copy of character at left_pointer, we can safely remove it.
                    else:
                        window_hashmap[s[left_pointer]] -= 1
                        left_pointer += 1

                # first sub-string which satisfies our conditions
                if answer_indices is None:
                    answer_indices = left_pointer, right_pointer

                # checking if new answer is smaller than current answer.
                elif answer_indices[1] - answer_indices[0] > right_pointer - left_pointer:
                    answer_indices = left_pointer, right_pointer

        # no such sub-string was found. 
        if answer_indices is None:
            return ""

        return s[answer_indices[0]: answer_indices[1] + 1]
