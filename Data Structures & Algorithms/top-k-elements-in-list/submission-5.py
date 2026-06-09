class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for no in nums:
            if no not in d:
                d[no] = 1
            else:
                d[no] += 1
        final_l = []
        
      
        for key, val in d.items():
            final_l.append([val, key])

        final_l.sort()
        res = []
        while len(res) < k:
            res.append(final_l.pop()[1])
        return res            