class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s)==0:
            return ""
        temp=""
        for i in range(0,len(s)):
            if  s[i].isalnum():
                temp=temp+s[i].lower()
        if temp!=temp[::-1]:
            return False
        return True

        
        