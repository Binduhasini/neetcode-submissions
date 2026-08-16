class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        res="".join(c for c in s if c.isalnum())
        left=0
        right=len(res)-1
        while left < right:
            if res[left] != res[right]:
                return False
                
            left+=1
            right-=1
        return True
            
            
