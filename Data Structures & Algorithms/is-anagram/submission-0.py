class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = {}
        
        # 1. Use .get() to safely add new characters
        for char in s:
            count[char] = count.get(char, 0) + 1
            
        for char in t:
            # 2. Fixed typo: char[count] -> count[char]
            if char not in count or count[char] == 0:
                return False
            count[char] -= 1
            
        return True