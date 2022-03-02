import math
from nltk.tokenize import word_tokenize

class tokenizer:
    def __init__(self,term,sentence,corpus):
        self.term = term
        self.sentence = sentence.lower()
        self.corpus = corpus.split('.')
        self.tokens = word_tokenize(self.sentence)
        self.word_freqs = {}
        for token in self.tokens:
            self.word_freqs.setdefault(token,0)
            self.word_freqs[token]+= 1
    def term_frequency(self,term):
        num = (self.word_freqs.get(term))
        den = max(self.word_freqs.values())
        return 0.5 + 0.5*num/den
    def  inverse_term_document_frequency(self,term):
        n = len(self.corpus)
        num = (self.word_freqs.get(term))
        return log(num/n)
    def tfidtf (self,term):
        num = (self.word_freqs.get(term))
        den = max(self.word_freqs.values())
        tf = 0.5 + 0.5*num/den
        n = len(self.corpus)
        itdf = log(num/n)
        return tf*itdf


sent = tokenizer('The','the quick brown fox jumps over the lazy dog','The quick brown fox jumps over the lazy dog.Never jump over the lazy dog quickly')
print(sent.term_frequency('the'))
print(sent.inverse_term_document_frequency('the'))
print(sent.tfidtf('the'))