class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        dp = [[] for _ in range(numRows)]
        s = list(s)
        i = 0
        even = 0
        while i < len(s):
                aux =0
                if even%2 == 0:
                    for j in range(numRows):
                        if (i + aux) < len(s):
                            dp[j].append(s[i + aux])
                            aux += 1
                else:
                    
                    for j in range(numRows - 2, 0, -1):
                        if (i + aux) < len(s):
                            dp[j].append(s[i + aux])
                            aux+=1
                i += aux
                even += 1
        r = "".join(["".join(lista) for lista in dp])
        return r

if __name__ == "__main__":
    s = Solution()
    i = "PAYPALISHIRING"
    numRows = 3
    r = s.convert(i, numRows)
    print(r)