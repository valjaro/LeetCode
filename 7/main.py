class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        try:
            x = [int(d) for d in str(x)]
            x = x[::-1]
        except:
            x = [d for d in str(x)]
            x = x[::-1]
            x.insert(0, '-')
            for i in range(len(x) - 1, 0, -1):
                if x[i] == '-' or x[i] == '0':
                    x.pop()
                else:
                    break
        finally:
            r = int("".join(map(str, x)))
            if r > (2**31 - 1) or r < -(2**31): return 0
            else:
                return r


if __name__ == "__main__":
    s = Solution()
    i = -1123
    r = s.reverse(i)
    print(r)