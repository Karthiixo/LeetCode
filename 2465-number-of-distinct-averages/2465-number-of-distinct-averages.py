class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()

        l = 0 
        r = len(nums) - 1
        res = set()

        while l < r:
            average = ((nums[l] + nums[r]) / 2)
            res.add(average)
            l += 1
            r -= 1 

        return len(res)       