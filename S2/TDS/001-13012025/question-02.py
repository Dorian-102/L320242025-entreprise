phrase = "The quick brown fox jumps over the lazy dog"

def est_pangramme_1(phrase):
    lettres = ''
    for car in phrase.lower():
        if car not in lettres and car != ' ':
            lettres += car
    return len(lettres) == 26

def est_pangramme_2(phrase):
    text = phrase.lower().replace(' ', '')
    return len(set(list(text))) == 26

print(est_pangramme_1(phrase))
print(est_pangramme_2(phrase))
