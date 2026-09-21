# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         if len(s)==0:
#             return ""
#         temp=""
#         for i in range(0,len(s)):
#             if  s[i].isalnum():
#                 temp=temp+s[i].lower()
#         if temp!=temp[::-1]:
#             return False
#         return True

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        while l<r:
            while l<r and not self.isalnumfun(s[l]):
                l+=1
            while r>l and not self.isalnumfun(s[r]):
                r-=1
            if s[l].lower()!=s[r].lower():
                return False
            l=l+1
            r=r-1
        return True
    

    def isalnumfun(self,c):
        return (
            ord('A')<=ord(c)<=ord('Z') or
            ord('a')<=ord(c)<=ord('z') or
            ord('0')<=ord(c)<=ord('9')
        )


        
        