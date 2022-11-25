# https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/
from typing import List


# space complexity = O(n+m) n: len of s, m: len of knowledge (num of pairs)
# m for creating dict + n for splitting input s
# time complexity = O(n+m): for split list(n) find value in dict(m)
def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
    str_dict = dict(knowledge)

    split_list = s.split('(')
    for i in range(1, len(split_list)):
        key, rest = split_list[i].split(')')
        split_list[i] = str_dict.get(key, '?') + rest

    return ''.join(split_list)
