#fastest
class Soluton:
    def validAnag(self, s:str, t:str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = set()
        for letts in s:
            if s in t:
                return True
            seen.add(t)
        return False
    

            
        