class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Hash of sorted string : list of words with that string
        anagrams = {}
        for word in strs:
            word_sorted = "".join(sorted(word))
            if word_sorted in anagrams:
                anagrams[word_sorted].append(word)
            else:
                anagrams[word_sorted] = [word]
        return list(anagrams.values())