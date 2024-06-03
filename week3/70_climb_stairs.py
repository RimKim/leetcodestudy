# https://leetcode.com/problems/climbing-stairs/description/
def climb_stairs(self, n: int) -> int:
    def recursive(n, memoize):
        if n in memoize:
            return memoize[n]

        memoize[n] = recursive(n - 1, memoize) + recursive(n - 2, memoize)
        return memoize[n]

    memoize = {1: 1, 2: 2}
    return recursive(n, memoize)

