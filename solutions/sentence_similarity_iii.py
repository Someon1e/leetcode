# https://leetcode.com/problems/sentence-similarity-iii/description/


class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        words_smaller = sentence1.split(" ")
        words_bigger = sentence2.split(" ")

        len_words_smaller = len(words_smaller)
        if len_words_smaller > len(words_bigger):
            words_smaller, words_bigger = words_bigger, words_smaller

        # Redundant optimisation
        elif len_words_smaller == len(words_bigger):
            return words_bigger == words_smaller

        # Check starting words
        offset = 0
        for word in words_smaller:
            if words_bigger[offset] == word:
                offset += 1
            else:
                break
        if offset == len_words_smaller:
            # All words were at the start
            return True

        # Check ending words
        ends_with = True
        for index, word in enumerate(
            reversed(
                words_smaller[offset:]  # Words that weren't at the start
            )
        ):
            if words_bigger[-index - 1] != word:
                ends_with = False
        if ends_with:
            return True

        return False


from leetcode import test

test(Solution().areSentencesSimilar("Aa a", "A a a"), False)
test(Solution().areSentencesSimilar("My name is Haley", "My Haley"), True)
test(Solution().areSentencesSimilar("of", "A lot of words"), False)
test(Solution().areSentencesSimilar("Eating right now", "Eating"), True)
test(Solution().areSentencesSimilar("Eating right now", "now"), True)
