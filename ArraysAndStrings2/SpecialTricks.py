class SpecialTricks :
    def reverseWordsInASentence(self, sentence, start,end):
        def reverse(s) :
            left = start
            right = end

            while left <= right :
                s[left],s[right] = s[right],s[left]
                left += 1
                right -= 1

            return sentence

        reversedSentence = reverse(sentence)

        left = 0
        for i in range(len(reversedSentence)-2) :
            if reversedSentence[i+1] == " " :
                reverse(reversedSentence, left,i)
                left = i + 2

        reverse(reversedSentence, left, len(sentence)-1)

        return reversedSentence

    def maxPalindrome(self, s, left,right):

        while left >= 0 and right < len(s) :
            if s[left] != s[right]:
                break
            continue

        return left - right + 1
    def longestPalindromicSubstring(self, s):
        result = 0
        for i in range(len(s)-1) :
            result = max(result, self.maxPalindrome(s,i,i), self.maxPalindrome(s,i,i+1))