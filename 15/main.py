# https://leetcode.com/problems/3sum/
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        sets = []
        set_ = set()
        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    s = [nums[i], nums[j], nums[k]]
                    if tuple(s) not in set_:
                        set_.add(tuple(s))
                        sets.append(s)
                    j += 1
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    k -= 1
        return sets

if __name__ == "__main__":
    s = Solution()
    nums = [-1,0,1,2,-1,-4]
    r = s.threeSum(nums)
    print(r)