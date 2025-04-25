from collections import Counter
from typing import List

class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        prefix_count = 0
        result = 0
        count_map = Counter()
        count_map[0] = 1  # for subarrays starting from index 0

        for num in nums:
            if num % modulo == k:
                prefix_count += 1

            # Current mod value
            current_mod = prefix_count % modulo

            # The target mod we need to find in the map
            target_mod = (current_mod - k) % modulo

            result += count_map[target_mod]

            # Update the count map
            count_map[current_mod] += 1

        return result
