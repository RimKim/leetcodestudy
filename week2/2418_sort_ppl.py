# https://leetcode.com/problems/sort-the-people/
from typing import List


class Solution:
    def sort_people(self, names: List[str], heights: List[int]) -> List[str]:
        person_dict = {heights[i]: names[i] for i in range(len(names))}
        return [v for k, v in sorted(person_dict.items(), reverse=True)]
