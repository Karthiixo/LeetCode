class Solution:
    def countSubarrays(self, nums: List[int]) -> int:

        result = 0 

        if len(nums)<3:
            return result

        for num in range(len(nums)-2):
            if (nums[num] + nums[num+2]) == (nums[num+1]/2):
                result =  result + 1
            
        return result