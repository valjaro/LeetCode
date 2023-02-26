
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic = {
            "2":    "abc",
            "3":    "def",
            "4":    "ghi",
            "5":    "jkl",
            "6":    "mno",
            "7":    "pqrs",
            "8":    "tuv",
            "9":    "wxyz",
        }
        letters_list = []
        first_letters = []
        for i, digit in enumerate(digits):
            if digit in dic:
                letters = list(dic[digit])
                if len(digits) == 1 : return letters
                if i == 0: 
                    first_letters = letters
                    prev_list = []
                    continue
                for j, letter in enumerate(letters):
                    letters_list += [l + letter for l in first_letters]
                first_letters = [x for x in letters_list if x not in prev_list]
                prev_list += first_letters
        return first_letters

if __name__ == "__main__":
    s = Solution()
    nums = "5678"
    r = s.letterCombinations(nums)
    print(r)