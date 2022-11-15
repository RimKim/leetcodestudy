# https://leetcode.com/problems/n-th-tribonacci-number/description/


class Solution:
    def tribonacci(self, n: int) -> int:
        # use a nested function with memoization
        def tribonacci_recursive(n, memoize):
            if n in memoize:
                return memoize[n]
            # Pycharm uses backslash line continuation, which is a style violation
            # Used therefore parentheses
            memoize[n] = (tribonacci_recursive(n - 1, memoize)
                          + tribonacci_recursive(n - 2, memoize)
                          + tribonacci_recursive(n - 3, memoize))
            return memoize[n]

        memoize = {0: 0, 1: 1, 2: 1}  # store for base case
        return tribonacci_recursive(n, memoize)

    # with recursive => time: O(n), space: O(n) for memoization and recursion
    # with iterative => time: O(n), space: O(1)
    def tribonacci_iterative(self, n: int) -> int:
        if n == 0:
            return 0
        t_0, t_1, t_2 = 0, 0, 1
        for i in range(3, n + 1):
            t_3 = t_0 + t_1 + t_2
            t_0, t_1, t_2 = t_1, t_2, t_3

        return t_0 + t_1 + t_2


