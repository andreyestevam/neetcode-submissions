class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l, r = 0 , 0
        seen = set()
        max_length = r - l + 1
        while r < len(s):
            if s[r] in seen:
                while s[r] in seen:
                    seen.discard(s[l])
                    l += 1
            seen.add(s[r])
            max_length = max(max_length, r - l + 1)
            r += 1
        return max_length