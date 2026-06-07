class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq={}
        freq1={}
        for ch in range(len(s)):
            if s[ch] in freq:
                freq[s[ch]]+=1
                
            else:
                freq[s[ch]]=1
        for ch in range(len(t)):
            if t[ch] in freq1:
                freq1[t[ch]]+=1
            else:
                freq1[t[ch]]=1
        if freq== freq1:
            return True
        return False