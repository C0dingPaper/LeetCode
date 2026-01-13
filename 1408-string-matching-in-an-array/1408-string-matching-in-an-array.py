class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        results = set()
        sorted_words = sorted(words, key=len)
        for i in range(len(words)):
            # For the word to be a substring a in b
            word = sorted_words[i]
            s = sorted_words[i+1:]
            for j in s:
                if word in j:
                    results.add(word)
                    break
        return list(results)


