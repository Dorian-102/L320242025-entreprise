sentence = (
    "The rocket, who was 6 named Ted, came back "
    "from Mars because he missed his friends."
)


def is_consonant(letter):
    vowels = "aeiou"
    return letter.isalpha() and letter.lower() not in vowels


print([char for char in sentence if is_consonant(char)])
