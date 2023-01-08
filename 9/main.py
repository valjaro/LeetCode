class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """ 
        x = [d for d in str(x)]
        for i in range(len(x)):
            if x[i] != x[-i - 1]:
                return False
        return True    

if __name__ == "__main__":
    s = Solution()
    i = 121
    r = s.isPalindrome(i)
    print(r)