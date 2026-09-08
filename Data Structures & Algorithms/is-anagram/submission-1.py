class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # Equal lenghts, so we can loop and add it to their dicts

        s_counts = {}
        t_counts = {}
        
        for i in range(len(s)):
            if s[i] not in s_counts:
                s_counts[s[i]] = 1
            if t[i] not in t_counts:
                t_counts[t[i]] = 1
            if s[i] in s_counts:
                s_counts[s[i]] += 1
            if t[i] in t_counts:
                t_counts[t[i]] += 1

        for character, count in s_counts.items():
            if character not in t_counts or count != t_counts[character]:
                return False
        return True