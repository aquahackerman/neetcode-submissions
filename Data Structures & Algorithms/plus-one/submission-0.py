class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        while True:
            k = digits[i]
            if k == 9:
                digits[i] = 0
                i -= 1
                if i == -1:
                    digits.insert(0, 1)
                    break
                continue
            else:
                k += 1
                digits[i] = k
                break
        return digits
