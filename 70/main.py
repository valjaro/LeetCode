# https://leetcode.com/problems/climbing-stairs/

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        visited = []
        # final_list = [1] * n
        # lst = [[1], [2]]
        # if n <= 2: return n
        # i = 0
        # while final_list not in visited:
        #     aux_list = [lst[i], lst[i]]
        #     check1 = aux_list[0] + [1]
        #     check2 = aux_list[1] + [2]
        #     lst.append(check1)
        #     lst.append(check2)
        #     if sum(check1) == n and check1 not in visited:
        #         visited.append(check1)
        #     if sum(check2) == n and check2 not in visited:
        #         visited.append(check2)
        #     i += 1
        # return (len(visited))
        if n <= 2: return n
        one_step_before = 2
        two_steps_before = 1
        all_ways = 0
        for i in range(2, n):
            all_ways = one_step_before + two_steps_before
            two_steps_before = one_step_before
            one_step_before  = all_ways
        return all_ways

                
            
            
            

if __name__ == "__main__":
    s = Solution()
    n = 4
    r = s.climbStairs(n)
    print(r)