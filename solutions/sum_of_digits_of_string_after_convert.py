# https://leetcode.com/problems/sum-of-digits-of-string-after-convert/description/


class Solution:
    def getLucky(self, s: str, k: int) -> int:
        value = {
            "a": 1,
            "b": 2,
            "c": 3,
            "d": 4,
            "e": 5,
            "f": 6,
            "g": 7,
            "h": 8,
            "i": 9,
            "j": 1 + 0,
            "k": 1 + 1,
            "l": 1 + 2,
            "m": 1 + 3,
            "n": 1 + 4,
            "o": 1 + 5,
            "p": 1 + 6,
            "q": 1 + 7,
            "r": 1 + 8,
            "s": 1 + 9,
            "t": 2 + 0,
            "u": 2 + 1,
            "v": 2 + 2,
            "w": 2 + 3,
            "x": 2 + 4,
            "y": 2 + 5,
            "z": 2 + 6,
        }
        transformed = sum(value[character] for character in s)

        for i in range(k - 1):
            transformed = sum(int(character) for character in str(transformed))
        return transformed


from leetcode import test

test(Solution().getLucky("iiii", 1), 36)
test(Solution().getLucky("leetcode", 2), 6)
test(Solution().getLucky("zbax", 2), 8)
