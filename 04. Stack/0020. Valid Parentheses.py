class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}

        for char in s:

            # checking if character is opening brackets.
            if char in bracket_map.values():
                stack.append(char)

            # checking if character is closing brackets.
            elif char in bracket_map:

                # checking if stack is not empty and top of stack is matching pair.
                if not stack or stack.pop() != bracket_map[char]:
                    return False

            # if string contain anything other than brackets.
            else:
                return False

        # if anything in stack -> False. Empty stack -> True
        return not stack
