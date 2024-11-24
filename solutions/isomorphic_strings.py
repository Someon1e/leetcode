# https://leetcode.com/problems/isomorphic-strings/description/


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        for a, b in zip(s, t):
            if a in mapping:
                if mapping[a] != b:
                    return False
            else:
                if b in mapping.values():
                    return False

                mapping[a] = b

        return True


# TODO: tests
