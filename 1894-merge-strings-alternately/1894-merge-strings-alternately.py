class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        length = min(len(word1), len(word2))
        for i in range(length):
            merged.append(word1[i])
            merged.append(word2[i])
        # from this we will get a alternately merged list of characters, now we have to check for remaining

        merged.append(word1[length:])
        merged.append(word2[length:])
        
        return "".join(merged)