class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        hidden = [0]

        for d in differences:
            hidden.append(hidden[-1] + d)
            
        mn = min(hidden)
        mx = max(hidden)

        res = (upper - mx) - (lower - mn) + 1

        return res if res > 0 else 0
        
