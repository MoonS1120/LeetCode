def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []

        for i in range(len(word2)):
            result.append(word1[i])
            result.append(word2[i])
        return ''.join(result)
