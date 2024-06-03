# https://leetcode.com/problems/third-maximum-number/
def third_maximum(nums: list[int]) -> int:
    max_num = 3
    num_list = sorted(set(nums), reverse=True)
    if len(num_list) >= max_num:
        return num_list[max_num - 1]
    else:
        return num_list[0]


if __name__ == "__main__":
    assert third_maximum([3, 2, 1]), 1
    assert third_maximum([1, 2]), 2
    assert third_maximum([2, 2, 3, 1]), 1


