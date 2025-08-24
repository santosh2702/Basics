   def subsets_bitmask(nums):
        n = len(nums)
        ans = []
        for mask in range(1 << n):
            cur = []
            for j in range(n):
                if (mask >> j) & 1:
                    cur.append(nums[j])
            ans.append(cur)
        return ans 
    
