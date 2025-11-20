"""If a word starts with a consonant,
move the first consonant (or group of consonants) to the end and add “ay”.

    Example:

        dog → ogday

        school → oolschay

If a word starts with a vowel, just add “way” or “yay” to the end.

    Example:

        apple → appleway

        orange → orangeway
"""

# Get user phrase as an input
english_phrase = input("Type a word/sentence/phrase: ")

# Separate phrase into words
words = english_phrase.split()

# Translate each word to Pig Latin

pig_words = []


for word in words:
    if word[0] in 'aeiou':
        pig_word = word + 'yay'
    else:
        # TODO: Figure out the index of the first vowel
        for letter in word:
            if letter in 'aeiou':
                ...
            else:
                ...

        # TODO: Find the index of character "a" in the word
        # s.index(character)


        # TODO: Split the word by that index
        # TODO: Construct the pig word from the parts and "ay"
    pig_words.append(pig_word)


 # lst.append(new_el)

# Assemble words back into a phrase, print the result