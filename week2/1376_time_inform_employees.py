# https://leetcode.com/problems/time-needed-to-inform-all-employees/
from collections import deque, defaultdict
from typing import List


class Solution:
    def num_of_min_timeout(self, n: int, head_id: int, manager: List[int], inform_time: List[int]) -> int:
        # BFS approach
        queue = deque([head_id])
        while queue:
            current_employee = queue.popleft()
            time_employee = inform_time[current_employee]
            subordinates = [i for i in manager if manager[i] == current_employee]
            if not subordinates:
                continue
            for s in subordinates:
                inform_time[s] += time_employee
                queue.append(s)

        return max(inform_time)

    # the function above exceeds the given time probably because the list of subordinate loops everytime
    # for each current_employee and max() iterates through the entire list of inform_time. We can improve this
    # by creating subordinate lists before traversing the tree and storing maximum at every level of the tree
    def num_of_min_bfs(self, n: int, head_id: int, manager: List[int], inform_time: List[int]) -> int:
        # create a dict of list of subordinates for each manager
        subordinates = defaultdict(list)
        for e, m in enumerate(manager):
            subordinates[m].append(e)

        # variable to store maximum of time for each tree level
        result = 0
        queue = deque([head_id])

        while queue:
            current_employee = queue.popleft()
            time_employee = inform_time[current_employee]
            result = max(time_employee, result)

            for s in subordinates[current_employee]:
                inform_time[s] += time_employee
                queue.append(s)

        return result
