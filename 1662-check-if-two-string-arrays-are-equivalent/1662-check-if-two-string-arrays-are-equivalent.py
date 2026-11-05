class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        result1="".join(word1)
        result2="".join(word2)
        if result1==result2:
            return True
        else:
            return  False