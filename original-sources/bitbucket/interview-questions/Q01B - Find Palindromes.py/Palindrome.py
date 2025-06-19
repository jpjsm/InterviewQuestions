# Palindrome class

class Palindrome:
    def IsPalindrome(text):
        i = 0
        j = len(text)-1
        while i < j and text[i].lower() == text[j].lower():
            i += 1
            j -= 1
        
        return i >= j     
        
    def IsAlmostPalindrome(text):
        textLen = len(text)
        for k in range(0, textLen):
            if Palindrome.IsPalindrome(text[0:k] + text[k+1:textLen]):
                return True
        
        return False
        
    def IsAlmostPalindrome2(text):
        textLen = len(text)
        for k in range(0, textLen):
            i = 0
            j = textLen - 1
            while i < j:
                if i == k:
                    i+= 1

                if j == k:
                    j -= 1

                if text[i].lower() != text[j].lower():
                    break
            
                i += 1
                j -= 1

            if i >= j:
                return True

        return False
