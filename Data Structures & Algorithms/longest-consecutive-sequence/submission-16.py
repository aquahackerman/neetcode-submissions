class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_no = max(abs(x) for x in nums)
        neg_max = -max_no
        numbers = [0] * (1 + (max_no) * 2)
        
        for number in nums:
            index = number + max_no
            print(index)
            numbers[index] = 1

        max_length = 0
        iterator = 0
        max_index = neg_max
        for i, number in enumerate(numbers):
            if number != 0:
                iterator += 1
            else:
                iterator = 0
            if iterator == 1:
                last_index = i
            if max_length < iterator:
                max_index = last_index
                max_length = iterator
        
        
        return max_length 



