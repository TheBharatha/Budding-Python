class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine = list(magazine)
        foundNotes = 0
        for note in ransomNote:
            if note in magazine:
                magazine.pop(magazine.index(note))
                foundNotes += 1
        if foundNotes == len(ransomNote):
            return True
        else:
            return False
