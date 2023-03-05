
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # l_dicc = {
        #     '{': '}',
        #     '[': ']',
        #     '(': ')',
        # }
        # r_dicc = {
        #     '}': '{',
        #     ']': '[',
        #     ')': '(',
        # }
        # i, n = 0, len(s)
        # check = True
        # if n % 2 != 0: return False
        # while i < n:
        #     l_var, r_var = False, False
        #     if s[i] in l_dicc:
        #         l_var = l_dicc[s[i]]
        #         if not l_var in s[i+1:]:
        #             return False
        #     elif s[i] in r_dicc:
        #         r_var = r_dicc[s[i]]
        #         if not r_var in s[:i]:
        #             return False
        #     count = 0
        #     if l_var:
        #         j = i
        #         while s[j] != l_var:
        #             count += 1
        #             j += 1
        #     elif r_var:
        #         j = len(s) - i
        #         while s[j] != r_var:
        #             count += 1
        #             j -= 1
        #     if (count - 1) % 2 != 0:
        #             return False
        #     i += 1
        # return check
        l_dicc = {
            '{': '}',
            '[': ']',
            '(': ')',
        }
        i, n = 0, len(s)
        check = True
        if n % 2 != 0: return False
        stack = []
        l_var = False
        while i < n:
            if s[i] in l_dicc:
                stack.append(s[i])
                l_var = l_dicc[stack[-1]]
                if not l_var in s[i+1:]:
                    return False
            else:
                if s[i] != l_var:
                    return False
                stack.pop()
                l_var = l_dicc[stack[-1]] if len(stack) > 0 else False
            i += 1
        if len(stack) > 0: return False
        return check
        
if __name__ == "__main__":
    s = Solution()
    sv = "[[[]"
    r = s.isValid(sv)
    print(r)