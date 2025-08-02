Two Pointer:
    
    left = 0
    right = len(array) - 1
    
    while left < right:
        left += 1
        right -= 1
        
        
    start = 0
    for end in range(len(array)):
        
        
    def reverseString(s):
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s
        
        
        def twoSum(numbers, target):
            left, right = 0, len(numbers) - 1
            while left < right:
                total = numbers[left] + numbers[right]
                if total == taregt:
                    return [left, right]
                elif:
                    left += 1
                else:
                    right -= 1
                    
    sliding window technique where we create a "window" (subarray or substring) that slides through the input to process one part at a time - either of fixed or variable size.
    
    Maximum Sum Subarray of Size K
    
    def max_sum_k(nums, k):
        max_sum = curr_sum = sum(nums[:k])
        for i in range(k, len(nums)):
            curr_sum += num[i] - nums[i - k]
            max_sum = max[max_sum, curr_sum]
        return max_sum
        
        
        
        def max_sum_k(nums, k):
            curr_sum = max_sum = sum(nums[:k])
            
        nums[:k]
        this is slicing:
        it takes the first k elements of the list nums
        
        nums = [1,2,3,4,5]
        k = 3
        nums[:k] = [1,2,3]
        
        add th enum in slice = sum(nums[:k])
        max_sum = curr_sum = 6
        
        
        nums = [1, 4, 2, 10 , 2, 3]
        k = 3
        max_sum = curr_sum = sum(nums[:k])
        sum([1 ,4, 2]) = 7
        
        
        curr_sum += nums[i] - nums[i - k]
        nums = [1,4,2,10,2]
        curr_sum += 10 - 1 # 7 + 10 -1 = 16
        max_sum = max(max_sum, curr_sum)
        return max_sum
        
        
        def max_substring(s):
            char_set = set()
            left = max_len = 0
            
            for right in range(len(s)):
                while s[right] in char_set:
                    char_set.remove (s[left])
                    left += 1
                    char_set.add(s[right])
                    max_len = max(max_len, right - left +1)
            return max_len
            
            
            
            def two_sum(nums, target):
                hashmap = {}
                for i , in enumerate(nums):
                    complement = target - nums
                    if complement in hashmap:
                        return [hashmap[complement], i]
                    hashmap[num] = i
                    
            def two_sum(nums, target):
                hashmap ={}
                for i, in enumerate(nums):
                    complement = tareget - nums
                    if complement in hashmap:
                        index1 =  hashmap[complement]
                        index2 = i
                        return {
                            "indices": [index1, index2],
                            "values": [nums[index1, nums[index2]]
                        }
                    hashmap[num] = i
                        
                        

                
        def longest_consecutive(nums):
            num_set = set(nums)     # set banaya
            longest = 0     # longest ko 0 loya
            
            for num in nums:    #    iterate through the nums
                if num - 1 not in num_set:  # agar num -1 krne pe set me ni mila to 
                    length = 1 # length 1 return krenge
                    while num + length in num_set:      # now we check through all the num+length agar numset me mila to 
                        length += 1  #length count increase krte jayenge
                    longest = max(longest, length) # fir longest aur length ka max return kr denge last me
            return longest
            
            
    def twoSum(nums, target):
        hashmap = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[num] = i
            
    # we are using hashmap for lookup of previously stored numbers, to avoid nested loops.
    
    def longestConsecutive(nums):
        num_set = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in num_set:
                length = 1
                while length + num in num_set:
                    length += 1
                longest = max(longest, length)
        return longest
        
        
    def maxSubArray(nums):
        current_sum = max_sum = num[0] 
        for num in nums[1:]:  # iterating after item 1
            current_sum = max(num, current_sum + num) # finding current sum from the max of num and current sum + num
            max_sum = max(max_sum, current_sum) # now max sum from the maximum of current sum and max sum
        return max_sum # here returning max sum
    

        
        
        
        
        
        
    def duplicate(nums):
        freq = {}
        for num in nums:
            if num in freq:
                return True
            freq[num] = 1
        return False
            
            
            
    def findDuplicate(nums):
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
            
            
            
    def has_duplicate(nums):
    freq = {}
    for num in nums:
        if num in freq:
            return True  # Found a duplicate
        freq[num] = 1  # First time seeing this number
    return False  # No duplicates found
    
    
    def lengthOfLongestSubstring(s):
        seen = {}
        left = 0
        max_len = 0
        
        for right in range(len(nums)):
            if s[right] in seen and seen[s[right]] >= left:
                left = seen[s[right]] + 1
                seen[s[right]] = right
                max_len = max(max_len, right - left +1)
            return max_len
            
            
    
    
    
    def lengthofSubstring(s):
        seen = {}
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            if s[right] in seen and seen[s[right]] >= left:
                left = seen[s[right]] + 1
                seen[s[right]] = right
                max_len = max(max_len, right - left +1)
            return max_len
    
    
    
    def longestSusequence(s,t):
        i = 0
        for i in range():
            if i < len(s) and s[i] == char:  # agar length of s bada hai i se mtlb s me abhi bhi characters hain check krne ko
            i += 1. # to fir ham i ko badha denge next item pe
        return i == len(s)
        
        
    🔤 String Patterns
   ├── ✨ Sliding Window
   │   ├── Longest Substring (No Repeat)
   │   └── Min Window Substring
   ├── 🔁 Two Pointers
   │   ├── Palindrome Expand
   │   └── Is Subsequence
   └── 🧮 Frequency Count
       ├── Valid Anagram
       └── Group Anagram (extra)

                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
