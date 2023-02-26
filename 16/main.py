
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        import math
        nums.sort()
        diff = 10**5 + 1
        r_sum = 0
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                r = nums[i] + nums[j] + nums[k]
                dist = math.sqrt((r - target)**2)
                if dist < diff:
                    diff = dist
                    r_sum = r
                if r < target:
                    j += 1
                elif r > target:
                    k -= 1
                else:
                    return r
        return r_sum
                
if __name__ == "__main__":
    s = Solution()
    nums, target = [-1000,-1000,-1000], 10000
    r = s.threeSumClosest(nums, target)
    print(r)