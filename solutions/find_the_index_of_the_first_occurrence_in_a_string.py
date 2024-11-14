class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        length = len(needle)
        for index in range(0, len(haystack) - length + 1):
            if haystack[index : index + length] == needle:
                return index
        return -1
