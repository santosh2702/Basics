Longest substring without repeating:
    
    def longestsubstring(s):
        max_len = 0
        left = 0
        seen= {}
        
        for right in range(len(s)):
            if s[right] in seen and seen[s[right] >= left:
                left = seen[s[right]] + 1
            seen[a[right]] = right
            max_len = max(max_len, right - left + 1)
        return max_len
        
        
    def maxSum(arr, k):
        max_sum = curr = sum(arr[:k])
        for i in range(k, len(arr)):
            curr += arr[i] - arr[i-k]
            max_sum = max(max_sum, curr)
        return max_sum
        
        ok so max_sum = max(curr, max_sum)
        
        
        
        
        def longestSubstring(s):
            seen = set()
            left = 0
            max_len = 0
            
            for right in range(len(s)):
                while s[right] in seen:
                    seen.remove(s[left])
                    left += 1
                seen.add(s[right])
                max_len = max(max_len, right - left + 1)
            return max_len
                
                
                
                
        def characterReplacement(s, k):
            count = {}
            maxf = left = 0
            for right in range(len(s)):
                count[s[right]] = count.gets(s[right], 0) + 1
                maxf = max(maxf, count[s[right]])
                if (right - left + 1) - maxf > k:
                    count[s[left]] -= 1
                    left += 1
                return right - left + 1
                
                
        from collections import defaultdict
        def groupAnagrams(strs):
            anagram_group = defaultdict(list)
            for word in strs:
                key = ''.join(sorted(word))
                anagram_map[key].append(word)
            return list(anagram_map.values())
            
            
        from collection import counter
        import heapq
        def topKFrequent(nums, k):
            count = Counter(nums)
            return heapq.nlargest(k, countm key=count.get)
            
            
        def longestConsecutive(nums):
            num_set = set(nums)
            longest = 0
            
            
            for num in nums:
                if num - 1 not in num_set:
                    length = 1
                    while num + length in num_set:
                        length += 1
                    longest = max(longest, length)
            return longest
            
            
            
    def groupAnagram(strs):
        anagram_map = 0
        for word in strs:
            key=''.join(sorted(word))
            if key not in anagram_map:
                anagram_map[key] = []
            anagram_map[key].append(word)
        return list(anagram_map.values())
        
        
        
        
    
    
    
    
    
    def longestConsecutive(nums):
        num_set = set(nums)
        longest = 0
        
        for num in nums:
            if num - 1 not in num_set:
                length = 1
                while num + length in num_set:
                    length += 1
                longest = max(length, longest)
        return longest
        
    
    def lengthOfLongestSubstring(s):
        seen = set()
        left = max_len = 0
        
        
    
    
    from collections import Counter
    import heapq
    
    def topKFrequent(num, k):
        count = Counter(nums)
        return heapq.nlargest(k, count, key=count.get)
        
        
    def topKFrequent(num, k):
        count = Counter(nums)
        return heapq.nlargest(k, count, key=count.get)
        
        
    def topkFrequent(num ,k):
        count = Counter(nums)
        return heapq.nlargest(k, count, key=count.get) 
        
    heapq is a python library that allows you to use a heap data structure (specially, a min heap) to efficiently get th esmallest (or largest) items from a list
        
        
    def middlenumber(nums):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    
    
    
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            
        
