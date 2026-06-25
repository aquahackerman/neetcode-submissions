class Solution:
    def numDecodings(self, s: str) -> int:
        res = [0 for i in range(len(s) + 2)]
        if int(s[-1]):
            res[-3] = 1
        res[len(s)] = 1
        flag = 0
        for i in range(len(s) - 2, -1, -1):
            no = int(s[i])
            no2 = int(s[i + 1])
            twosum = no * 10 + no2
            if no == 0:
                continue
            else:
                res[i] = res[i + 1]
            
            if twosum <= 26:
                res[i] += res[i + 2]
            

            flag = 0

           


        print(res)
        return res[0]