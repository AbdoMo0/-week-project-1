# Abdelrhman Mohamed 11/314a

class Solution(object):
    def sortSentence(self, s):
        words = s.split()
        sorted_words = sorted(words, key=lambda x: int(x[-1]))  
        original_sentence = ' '.join(word[:-1] for word in sorted_words)  
        return original_sentence
