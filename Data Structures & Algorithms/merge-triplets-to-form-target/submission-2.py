class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        t1, t2, t3 = 0, 0 ,0 
        for a,b,c in triplets:
            if a <= target[0] and b<= target[1] and c <= target[2]:
                t1 = max(t1,a)
            
                t2 = max(t2,b)
            
                t3 = max(t3, c)
            if t1 == target[0] and t2 == target[1] and t3 == target[2]:
                return True
        return False
            
            
