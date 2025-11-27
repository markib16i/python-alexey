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
        # Handle words that start with a vowel
        pig_word = word + 'yay'
    else:
        # Handle words that start with a consonant
        consonants = ""
        for letter in word:
            if letter in 'aeiou':
                break
            else:
                consonants += letter
        pig_word = word[len(consonants):] + consonants + "ay"
    pig_words.append(pig_word)


 # lst.append(new_el)

# Assemble words back into a phrase, print the result