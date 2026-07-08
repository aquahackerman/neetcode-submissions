class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        def to_binary(n):
            nonlocal count
            if n == 0:
                return "0"

            binary = ""

            while n > 0:
                if n % 2 == 1:
                    count += 1
                binary = str(n % 2) + binary
                n //= 2

            return binary
        to_binary(n)
        return count