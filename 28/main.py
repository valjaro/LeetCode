# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        length = len(haystack) - len(needle)
        for i in range(0, length + 1):
            print(haystack[i:i+len(needle)])
            if needle == haystack[i:i+len(needle)]:
                return i
        return -1

if __name__ == "__main__":
    s = Solution()
    haystack = "sadbutsad"
    needle = "sad"
    r= s.strStr(haystack, needle)
    print(r)