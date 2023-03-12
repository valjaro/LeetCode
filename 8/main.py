# https://leetcode.com/problems/string-to-integer-atoi/
class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        ls = list(s.strip())
        if len(ls) == 0 : return 0
        
        sign = -1 if ls[0] == '-' else 1
        if ls[0] in ['-','+'] : del ls[0]
        
        r, i = 0, 0        
        while i < len(ls) and ls[i].isdigit() :
            r = r*10 + ord(ls[i]) - ord('0')
            i += 1
        r = sign * r
        return (r) if r > (-2**31) and r < (2**31 - 1) else (-2**31) if r < 0 else (2**31 - 1)
    
if __name__ == "__main__":
    s = Solution()
    i = " "
    r = s.myAtoi(i) 
    print(r)