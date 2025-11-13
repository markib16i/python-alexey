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
english_phrase = input("Type a word/sentence/phrase. I am going to translate it to pig latin. ")

# Separate phrase into words
words = english_phrase.split()
# print(words)

# Translate each word to Pig Latin
# TODO: Make a new empty list for pig words
for i in words:
    # print(i)
    if i[0] in 'aeiou':
       pig_word = i + 'yay'
    # TODO: append the new pig word to the list of pig words

# Assemble words back into a phrase, print the result