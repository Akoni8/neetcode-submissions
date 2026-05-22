class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word1 = {}
        word2 = {}

        for letter in s:
            if not letter in word1:
                word1[letter] = 1
            else:
                word1[letter] += 1

        for letter in t:
            if not letter in word2:
                word2[letter] = 1
            else:
                word2[letter] += 1

        for key, value in word1.items():
            if not key in word2:
                return False
            elif not word2[key] == word1[key]:
                return False 

        for key, value in word2.items():
            if not key in word1:
                return False
        return True