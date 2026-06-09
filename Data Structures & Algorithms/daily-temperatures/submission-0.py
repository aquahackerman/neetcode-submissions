class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        s = []
        final = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            if len(s) > 0:
                while s and temp > s[-1][1]:
                    a,b = s.pop()
                    final[a] = i - a
            s.append((i, temp))
        return final
            




        