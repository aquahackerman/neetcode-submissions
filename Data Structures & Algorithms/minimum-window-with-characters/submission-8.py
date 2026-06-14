class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        letter_count = {}
        for letter in t:
            
            letter_count[letter] = letter_count.get(letter, 0) + 1
        
        min_index, min_len = -1, len(s)
        for o_index in range(len(s)):
            temp_dic = letter_count.copy()
            count = 0
            
            for i_index in range(o_index, len(s)):
                if s[i_index] in temp_dic:
                    
                    if temp_dic[s[i_index]] == 1:
                        temp_dic[s[i_index]] = 0
                        count += 1
                    else:
                        if not temp_dic[s[i_index]] == 0:
                            temp_dic[s[i_index]] -= 1
                if count == len(letter_count):
                    if i_index - o_index < min_len:
                        min_len = i_index - o_index
                        min_index = o_index
        print(min_len, min_index)
        if min_index == -1:
            return ""
        return s[min_index : min_len + 1 + min_index]
        
