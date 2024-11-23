import nltk

from nltk.tokenize import word_tokenize, sent_tokenize

text = "I believe this would help the reader understand how tokenization works. as well as realize its importance."

# Tokenize into sentences
sents = sent_tokenize(text)
print(sents)

# Tokenize into words
print(word_tokenize(text))

# Tokenize each sentence into words
words = [word_tokenize(sent) for sent in sents]
print(words)
