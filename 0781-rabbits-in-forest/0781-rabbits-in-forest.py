class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        from collections import defaultdict

        count_map = defaultdict(int)
        result = 0

        for answer in answers:
            count_map[answer] += 1
            if count_map[answer] > answer:
                result += count_map[answer]
                count_map[answer] = 0

        for key, value in count_map.items():
            if value != 0:
                result += key + 1

        return result