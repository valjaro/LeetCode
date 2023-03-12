# https://leetcode.com/problems/regular-expression-matching/
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        import re
        pattern = r'%s' % s
        match = re.search(pattern, p)
        if match:
            return True
        else:
            p = list(p)
            if '.' in p:
                print(1)
            elif '*' in p:
                print(2)
            else:
                return False




if __name__ == "__main__":
    s = Solution()
    b, p = "ab", ".*"
    r = s.isMatch(b,p)
    print(r)