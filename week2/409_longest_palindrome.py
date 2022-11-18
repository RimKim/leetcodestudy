# https://leetcode.com/problems/longest-palindrome/description/
from collections import defaultdict


def longest_palindrome(self, s: str) -> int:
    if len(s) == 1:
        return 1

        # create frequency dictionary
    freq_dist = defaultdict(int)
    for letter in s:
        if letter in freq_dist:
            freq_dist[letter] += 1
        else:
            freq_dist[letter] = 1

    if len(freq_dist.values()) == len(s):
        return 1

    freq_sum = 0
    all_even_number = True
    for v in freq_dist.values():
        if v % 2 == 0:
            freq_sum += v
        else:
            all_even_number = False
            freq_sum += v - 1

    return freq_sum if all_even_number else freq_sum + 1
