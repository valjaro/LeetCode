
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i, n = 0, len(s) - 1
        check = True
        while i < n:
            if s[i] == "(" and s[i + 1] != ")":
                check = False
            elif s[i] == "[" and s[i + 1] != "]":
                check = False
            elif s[i] == "{" and s[i + 1] != "}":
                check = False
            i += 2
        return check

if __name__ == "__main__":
    s = Solution()
    sv = "{[]}"
    r = s.isValid(sv)
    print(r)