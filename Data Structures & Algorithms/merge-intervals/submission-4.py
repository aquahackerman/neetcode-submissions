class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        s_interval = sorted(intervals)
        
        a,b = s_interval[0][0], s_interval[0][1]
        final_arr = []
        for s,e in s_interval:
            print(s,b)
            if s > b:
                print("d")
                final_arr.append([a,b])
                a,b = s,e
            else:
                
                b = max(b,e)
        final_arr.append([a,b])
        return final_arr
                

