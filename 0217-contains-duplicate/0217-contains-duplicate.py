class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ifuniquenums = set(nums)

        if len(ifuniquenums)==len(nums):
            return False
        else:
            return True
        