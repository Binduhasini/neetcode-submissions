class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq={}
        max_len=0
        left=0
        for right in range(len(s)):
            if s[right] in freq:
                freq[s[right]]+=1
            else:
                freq[s[right]]=1
            
            while freq[s[right]] > 1:
                freq[s[left]]-=1
                left+=1
            max_len=max(max_len,right-left+1)
        return max_len