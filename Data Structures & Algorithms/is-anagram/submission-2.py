class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        for letter in s:
            if not letter in dic:
                dic[letter] = 1
            else:
                dic[letter] += 1
        val = 0
        
        for letter in t:
            if not letter in dic:
                return False
            else:
                if dic[letter] == 0:
                    return False
                dic[letter] -= 1
                if dic[letter] == 0:
                    val += 1
            
        
        if val == len(dic):
            return True
        else:
            return False
        
            
            