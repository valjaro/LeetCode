
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        n = len(nums)
        if n < 4: return result
        for i in range(0, n - 3):
            j = i +1
            k = n - 2
            l = n - 1
            if n < 0: return []
            while k > j and j > 0:
                while l > k and k > j:
                    # print(nums[i], nums[j], nums[k], nums[l])
                    suma = nums[i] + nums[j] + nums[k] + nums[l]
                    lst = [nums[i], nums[j], nums[k], nums[l]]
                    if suma == target and lst not in result:
                        result.append([nums[i], nums[j], nums[k], nums[l]])
                    if suma < target:
                        k -= 1
                        l = n - 1
                    else:
                        l -= 1
                if suma < target:
                    j += 1
                    k = n - 2
                    l = n - 1
                else:
                    k -= 1
                    l = n - 1
        return result

if __name__ == "__main__":
    s = Solution()
    nums = [2,2,2,2,2]
    target = 8
    r = s.fourSum(nums, target)
    print(r)