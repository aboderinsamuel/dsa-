class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = set()
        for letts in s:
            if s in t:
                return True
            seen.add(t)
        return False
        