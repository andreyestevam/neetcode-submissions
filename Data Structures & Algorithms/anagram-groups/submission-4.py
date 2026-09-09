class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for s in strs: # n is the number of strings in the list
            count = [0] * 26 # characters from a to z

            for c in s: # m is the average length of the string
                count[ord(c) - ord("a")] += 1
            result[tuple(count)].append(s) # Make it a tuple since it's immutable
        
        return list(result.values())