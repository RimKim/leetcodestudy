def parse_input():
    test_cases = []
    for _ in range(int(input())):
        n = int(input())
        s = input()
        test_cases.append((n, s))
    return test_cases


# Not valid solution: TLE for test case 2
def solution(test_case):
    n, s = test_case
    sum_distance = 0
    for i in range(n):
        if int(s[i]) == 0:
            left_bin_index, right_bin_index = 2 * n, 2 * n

            # left traversal (i-1...0)
            for left_index in range(i-1, -1, -1):
                if int(s[left_index]) == 1:
                    left_bin_index = left_index
                    break
            # right traversal (i+1...n-1)
            for right_index in range(i+1, n):
                if int(s[right_index]) == 1:
                    right_bin_index = right_index
                    break

            sum_distance += min(abs(i - left_bin_index), right_bin_index - i)

    return sum_distance


if __name__ == '__main__':
    for i, test_case in enumerate(parse_input()):
        print("Case #{}: {}".format(i + 1, solution(test_case)))
