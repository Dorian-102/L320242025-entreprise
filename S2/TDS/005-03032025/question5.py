word1 = "apple"
word2 = "banana"

lettre_commune = tuple(char for char in word1 if char in word2)

print(lettre_commune)