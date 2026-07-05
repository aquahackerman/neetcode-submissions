class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        d = {}
        for no in hand:
            if no in d:
                d[no] += 1
            else:
                d[no] = 1

        sq = list(set(hand))
        sq.sort()
        print(sq)
        i = 0
        while i < len(sq):
        
            no = sq[i]
            print(no, d[no])
            count = d[no]
            if d[no] == 0:
                i += 1
                continue
            for j in range(1, groupSize):
                if no+ j in d and d[no +j] - count >=0:
                    d[no +j] -= count
                else:
                    print(no+j, count)
                    return False
            i += 1
        return True

            

        
            