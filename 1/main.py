class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, num in enumerate(nums):
            for j, next in enumerate(nums[(i+1):]):
                if (num+next) == target:
                    return [i, j + i + 1]
        return False


 

if __name__ == "__main__":
    s = Solution()
    i = [3,2,4]
    r = s.twoSum(i, 6)
    print(r)