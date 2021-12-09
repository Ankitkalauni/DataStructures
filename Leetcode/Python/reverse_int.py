class Solution:
    def reverse(self, x):
        import sys
        is_neg = False

        if x<0:
            is_neg = True
            x = abs(x)

        ans = 0
        while(x!=0):
            ans = (ans * 10) + x % 10
            if ((ans > 2**31-1) or (ans < (-2**31)) ):
                return 0
            x = x//10

        if is_neg:
            return -ans
        else:
            return ans


if __name__ == '__main__':
    Solution().reverse(-123)
