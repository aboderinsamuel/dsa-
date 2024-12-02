#Brute Force
class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]

#better:
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left +=1
            while right > left and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
    
#or
class Solution:
    def alphNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
    
    def isPalindrome(self, c:str) -> bool:
        left, right = 0, len(c) - 1
        while left < right:
            while left < right and not self.alphNum(c[left]):
                left += 1
            while right > left and not self.alphNum(c[right]):
                right -= 1
            if c[left].lower() != c[right].lower():
                return False
            left += 1
            right -= 1
        return True
