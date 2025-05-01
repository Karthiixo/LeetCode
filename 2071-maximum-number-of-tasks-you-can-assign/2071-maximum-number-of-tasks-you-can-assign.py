class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        from sortedcontainers import SortedList
        tasks.sort()
        workers.sort()

        def can_assign(k):
            available_workers = SortedList(workers[-k:])
            pills_left = pills

            for i in range(k-1, -1, -1):  # hardest to easiest task
                task_strength = tasks[i]

                # If strongest worker can do it — assign
                if available_workers and available_workers[-1] >= task_strength:
                    available_workers.pop(-1)

                # Else, use a pill for the weakest possible worker who can reach task_strength
                elif pills_left > 0:
                    idx = available_workers.bisect_left(task_strength - strength)
                    if idx < len(available_workers):
                        available_workers.pop(idx)
                        pills_left -= 1
                    else:
                        return False
                else:
                    return False

            return True

        left, right = 0, min(len(tasks), len(workers))
        result = 0

        while left <= right:
            mid = (left + right) // 2
            if can_assign(mid):
                result = mid
                left = mid + 1
            else:
                right = mid - 1

        return result
