class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        count=0
        start=lastmin=lastmax=-1
        for i,num in enumerate(nums):
            if num==minK: lastmin=i
            if num==maxK: lastmax=i
            if num>maxK or num<minK: start=lastmin=lastmax=i
            count+=min(lastmin,lastmax)-start

        return count
        