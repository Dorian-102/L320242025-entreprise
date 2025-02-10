from texte import TEXTE
from functools import reduce

def count_words(dico, word):
    dico[word] = dico.get(word, 0) + 1
    return dico

word_count = reduce(count_words, TEXTE.split(), {})
print(word_count)

