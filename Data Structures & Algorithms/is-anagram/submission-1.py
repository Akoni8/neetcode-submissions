class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letters1 = dict()
        letters2 = dict()
        for letter in range(len(s)):
            letter1 = s[letter]
            letter2 = t[letter]
            if letter1 in letters1:
                letters1[letter1] = letters1[letter1] + 1
            else:
                letters1[letter1] = 1

            if letter2 in letters2:
                letters2[letter2] = letters2[letter2] + 1
            else:
                letters2[letter2] = 1
        for letter in s:
            if letters1.get(letter) != letters2.get(letter):
                return False
        return True
        