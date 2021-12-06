class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sum = 0

        while True:
            if n == 0:
                break
            else:
                remainder = n%10
                product = product * remainder
                sum += remainder
                n = n//10

        return product - sum
