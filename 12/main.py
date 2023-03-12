# https://leetcode.com/problems/integer-to-roman/
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        numbers = [1, 4, 5, 9, 10, 40, 50, 90,
        100, 400, 500, 900, 1000]
        sym = ["I", "IV", "V", "IX", "X", "XL",
            "L", "XC", "C", "CD", "D", "CM", "M"]
        i = 12
        r = ""
        while num:
            div = num // numbers[i]
            num %= numbers[i]
            while div:
                r += sym[i]
                div -= 1
            i -= 1
        return r


if __name__ == "__main__":
    s = Solution()
    num = 58
    r = s.intToRoman(num)
    print(r)