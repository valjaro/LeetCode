# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution(object):
    
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        s = set()
        length = len(nums)
        j = len(nums) - 1
        for i in range(0, length):
            if nums[i] in s:
                nums[i] = '_'
                while i != j:
                    if nums[j] not in s:
                        s.add(nums[j])
                        nums[i], nums[j] = nums[j], nums[i]
                        count += 1
                        j -= 1
                        break
                    else:
                        nums[j] = "_"
                        j -= 1
            else:
                s.add(nums[i])
                count += 1
            if i == j: break
        print(nums)
        return count
            

if __name__ == "__main__":
    s = Solution()
    nums = [0,0,1,1,1,2,2,3,3,4]
    rint= s.removeDuplicates(nums)
    print(rint)