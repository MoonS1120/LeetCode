def reverseVowels(self, s: str) -> str:
        s = list(s)
        left = 0
        right = len(s)-1
        vowels = "AEIOUaeiou"

        while left < right:
            while s[left] not in vowels:
                left+=1
            while s[right] not in vowels:
                right-=1
            
            s[left], s[right] = s[right], s[left]
            left+=1
            right-=1
        
        return ''.join(s)
