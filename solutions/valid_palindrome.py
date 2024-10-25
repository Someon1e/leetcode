# https://leetcode.com/problems/valid-palindrome/description/


class Solution:
    def isPalindrome(self, s: str) -> bool:
        processed = "".join(character for character in s if character.isalnum()).lower()
        return processed[::-1] == processed


from leetcode import test

test(Solution().isPalindrome("A man, a plan, a canal: Panama"), True)
test(Solution().isPalindrome("race a car"), False)
test(Solution().isPalindrome(" "), True)
