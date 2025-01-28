# https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/description/


class Solution:
    def finalPrices(self, prices):
        answer = []
        for i, price in enumerate(prices):
            discounted = price
            if i != len(prices):
                for discount in prices[i + 1 :]:
                    if discount <= price:
                        discounted = price - discount
                        break
            answer.append(discounted)
        return answer


from leetcode import test


test(Solution().finalPrices([8, 4, 6, 2, 3]), [4, 2, 4, 2, 3])
test(Solution().finalPrices([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
test(Solution().finalPrices([10, 1, 1, 6]), [9, 0, 1, 6])
