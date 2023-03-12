# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        main = []
        aux_list = []
        for i in range(len(s)):
            aux_list.append(s[i])
            for j in range(i+1, len(s)):
                if s[i] != s[j] and s[j] not in aux_list:
                    aux_list.append(s[j])
                else:
                    break
            main.append(len(aux_list))
            aux_list = []
        return max(main) if len(main) > 0 else 0




 

if __name__ == "__main__":
    s = Solution()
    i = ""
    r = s.lengthOfLongestSubstring(i)
    print(r)