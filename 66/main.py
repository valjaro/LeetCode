# https://leetcode.com/problems/plus-one/

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        k = 0
        for i in range(len(digits)):
            k = 10 * k + digits[i]
        k += 1
        return [int(i) for i in str(k)]
if __name__ == "__main__":
    s = Solution()
    digits = [9]
    r = s.plusOne(digits)
    print(r)