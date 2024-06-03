# https://leetcode.com/problems/set-mismatch/
def set_mismatch(nums: list[int]) -> list[int]:
    freq_dict = {i + 1: 0 for i in range(len(nums))}
    for n in nums:
        freq_dict[n] += 1

    freq_list = list(freq_dict.values())
    if 0 not in freq_list:
        return []
    else:
        return [freq_list.index(2) + 1, freq_list.index(0) + 1]
