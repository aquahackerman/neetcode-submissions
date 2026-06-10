class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        
        li = sorted(nums)
        print(li)
        l, r = 0, len(nums) - 1
        ar = [None] * len(nums)
        flag = True
        d = dict()
        i = 0
        while l != r and i!= 5:
            i += 1
            s = li[l] + li[r]
            negs = s * -1
            flag = True
            while flag is not False:
                flag = False
                if l == r:
                    break
                if negs >= li[r]:
                    r = r -1
                    flag = True
                elif negs <= li[l]:
                    l = l + 1
                    flag = True

            if negs in nums:
                if negs not in d:
                    d[negs] = [li[l], li[r]]
                else:
                    d[negs].append([li[l], li[r]])
            print("hi")
        
        print(d)
        """
        dic = {}
        

        for i, no in enumerate(nums):
            freq = dic.get(no, (-1, 0))[1]
            dic[no] = [i, freq + 1]
            
        nums = sorted(list(set(nums)))
        for i, no in enumerate(nums):
            dic[no][0] = i
        print(nums, dic)
        final_arr = []
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                diff = nums[j] + nums[i]
                diff = diff * -1
               
                if diff in dic:
                    index = dic[diff][0]
                    print(i,index,j)
                    if index > i and index < j:
                        final_arr.append([nums[i], diff, nums[j]])
                    elif index == i and index == j:
                        if dic[diff][1] > 2:
                            final_arr.append([nums[i], diff, nums[j]])
                    elif index == i:
                        if dic[diff][1] > 1:
                            final_arr.append([nums[i], diff, nums[j]])
                    elif index == j:
                        if dic[diff][1] > 1:
                            final_arr.append([nums[i], diff, nums[j]])
                
        return final_arr
