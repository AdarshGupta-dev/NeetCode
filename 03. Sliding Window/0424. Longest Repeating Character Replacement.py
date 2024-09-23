class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # keeping track of frequency of all characters in current window.
        frequency_count = {}

        # start of current window.
        left_index = 0

        # maximum frequency of any character out of all characters
        max_frequency = 0

        # right_index in end of out window.
        for right_index in range(len(s)):

            # new character
            character = s[right_index]

            # frequency of new character
            frequency_count[character] = frequency_count.get(character, 0) + 1

            # checking new frequency of new character is greater than current greatest.
            max_frequency = max(max_frequency, frequency_count[character])

            # this is the trick.
            # right_index - left_index + 1 -> total length of current window.
            # max_frequency is frequency of a single character
            # subtracting both will give count of all character that do not have maximum frequency.
            # we are allowed to substitute upto k.
            # if there number become more than k, we have to drop from left.
            if (right_index - left_index + 1) - max_frequency > k:
                # dropping from left. Here dropped can be character with maximum frequency or without.
                frequency_count[s[left_index]] -= 1
                left_index += 1

        # returning length of window.
        return right_index - left_index + 1
