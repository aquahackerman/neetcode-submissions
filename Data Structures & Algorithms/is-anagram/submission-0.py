class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        for letter in s:
            if not letter in dic:
                dic[letter] = 1
            else:
                dic[letter] += 1
        
        for letter in t:
            if not letter in dic:
                return False
            else:
                dic[letter] -= 1
        
        for key,val in dic.items():
            if val != 0:
                return False
        return True
            
            