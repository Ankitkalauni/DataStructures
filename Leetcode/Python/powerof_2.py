class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        is_pow = False

        for i in range(32):
            if 2**i == n:
                is_pow = True
                break

        return is_pow

    def isPowerOfthree(self, n: int) -> bool:
        is_pow = False

        for i in range(32):
            if 3**i == n:
                is_pow = True
                break

        return is_pow

    def isPowerOffour(self, n: int) -> bool:
        is_pow = False

        for i in range(32):
            if 4**i == n:
                is_pow = True
                break

        return is_pow