# https://leetcode.com/problems/roman-to-integer/
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if 1 <= len(s) <= 15:
            d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000,}
            n = 0
            for index, symbol in enumerate(s):
                i = list(d).index(s[index]) if symbol in d.keys() else False
                j = list(d).index(s[index+1]) if (index+1 < len(s)) else False
                val = list(d.values())[i] if i is not False else 0
                val2 = list(d.values())[j] if j is not False else 0
                n+=(((-d[symbol]) if (val < val2) else d[symbol]) if val > 0 or val2 > 0 else False)
            return n if (n >0 and n <= 3999) else 0
        return 0
 

if __name__ == "__main__":
    s = Solution()
    i = "MMMDCCCLXXXVIII"
    r = s.romanToInt(i)
    print(r)