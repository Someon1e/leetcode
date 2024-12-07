# https://leetcode.com/problems/lemonade-change/description/


class Solution:
    def lemonadeChange(self, bills) -> bool:
        fives = 0
        tens = 0
        # twenties = 0

        for bill in bills:
            match bill:
                case 5:
                    fives += 1
                case 10:
                    tens += 1
                    if fives == 0:
                        return False
                    fives -= 1
                case 20:
                    # twenties += 1
                    if tens == 0:
                        if fives >= 3:
                            fives -= 3
                        else:
                            return False
                    else:
                        tens -= 1
                        if fives == 0:
                            return False
                        fives -= 1

        return True


# TODO: tests
