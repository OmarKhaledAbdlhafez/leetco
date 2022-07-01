class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count_magazine = collections.Counter(magazine)
        count_ransomNote = collections.Counter(ransomNote)
        for char in ransomNote:
            if count_ransomNote[char] > count_magazine[char]:
                return False
        return True
        