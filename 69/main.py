# https://leetcode.com/problems/sqrtx/

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        sqrt = x / 2
        temp = 0
        while sqrt != temp:
            temp = sqrt
            sqrt = (x/temp + temp) /2
        return int(sqrt)

if __name__ == "__main__":
    s = Solution()
    digits = 8
    r = s.mySqrt(digits)
    print(r)