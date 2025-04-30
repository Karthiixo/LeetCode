class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max_ele = max(nums)

        pos_dic = {}

        freq = 0
        res = 0
        pos = 0
        for i in range(n):
            if nums[i] == max_ele:
                freq += 1
                pos_dic[pos] = i
                pos += 1
            if freq >= k:
                res += pos_dic[freq-k] + 1

        return res

        