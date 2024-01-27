def parse_input():
    test_cases = []
    for _ in range(int(input())):
        padlock = input()
        favorite = input()
        test_cases.append((padlock, favorite))
    return test_cases


def solution(test_case):
    padlock, favorite = test_case
    num_op = 0
    for c in padlock:
        c_op = 13
        for f in favorite:
            preceding_op = 26 - abs(ord(c) - ord(f))
            following_op = abs(ord(c) - ord(f))
            min_op = min(preceding_op, following_op)
            if min_op <= c_op:
                c_op = min_op
        num_op += c_op
    return num_op


if __name__ == '__main__':
    for i, test_case in enumerate(parse_input()):
        print("Case #{}: {}".format(i + 1, solution(test_case)))