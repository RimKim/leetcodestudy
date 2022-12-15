def parse_input():
    test_cases = []
    for _ in range(int(input())):
        n, k, s = map(int, input().split())
        test_cases.append((n, k, s))
    return test_cases


def solution(test_case):
    n, k, s = test_case
    # (K - 1) min to reach initial state
    # 1. start all over again : (K - 1) + 1 + N = K + N
    # 2. return to s and finish the game : (K - 1) + K - S + N - S + 1 = 2 * K - 2 * S + N
    return min(k + n, 2 * k - 2 * s + n)


if __name__ == '__main__':
    for i, test_case in enumerate(parse_input()):
        print("Case #{}: {}".format(i + 1, solution(test_case)))
