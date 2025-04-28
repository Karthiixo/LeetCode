
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        from collections import defaultdict

        total_distinct = len(set(nums))  
        count = 0
        n = len(nums)

        for i in range(n):  
            freq = defaultdict(int)
            distinct_in_window = 0
            for j in range(i, n):  
                if freq[nums[j]] == 0:
                    distinct_in_window += 1
                freq[nums[j]] += 1

                if distinct_in_window == total_distinct:  
                    count += 1
        return count
