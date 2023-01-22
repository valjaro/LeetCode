class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        w1 =  min(strs,key=len)
        strs.remove(w1)
        i = 0
        pre = w1
        while i < len(w1):
            for w in strs:
                if not w.startswith(pre):
                    pre = pre[:-1]
            i += 1
        return pre
if __name__ == "__main__":
    s = Solution()
    strs = ["dog","racecar","car"]
    r = s.longestCommonPrefix(strs)
    print(r)